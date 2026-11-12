# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo se organiza un programa DLP que trabaja con el SOC, los equipos de endpoint y de red, los dueños de datos y privacidad: responsabilidades, procedimientos, métricas, mejora continua y gobierno en MCSA, sin interpretar la ley.

*L300–L400 · 3 módulos · ~11 horas · 10 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno, privacidad y MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo y responsabilidades

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

Un programa DLP no lo opera una sola persona: lo operan el equipo de seguridad de datos, el SOC, los equipos de endpoint y de red, los dueños de datos de cada área y privacidad. La guía oficial de planificación sugiere empezar por las partes interesadas, las categorías de información y los objetivos, y recuerda que la mayoría de las necesidades son regulatorias (alrededor del 85 %) y una parte menor, de propiedad intelectual. Sin roles claros, cada bloqueo se vuelve una negociación y cada alerta, un huérfano.

Para grupos que operan en varios países, las **unidades administrativas** permiten un modelo descentralizado y «cercado»: cada país administra e investiga lo suyo mientras el equipo central mantiene las directivas globales. Algunas piezas no reconocen unidades administrativas —los agentes de Purview o la DLP de apps no Microsoft conectadas— y deben quedar en el equipo central. Los diagramas de arquitectura de referencia de Purview y las sesiones de Ignite 2025 sobre modernizar un DLP heredado y gestionar el cambio son la base de este módulo.

**Por qué importa**

La mayoría de los programas DLP fracasan por organización, no por tecnología: directivas sin dueño, excepciones sin vencimiento y alertas que nadie revisa. Un RACI explícito, un proceso de cambios con criterio de salida de la simulación y un modelo por país con gobierno central acortan el tiempo de respuesta, reducen los conflictos con el negocio y sostienen el programa cuando cambian las personas.

**Qué vas a lograr**

- Definir un RACI entre DLP, SOC, endpoint, red, dueños de datos y privacidad.
- Diseñar un modelo descentralizado con unidades administrativas y gobierno central.
- Establecer el procedimiento de cambios de directivas, de la simulación al bloqueo.
- Gestionar excepciones con dueño, justificación y vencimiento.

> **Consejo Ninja.** La [guía de planificación](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp) propone empezar por las partes interesadas, las categorías de información y los objetivos, y señala que las necesidades suelen ser cerca de 85 % regulatorias y 15 % de propiedad intelectual. Úsalo para priorizar el backlog del programa con el negocio.

> **Novedad.** Abril de 2026: Microsoft publicó [tres arquitecturas de referencia](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/deploy-scalable-ring%E2%80%91fenced-purview-operations-with-administrative-units/4512556) para operar Purview de forma descentralizada con unidades administrativas (por región o por poblaciones sensibles) sin perder el gobierno central, y [diagramas de referencia](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925) de clasificación, etiquetas, DLP por carga de trabajo e Insider Risk en PowerPoint, actualizados el 9 de septiembre de 2026.

> **Consejo Ninja.** Las sesiones de Ignite 2025 [BRK255](https://www.youtube.com/watch?v=6Gp21z39nQU) (buenas prácticas, indicadores de éxito y gestión del cambio) y [BRKSP473](https://www.youtube.com/watch?v=Zy_kxJSeYGo) (caso de PwC al pasar de un DLP heredado lleno de alertas a un programa gobernado) son el mejor insumo para presentar el modelo operativo a la dirección. La segunda es una sesión patrocinada por un partner.

> **Atención.** Algunas piezas no reconocen unidades administrativas: los agentes de Purview solo las respetan por el contexto del administrador ([agentes](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)) y la DLP de apps no Microsoft conectadas no las admite ([apps conectadas](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications)). En un modelo por país, esas piezas quedan en manos del equipo central.

**¿Tienes poco tiempo?**

- [Plan for data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp) · Documentación
- [Deploy scalable ring-fenced Purview operations with Administrative Units](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/deploy-scalable-ring%E2%80%91fenced-purview-operations-with-administrative-units/4512556) · Blog oficial
- [Microsoft Purview Referential Architecture Diagrams](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925) · Blog oficial
- [Best practices to maximize Microsoft Purview data security solutions | BRK255](https://www.youtube.com/watch?v=6Gp21z39nQU) · Video

### Anuncios y blogs oficiales

- [Deploy scalable ring-fenced Purview operations with Administrative Units](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/deploy-scalable-ring%E2%80%91fenced-purview-operations-with-administrative-units/4512556) · Blog oficial · Empleado de Microsoft · Maxime Bombardier · Microsoft Purview Blog (Tech Community) · 17 abr 2026. Tres arquitecturas de referencia para operar DLP de forma descentralizada con unidades administrativas (regiones, poblaciones sensibles) sin perder gobierno central.
- [Microsoft Purview Referential Architecture Diagrams](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925) · Blog oficial · Empleado de Microsoft · Maxime Bombardier · Microsoft Purview Blog (Tech Community) · 13 abr 2026. Diagramas de referencia del equipo de Customer Experience Engineering de Purview sobre clasificación, etiquetas, DLP por carga de trabajo (endpoint, Exchange, SharePoint, navegador), IRM y Copilot.

### Webinars, videos y podcasts

- [Best practices to maximize Microsoft Purview data security solutions | BRK255](https://www.youtube.com/watch?v=6Gp21z39nQU) · Video · Empleado de Microsoft · Nick Caromano, Vivian Ma, Antonio Maio, Aashish Ramdas, Scott Whittington · Microsoft Events (YouTube) · nov 2025. Sesión de Ignite 2025 con historias reales de implementación de clasificación, etiquetas y DLP: modernizar DLP heredado, indicadores de éxito, gestión del cambio y colaboración transversal.
- [Envision next generation DLP with Microsoft Purview and Copilot | BRKSP473](https://www.youtube.com/watch?v=Zy_kxJSeYGo) · Video · Comunidad · Adam Ames, Nick Caromano, Josh Rattan · Microsoft Events (YouTube) · nov 2025. Caso de PwC y Microsoft (Ignite 2025) sobre pasar de un DLP heredado lleno de alertas a un programa con gobierno, alineación ejecutiva, aplicación automatizada y Security Copilot.

**Manos a la obra**

1. `Laboratorio` Construye el RACI del programa DLP con seis roles (DLP, SOC, endpoint, red, dueños de datos y privacidad) y diez actividades: diseño, simulación, activación, excepciones, triage, investigación, escalamiento a RR. HH. y Legal, cambios de licencias, métricas y retiro de directivas ([planificación](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp)). Evidencia: matriz RACI de una página.
2. `Laboratorio` Elige la arquitectura de [unidades administrativas](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/deploy-scalable-ring%E2%80%91fenced-purview-operations-with-administrative-units/4512556) que mejor se ajuste a tu grupo y pruébala con una unidad administrativa de prueba y un administrador acotado. Evidencia: diagrama y captura de lo que ve el administrador acotado.
3. `Laboratorio` Escribe el procedimiento de cambios: solicitud, diseño, copia v2 en simulación, criterio de salida, aprobación del dueño del proceso, activación por ubicación, comunicación a las personas y revisión a los 30 días. Evidencia: procedimiento con plantilla de solicitud.
4. `Laboratorio` Define el registro de excepciones —dueño, justificación, alcance, fecha de vencimiento y revisión— y aplícalo a una excepción de tus directivas de prueba. Evidencia: registro con una excepción completa.
5. `Solo producción` Presenta el modelo operativo al comité de seguridad o de riesgos y acuerda el RACI con los dueños de datos de dos áreas, apoyándote en los [diagramas de referencia](https://techcommunity.microsoft.com/blog/microsoft-purview-blog/microsoft-purview-referential-architecture-diagrams/4510925). Cómo hacerlo seguro: piloto con dos áreas voluntarias, ningún cambio técnico hasta la aprobación y revisión a los 90 días antes de ampliar.

**¿Quieres profundizar?**

- [Envision next generation DLP with Microsoft Purview and Copilot | BRKSP473](https://www.youtube.com/watch?v=Zy_kxJSeYGo) · Video

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

Lo que no se mide no mejora y, en DLP, lo que se mide mal empeora: contar bloqueos sin contar falsos positivos premia las directivas ruidosas. Purview ofrece fuentes para un tablero honesto: los **reportes de postura** de Information Protection y DLP (vista previa, ventana de 30 días y sin directivas en simulación; reportes personalizados en vista previa desde mayo de 2026), el **panel de salud de dispositivos** (cobertura de incorporación y preparación para JIT, actualizado cada hora) y el KPI de DSPM de porcentaje de activos sensibles protegidos por al menos una directiva DLP.

La mejora continua cierra el ciclo: revisar las recomendaciones al menos cada 30 días, convertir cada falso positivo en un ajuste probado en simulación y medir si el ajuste funcionó. El proyecto comunitario Data Security Workbench, publicado por un empleado de Microsoft, propone justamente ese ciclo de observar, explicar, mejorar y probar sobre las alertas DLP. Publica las métricas agregadas por área y no por persona, y acuerda con privacidad qué se comparte con la dirección.

**Por qué importa**

La dirección no financia lo que no entiende. Un tablero mensual con cobertura, precisión, tiempo de triage y riesgo residual traduce el trabajo técnico en reducción de riesgo y permite priorizar inversiones —por ejemplo, entre ampliar Endpoint DLP o habilitar la protección de red— con datos y no con intuición.

**Qué vas a lograr**

- Definir KPI de cobertura, precisión, operación y riesgo para DLP.
- Construir un tablero mensual con reportes de postura, salud de dispositivos y DSPM.
- Conservar el histórico de los reportes que solo muestran 30 días.
- Aplicar un ciclo de mejora continua con evidencia antes y después de cada ajuste.

> **Atención.** Los [reportes de postura](https://learn.microsoft.com/en-us/purview/purview-reports) de Information Protection y DLP están en vista previa, muestran una ventana móvil de 30 días y no incluyen directivas en simulación: expórtalos a PDF cada mes para conservar el histórico. Los reportes personalizados entraron en vista previa en mayo de 2026 ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** El KPI de DSPM «porcentaje de activos sensibles protegidos por al menos una directiva DLP» es el mejor indicador de cobertura para la dirección; la guía recomienda revisar las recomendaciones al menos cada 30 días ([DSPM, paso 3](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3)). Para Fabric, los insights de actividad y adopción de DLP están en el catálogo de OneLake ([Fabric y Power BI](https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started)), y el [panel de salud de dispositivos](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard) muestra 30 días de cobertura con actualización horaria.

> **Novedad.** Septiembre de 2026: un empleado de Microsoft publicó [Data Security Workbench](https://techcommunity.microsoft.com/blog/microsoft-security-blog/from-dlp-alert-volume-to-measurable-detection-assurance/4545973), un punto de partida de código abierto que vincula incidentes con evidencia, separa el ruido con IA gobernada, propone ajustes y mide su efecto ([repositorio](https://github.com/jonnords/dataworkbench)). Es una herramienta comunitaria, no un producto soportado.

**¿Tienes poco tiempo?**

- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación
- [Step 3: Understand data landscape and risks - Deploy and use Data Security Posture Management](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3) · Documentación
- [Monitor device health with the device health reports dashboard](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard) · Documentación

### Documentación, cursos y credenciales

- [Monitor device health with the device health reports dashboard](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard) · Documentación · Oficial · Microsoft Learn. Panel de salud de dispositivos para Endpoint DLP: cobertura de incorporación, dispositivos en riesgo de no recibir actualizaciones, última conexión y preparación para JIT y "pegar en navegador".
- [Step 3: Understand data landscape and risks - Deploy and use Data Security Posture Management](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-dspm-step3) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Guía DSPM para revisar reportes, tendencias y recomendaciones, incluido el KPI de porcentaje de activos sensibles protegidos por al menos una directiva DLP.
- [Microsoft Purview posture reports overview](https://learn.microsoft.com/en-us/purview/purview-reports) · Documentación · Oficial · Vista previa · Microsoft Learn. Reportes de postura de Information Protection y DLP (preview): reglas y actividades más disparadas, directivas con mayor volumen y principales infractores, más reportes personalizados. *Nota:* Ventana móvil de 30 días (exportar a PDF para histórico); las directivas en simulación no aparecen

**Manos a la obra**

1. `Laboratorio` Define ocho KPI con fórmula y fuente: cobertura de dispositivos incorporados ([panel de salud](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard)), porcentaje de activos sensibles protegidos (DSPM), tasa de falsos positivos por regla, tasa de invalidaciones, alertas por día, tiempo de triage, directivas en simulación con más de 30 días y excepciones vencidas. Evidencia: ficha de KPI.
2. `Laboratorio` Construye el tablero mensual con los [reportes de postura](https://learn.microsoft.com/en-us/purview/purview-reports) (reglas, actividades y personas con más coincidencias), el panel de salud de dispositivos y el KPI de DSPM, y exporta los reportes a PDF. Evidencia: tablero de una página con los PDF archivados.
3. `Laboratorio parcial` Prueba [Data Security Workbench](https://github.com/jonnords/dataworkbench) en el tenant de laboratorio (Node.js 20 o posterior, PowerShell 7 y permisos delegados de lectura de alertas e incidentes): observa, explica y propone un ajuste sobre tus alertas DLP de prueba. Limitación: con pocas alertas el análisis es demostrativo, y es una herramienta comunitaria con la aplicación en vivo deshabilitada por defecto. Evidencia: informe del ciclo observar, explicar, mejorar y probar.
4. `Laboratorio` Aplica el ciclo de mejora a un ajuste de [M1](02_Nivel_2_Intermedio.md#m1): mide la tasa de falsos positivos antes, aplica el cambio en la copia v2, mide después y documenta la decisión. Evidencia: ficha antes y después.
5. `Solo producción` Presenta el primer tablero mensual a la dirección con datos reales. Cómo hacerlo seguro: datos agregados sin nombres de personas, revisión previa de privacidad, roles de solo lectura para quien prepara el tablero y metas acordadas con los dueños de datos antes de publicarlas.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

DLP procesa datos personales para proteger datos personales, y esa paradoja exige gobierno. Las coincidencias revelan quién envió qué; la recolección de evidencia guarda copias completas de archivos; la captura de prompts y respuestas de IA se define en las directivas de recopilación; la DLP adaptativa muestra nombres reales en las alertas; y un socio SASE puede almacenar parte de la configuración, incluidos identificadores de usuario. Cada una de esas decisiones debe revisarse con Legal, privacidad y, cuando corresponda, RR. HH., antes de activarla.

En MCSA, las directivas también deben reflejar las normas y los identificadores de cada país. El catálogo de SIT incluye identificadores de Argentina, Brasil, Chile, Colombia y Ecuador (en junio de 2026 se sumaron la cédula y el número de identificación tributaria de Colombia); para el resto conviene verificar la cobertura y crear SIT personalizados cuando falten. La hoja «Normativa MCSA» del libro de Excel resume leyes de privacidad, ciberseguridad y del sector financiero de la región como punto de partida para la conversación con Legal: esta guía no interpreta la ley.

**Por qué importa**

Un programa DLP que ignora la privacidad puede convertirse en un incidente de privacidad: evidencias con datos de terceros sin control de acceso, monitoreo sin base legal o datos procesados fuera de la región sin evaluación. Gobernar desde el diseño reduce el riesgo regulatorio y reputacional y facilita demostrar diligencia ante las autoridades de protección de datos de cada país.

**Qué vas a lograr**

- Mapear los SIT disponibles a los identificadores de cada país de MCSA donde operas.
- Identificar las decisiones de DLP con impacto en privacidad y quién debe aprobarlas.
- Diseñar el almacenamiento de evidencias con compartimentación, acceso mínimo y retención definida.
- Preparar un resumen normativo por país con fuentes oficiales para la revisión de Legal.

> **Novedad.** Junio de 2026: el catálogo de SIT sumó la cédula y el número de identificación tributaria de Colombia ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). El catálogo incluye identificadores de Argentina, Brasil, Chile, Colombia y Ecuador; para los demás países de MCSA verifica la cobertura y crea SIT personalizados con palabras clave en español cuando falten ([definiciones de SIT](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions)).

> **Atención.** Decisiones con impacto en privacidad que deben pasar por Legal y privacidad: la captura de prompts y respuestas de IA en directivas de recopilación ([referencia](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference)); la recolección de evidencia, que guarda copias completas de archivos ([evidencia](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started)); un SASE de terceros, que puede acceder a parte de la configuración e identificadores de usuario y almacenarlos ([red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)); y la DLP adaptativa, que muestra nombres reales en las alertas.

> **Atención.** Esta guía no interpreta la ley. La hoja «Normativa MCSA» del libro de Excel resume normas de la región con su fuente, por ejemplo la nueva [LFPDPPP de México](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) (marzo de 2025), la [Ley 21.719 de Chile](https://www.leychile.cl/leychile/Navegar?idNorma=1209272&idParte=1), que entra en vigencia el 1 de diciembre de 2026, la [Ley 1581 de Colombia](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) y el [reglamento de la Ley 29733 de Perú](https://cdn.www.gob.pe/uploads/document/file/7756037/6554453-reglamento-de-la-ley-n-29733.pdf?v=1741726731). Los plazos de notificación de vulneraciones varían mucho entre países: confírmalos siempre con Legal.

**¿Tienes poco tiempo?**

- [Sensitive information type entity definitions](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions) · Documentación
- [Collection policy reference](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference) · Documentación
- [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started) · Documentación

### Documentación, cursos y credenciales

- [Sensitive information type entity definitions](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions) · Documentación · Oficial · Microsoft Learn. Catálogo oficial de SIT con su definición; incluye identificadores de la región (Argentina DNI y CUIT/CUIL, Brasil CPF/CNPJ/RG, Chile, Colombia, Ecuador) útiles para directivas alineadas a normas locales.
- [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started) · Documentación · Oficial · Microsoft Learn. Configura la recolección de evidencia (copias de archivos coincidentes) desde dispositivos hacia almacenamiento Azure, con roles de vista previa/descarga y opciones de inmutabilidad.
- [Collection policy reference](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference) · Documentación · Oficial · Microsoft Learn. Anatomía de las directivas de recopilación que definen qué actividades y orígenes (dispositivos, IA empresarial, apps no administradas, navegador y red) se capturan, incluida la captura de prompts y respuestas de IA.

**Manos a la obra**

1. `Laboratorio` Construye el mapa de SIT por país: para cada país donde operas, lista los identificadores (fiscal, de identidad, de seguridad social y bancarios), si existe un SIT integrado en el [catálogo](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions) y, si no, el diseño del SIT personalizado (patrón, palabras clave en español y validación). Evidencia: tabla por país.
2. `Laboratorio` Crea un SIT personalizado para un identificador que no tenga SIT integrado, con datos sintéticos de formato y dígito verificador válidos, y pruébalo con un caso válido y uno inválido ([probar un SIT](https://learn.microsoft.com/en-us/purview/sit-test-a-sit)). Evidencia: resultados de la prueba.
3. `Laboratorio` Revisa con criterio de privacidad la recolección de evidencia de [M2](02_Nivel_2_Intermedio.md#m2): cuentas de almacenamiento separadas por población (por ejemplo, RR. HH. y ejecutivos), quién ve y quién descarga, retención y opción de inmutabilidad ([evidencia](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started)). Evidencia: diseño revisado por tu equipo.
4. `Laboratorio` Prepara para Legal una ficha por país con la norma de privacidad aplicable, su autoridad y el plazo de notificación que reporta la hoja «Normativa MCSA», más las decisiones de DLP que requieren su revisión. Evidencia: ficha con fuentes oficiales, marcada como «para revisión de Legal».
5. `Solo producción` Somete a una evaluación de impacto de privacidad las capacidades de DLP que tratan datos personales (evidencia, captura de prompts, red con socios y DLP adaptativa). Cómo hacerlo seguro: participación de Legal, privacidad, RR. HH. y, cuando corresponda, de la representación de los trabajadores; activación solo después de la aprobación; aviso a las personas cuando corresponda y revisión anual.

<a id="reto-operacion"></a>

## Reto del nivel

**El programa ante el comité.** Presenta el programa DLP como si fuera ante el comité de riesgos: RACI, modelo por país con unidades administrativas, tablero mensual con ocho KPI, mapa de SIT por país, decisiones de privacidad pendientes para Legal y hoja de ruta de seis meses (incluidos el retiro de «Instances» y las capacidades en vista previa que validarás después de Ignite). Entregables: resumen ejecutivo de una página y diez minutos de exposición.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Según la guía de planificación de DLP, ¿cómo suelen repartirse las necesidades de protección?
   - a) Cerca de 85 % regulatorias y 15 % de propiedad intelectual
   - b) 50 % regulatorias y 50 % de propiedad intelectual
   - c) 15 % regulatorias y 85 % de propiedad intelectual
   - d) 100 % regulatorias

2. ¿Qué permite el modelo «cercado» (ring-fenced) con unidades administrativas?
   - a) Eliminar el equipo central
   - b) Que cada país administre e investigue lo suyo mientras el equipo central mantiene el gobierno
   - c) Compartir alertas con otros tenants
   - d) Prescindir de las licencias E5

3. ¿Qué pieza de DLP no admite unidades administrativas y debe quedar en el equipo central?
   - a) Las directivas de Exchange
   - b) Las alertas de Endpoint DLP
   - c) La DLP de apps no Microsoft conectadas (vista previa)
   - d) Los SIT integrados

4. ¿Qué limitación tienen los reportes de postura de Information Protection y DLP?
   - a) Muestran un año de datos
   - b) Incluyen las directivas en simulación
   - c) Solo se exportan a Excel
   - d) Usan una ventana móvil de 30 días y no incluyen directivas en simulación

5. ¿Qué KPI de DSPM mide la cobertura de DLP?
   - a) Número de directivas creadas
   - b) Porcentaje de activos sensibles protegidos por al menos una directiva DLP
   - c) Cantidad de alertas por día
   - d) Número de personas bloqueadas

6. ¿Qué datos ofrece el panel de salud de dispositivos de Purview?
   - a) Solo el inventario de licencias
   - b) El contenido de los archivos bloqueados
   - c) Las alertas de Defender for Endpoint
   - d) Cobertura de incorporación, dispositivos en riesgo de no recibir actualizaciones y preparación para JIT, con 30 días de datos

7. ¿Cómo conservas el histórico de los reportes de postura, que solo muestran 30 días?
   - a) No es posible conservarlo
   - b) Activando una retención de un año en el reporte
   - c) Exportándolos a PDF de forma periódica
   - d) Pidiendo un respaldo a soporte

8. ¿Qué ciclo propone Data Security Workbench para las alertas DLP?
   - a) Observar, explicar, mejorar y probar
   - b) Bloquear, notificar y cerrar
   - c) Detectar, contener, erradicar y recuperar
   - d) Planificar, comprar y desplegar

9. ¿Qué identificadores agregó el catálogo de SIT en junio de 2026?
   - a) RFC y CURP de México
   - b) RUT de Chile
   - c) La cédula y el número de identificación tributaria de Colombia
   - d) DNI de Perú

10. ¿Qué recomienda la guía sobre las cuentas de almacenamiento para la evidencia de endpoints?
   - a) Una sola cuenta compartida por todas las áreas
   - b) Compartimentarlas por población y limitar quién descarga
   - c) Usar almacenamiento público para facilitar las auditorías
   - d) No definir retención

11. Con un SASE de terceros para la DLP de red, ¿qué debe revisar privacidad?
   - a) Nada, porque el socio no recibe datos
   - b) Solo el precio por solicitud
   - c) Que el socio reemplaza a Purview
   - d) Que el socio puede acceder a parte de la configuración, incluidos identificadores de usuario, y almacenarla

12. ¿Dónde se define en Purview la captura de prompts y respuestas de IA?
   - a) En las directivas de recopilación
   - b) En las etiquetas de retención
   - c) En Defender for Cloud Apps
   - d) En el centro de administración de Teams

13. Según la hoja «Normativa MCSA», ¿desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?
   - a) 1 de enero de 2025
   - b) 1 de diciembre de 2026
   - c) 20 de marzo de 2025
   - d) Rige desde 2012

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

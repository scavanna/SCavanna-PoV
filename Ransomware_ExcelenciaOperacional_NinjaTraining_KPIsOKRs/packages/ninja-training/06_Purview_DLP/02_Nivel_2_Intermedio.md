# Nivel 2 · Intermedio · Ajustar, investigar y extender

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Reducción de falsos positivos, alertas e investigación, DLP para Copilot, IA generativa y la red, y protección adaptativa con Insider Risk. Terminas con una línea base de falsos positivos, un runbook de triage con el SOC y directivas para Copilot y la protección adaptativa en modo de prueba.

*L300 · 4 módulos · ~25 horas · 32 recursos*

**Módulos de este nivel:** [M1 Ajuste y falsos positivos](#m1) · [M2 Alertas e investigación](#m2) · [M3 Copilot, IA y red](#m3) · [M4 Protección adaptativa](#m4)

<a id="m1"></a>

## M1 · Ajuste y reducción de falsos positivos

*L300 · ~6 h · Origen: Ruta Ninja de Learn, módulo 1 (tipos de información confidencial), aplicado al ajuste de DLP*

Los falsos positivos son el enemigo silencioso de un programa DLP: generan fatiga de alertas, fricción con las personas y pérdida de confianza en el equipo. En 2026 Microsoft publicó un modelo de despliegue en cuatro pasos para reducirlos: tipos de información confidencial (SIT) por patrones bien configurados, Exact Data Match, clasificadores entrenables y huellas digitales de documentos. El primer paso concentra la mayor parte de las ganancias: clonar los SIT integrados, elegir el elemento primario correcto, usar la proximidad de 300 caracteres, subir el nivel de confianza (baja ≤65, media 75, alta 85) y agregar exclusiones.

El ajuste se apoya en datos: la retroalimentación «Match / Not a match» desde el Content explorer, las alertas DLP y Defender mejora los SIT y los clasificadores; la **analítica DLP** (vista previa, opcional) propone directivas nuevas y mejoras de precisión a partir de 30 días de datos; y el **diagnóstico guiado**, disponible en general desde octubre de 2026, explica el orden de evaluación, las condiciones coincidentes y las acciones de una directiva. La [Guía de ajuste de directivas](00_Programa.md#ajuste-directivas) resume los patrones más frecuentes; EDM, huellas y OCR a escala se profundizan en [A3](03_Nivel_3_Avanzado.md#a3).

**Por qué importa**

Cada falso positivo cuesta dos veces: el tiempo del analista que lo descarta y la paciencia de la persona bloqueada sin razón. Bajar la tasa de falsos positivos permite pasar de auditoría a bloqueo con respaldo del negocio, reduce el volumen de alertas que llega al SOC y libera tiempo para investigar lo que importa. Es la palanca más directa sobre la credibilidad del programa.

**Qué vas a lograr**

- Diagnosticar la causa de un falso positivo con el diagnóstico guiado y el panel de simulación.
- Ajustar un SIT integrado: nivel de confianza, proximidad, evidencia de soporte y exclusiones.
- Usar el conteo de instancias y las excepciones para separar reglas de sensibilización y de bloqueo.
- Dar retroalimentación sobre coincidencias y medir su efecto en una línea base.
- Evaluar las recomendaciones de la analítica DLP sin activarlas a ciegas.

> **Consejo Ninja.** El [modelo para reducir falsos positivos](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives) (abril de 2026) propone cuatro pasos —SIT por patrones, EDM, clasificadores entrenables y huellas digitales—; el [paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1) reúne las buenas prácticas de SIT: clonar el integrado en lugar de editarlo, elegir el elemento primario correcto, proximidad de 300 caracteres, niveles de confianza y exclusiones. El mapeo de confianza es baja ≤65, media 75 y alta 85 ([definiciones de SIT](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions)).

> **Atención.** La clasificación bajo demanda **no es una simulación**: puede disparar acciones de directivas activas sobre el contenido que reclasifica ([paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1)). Revisa qué directivas están activas antes de ejecutarla en producción.

> **Novedad.** El diagnóstico guiado de DLP (orden de evaluación, condiciones coincidentes y acciones) entró en vista previa en septiembre de 2026 y está disponible en general desde octubre; sus recomendaciones de Security Copilot requieren E5 y un licenciamiento de Copilot elegible ([MC1293479](https://mc.merill.net/message/MC1293479)). En julio de 2026 llegó, en vista previa, la condición DocumentScanFailures para detectar fallas de clasificación en Exchange por tiempos de espera o limitación ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** La [analítica DLP](https://learn.microsoft.com/en-us/purview/dlp-analytics-get-started) (vista previa, opcional, solo para Global Administrator o Compliance Administrator) se actualiza cada semana y entrega sus primeras recomendaciones a los 7 días sobre 30 días de datos; las directivas que crea se llaman «RiskSpotlighting-AAAA-MM-DD» y se versionan con el sufijo `_copy` para poder revertir. La retroalimentación «Match / Not a match» no está disponible para EDM ni para entidades con nombre ([precisión de clasificadores](https://learn.microsoft.com/en-us/purview/data-classification-increase-accuracy)).

**¿Tienes poco tiempo?**

- [Reduce false positives by using SITs and advanced classifiers](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives) · Documentación
- [Step 1: Configure pattern-based sensitive data detection](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1) · Documentación
- [Increase classifier accuracy](https://learn.microsoft.com/en-us/purview/data-classification-increase-accuracy) · Documentación

### Documentación, cursos y credenciales

- [Increase classifier accuracy](https://learn.microsoft.com/en-us/purview/data-classification-increase-accuracy) · Documentación · Oficial · Microsoft Learn. Cómo revisar coincidencias (resumen contextual) y dar retroalimentación Match/Not a match en Content explorer, alertas DLP y Defender para ajustar SIT y clasificadores entrenables.
- [Learn about sensitive information types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about) · Documentación · Oficial · Microsoft Learn. Fundamentos de los SIT: integrados, entidades con nombre, personalizados y EDM; elemento primario, de soporte, nivel de confianza y proximidad, y cómo probarlos y dar retroalimentación.
- [Reduce false positives by using SITs and advanced classifiers](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives) · Documentación · Oficial · Microsoft Learn (Deployment models) · 3 abr 2026. Modelo de despliegue oficial en 4 pasos para bajar falsos positivos: SIT por patrones, EDM, clasificadores entrenables y fingerprinting, con estrategias por escenario y optimización de reglas DLP.
- [Step 1: Configure pattern-based sensitive data detection](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1) · Documentación · Oficial · Microsoft Learn (Deployment models) · 3 abr 2026. Buenas prácticas para SIT: clonar/editar integrados, elegir el elemento primario correcto, proximidad de 300 caracteres, niveles de confianza, exclusiones y retroalimentación Match/Not a match.
- [Get started with data loss prevention analytics](https://learn.microsoft.com/en-us/purview/dlp-analytics-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 26 jun 2026. Analítica DLP (opt-in): tarjeta Risk Spotlighting, recomendaciones de nuevas directivas con un clic y mejora de precisión de directivas existentes basadas en 30 días de datos. *Nota:* Refresco semanal; 7 días para primeras recomendaciones; crea directivas "RiskSpotlighting-AAAA-MM-DD" y versiona con sufijo _copy (rollback). Solo Global admin o Compliance admin

### Comunidad: blogs, libros, newsletters y eventos

- [Common mistakes you may be making with Data Loss Prevention](https://www.welkasworld.com/post/common-mistakes-you-may-be-making-with-data-loss-prevention) · Blog · MVP · Ewelina Paczkowska · Welka's World. Artículo de una MVP de Security sobre errores frecuentes en DLP: falta de planificación, clasificación deficiente, fatiga de alertas y directivas poco amigables para el usuario.

**Manos a la obra**

1. `Laboratorio` Clona un SIT integrado (por ejemplo, tarjeta de crédito o un identificador de tu país), cambia la proximidad y el nivel de confianza, agrega palabras clave en español y una exclusión, y pruébalo con un archivo que coincide y otro que no ([probar un SIT](https://learn.microsoft.com/en-us/purview/sit-test-a-sit), [paso 1](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-reduce-false-positives-step1)). Evidencia: resultados de la prueba antes y después del ajuste.
2. `Laboratorio` En la copia v2 de tu directiva de [I2](01_Nivel_1_Inicial.md#i2), separa la regla en dos por conteo de instancias (pocas instancias: sugerencia y auditoría; muchas: bloqueo con invalidación) y compárala en simulación con la v1 durante una semana ([diseño de directivas](https://learn.microsoft.com/en-us/purview/dlp-policy-design)). Evidencia: tabla de coincidencias por regla y versión.
3. `Laboratorio` Da retroalimentación «Match / Not a match» sobre diez coincidencias del Content explorer o de las alertas y documenta qué SIT o clasificador mejorarías ([precisión de clasificadores](https://learn.microsoft.com/en-us/purview/data-classification-increase-accuracy)). Evidencia: registro de las diez revisiones con su decisión.
4. `Laboratorio` Usa el diagnóstico guiado sobre un elemento de prueba que no coincidió como esperabas y documenta el orden de evaluación, las condiciones y la acción resultante ([MC1293479](https://mc.merill.net/message/MC1293479)). Evidencia: informe del diagnóstico con tu conclusión.
5. `Laboratorio` Calcula la línea base de falsos positivos: de 50 coincidencias revisadas de tus directivas en simulación, ¿cuántas son falsos positivos en cada regla? Registra el resultado con la palanca que aplicarías según la [Guía de ajuste de directivas](00_Programa.md#ajuste-directivas). Evidencia: tasa por regla y acción propuesta.
6. `Laboratorio parcial` Activa la [analítica DLP](https://learn.microsoft.com/en-us/purview/dlp-analytics-get-started) el día 0 y revisa la tarjeta Risk Spotlighting y las recomendaciones a partir del día 7. Limitación: necesita de 7 a 30 días de actividad real y en una prueba el volumen es bajo; en producción, acepta las recomendaciones solo como copias en simulación. Evidencia: captura de las recomendaciones y decisión sobre cada una.
7. `Solo producción` Revisa con un dueño de datos las 20 coincidencias más frecuentes de una directiva productiva y ajústala en una copia v2. Cómo hacerlo seguro: rol de solo lectura para revisar el contenido, ninguna clasificación bajo demanda sobre sitios con directivas activas, cambios solo en la copia v2 en simulación y conmutación con aprobación del dueño del proceso.

**¿Quieres profundizar?**

- [Common mistakes you may be making with Data Loss Prevention](https://www.welkasworld.com/post/common-mistakes-you-may-be-making-with-data-loss-prevention) · Blog

<a id="m2"></a>

## M2 · Alertas, investigación e incidentes de DLP

*L300 · ~6 h · Origen: Ruta Ninja de Learn, módulo 3 (investigación con Security Copilot), y módulo de alertas de la ruta SC-401*

Una alerta DLP recorre un ciclo de seis pasos: se dispara, notifica, se tría, se investiga, se remedia y alimenta el ajuste. Purview y Defender XDR se reparten el trabajo: Microsoft recomienda crear directivas en Purview e investigar en Defender, donde la alerta se correlaciona con identidad, correo y endpoint. Los plazos importan: las alertas se conservan seis meses en el portal de Defender y 30 días en el panel de alertas DLP; tras un cambio de directiva pueden tardar hasta tres horas en generarse; y el explorador de actividad muestra 30 días, con 60 a 90 minutos de demora en los servicios principales.

También importa la licencia: con E5 las alertas se agregan cada minuto y puedes crear alertas agregadas por umbral; con E3, la agregación es de 15 minutos. Para incidentes de alto impacto, **Data Security Investigations** (pago por uso) busca y analiza con IA el contenido afectado y, desde junio de 2026, puede usar en vista previa la evidencia de Endpoint DLP. Cómo llegan hoy estas señales al SOC cambió en octubre de 2026: lo verás en [A2](03_Nivel_3_Avanzado.md#a2).

**Por qué importa**

Sin un proceso de triage, las alertas DLP se acumulan sin dueño y el riesgo real queda escondido en el ruido. Un runbook acordado entre el equipo DLP, el SOC y los dueños de datos define severidades, tiempos de respuesta y quién decide la remediación; eso reduce el tiempo de contención y deja evidencia para auditoría y para cualquier proceso que luego gestionen RR. HH. y Legal.

**Qué vas a lograr**

- Describir el ciclo de vida de una alerta DLP y las herramientas de cada fase.
- Configurar alertas por evento y por umbral según la licencia disponible.
- Investigar una coincidencia con el panel de alertas DLP y el explorador de actividad.
- Configurar la recolección de evidencia de endpoints con acceso compartimentado.
- Escalar un incidente de alto impacto a Data Security Investigations considerando su costo.

> **Atención.** Conservación: seis meses en el portal de Defender y 30 días en el panel de alertas DLP de Purview; los administradores acotados por unidad administrativa solo ven sus alertas ([Learn about DLP](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)). La página del panel, en cambio, indica que la retención de auditoría controla cuánto tiempo se ve una alerta ([panel de alertas](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started)). Y desde octubre de 2026 la mayoría de las señales DLP llegan a Defender como *behaviors*, no como alertas: lo verás en [A2](03_Nivel_3_Avanzado.md#a2).

> **Consejo Ninja.** Licencias de alertas: la agregación es de 1 minuto con E5 y de 15 con E3; las alertas agregadas por umbral requieren E5/A5/G5 o complementos como Purview Suite; y tras un cambio de directiva las alertas pueden tardar hasta 3 horas ([alertas DLP](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)). La pestaña «User activity summary» (120 días) del panel requiere compartir datos de Insider Risk.

> **Atención.** El explorador de actividad no es tiempo real: muestra 30 días con una demora de 60 a 90 minutos en los servicios principales y, para endpoints, solo la regla más restrictiva ([explorador de actividad](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)). En la red, una solicitud tarda hasta 30 minutos en aparecer ([red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)) y, en Copilot, los cambios de directiva tardan hasta 4 horas.

> **Novedad.** Data Security Investigations se factura por pago por uso (almacenamiento y capacidad de IA) y, desde junio de 2026, puede usar en vista previa la evidencia de Endpoint DLP como fuente ([primeros pasos](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started), [flujo de trabajo](https://learn.microsoft.com/en-us/purview/data-security-investigations-workflow)). La recolección de evidencia copia los archivos coincidentes a Azure Storage y es requisito para que el agente de triage evalúe alertas de endpoint ([evidencia](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started)). El uso de DSI en investigaciones se profundiza en el programa de eDiscovery y Audit (A4).

**¿Tienes poco tiempo?**

- [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) · Documentación
- [Get started with data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started) · Documentación
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Documentación
- [Investigate and Respond to Microsoft Purview Data Loss Prevention Alerts](https://learn.microsoft.com/en-us/training/modules/purview-data-loss-prevention-alerts/) · Curso

### Documentación, cursos y credenciales

- [Get started with data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started) · Documentación · Oficial · Microsoft Learn. Tipos de alertas DLP (evento único vs. agregadas), requisitos de licencia y roles del panel de alertas, y recomendación de usar Defender XDR para investigar y Purview para crear directivas.
- [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) · Documentación · Oficial · Microsoft Learn. Describe el ciclo de vida de una alerta DLP en seis pasos (disparar, notificar, triar, investigar, remediar, ajustar) y las herramientas de cada fase.
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Documentación · Oficial · Microsoft Learn. Activity explorer muestra hasta 30 días de actividades sobre contenido etiquetado y coincidencias DLP (incluye endpoint, red y navegador) con ~50 filtros y conjuntos de filtros predefinidos.
- [Investigate and Respond to Microsoft Purview Data Loss Prevention Alerts](https://learn.microsoft.com/en-us/training/modules/purview-data-loss-prevention-alerts/) · Curso · Oficial · Microsoft Learn. Módulo de Learn (11 unidades) sobre investigar y responder alertas DLP en Purview y Defender XDR, con Security Copilot/agentes y un ejercicio práctico de incidente.
- [Get started with the Data Loss Prevention Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) · Documentación · Oficial · Microsoft Learn. Uso del panel de alertas DLP: roles requeridos, cargas cubiertas (incluye Instances, repositorios locales y Fabric/Power BI), vista estándar, vista del agente de triaje (preview) y resumen con Security Copilot.
- [Learn about the Data Security Investigations workflow](https://learn.microsoft.com/en-us/purview/data-security-investigations-workflow) · Documentación · Oficial · Microsoft Learn. Flujo de Data Security Investigations para escalar incidentes de Defender XDR, casos de IRM o hallazgos de DSPM, buscar contenido afectado (incluida evidencia de Endpoint DLP) y analizarlo con IA.
- [Get started with Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started) · Documentación · Oficial · Microsoft Learn. Pasos de configuración de Data Security Investigations: aceptación de términos, permisos, facturación por volumen de datos y capacidad de IA, creación de investigaciones y mitigación.

**Manos a la obra**

1. `Laboratorio` Crea una directiva activa **sin bloqueo** (solo auditoría y alerta a un buzón del equipo) para el grupo de personas de prueba, porque las alertas de simulación no llegan al panel; genera dos coincidencias y tría la alerta en el [panel de alertas DLP](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started). Evidencia: alerta con estado, severidad y comentario de cierre.
2. `Laboratorio` Configura una alerta agregada por umbral (por ejemplo, cinco coincidencias en 60 minutos para la misma persona) y otra por evento único, y compara su volumen y su utilidad ([alertas DLP](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)). Evidencia: tabla con ambas configuraciones y las alertas generadas.
3. `Laboratorio` Investiga la coincidencia en el [explorador de actividad](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer): filtra por directiva, persona y actividad, guarda un conjunto de filtros y exporta el resultado. Evidencia: conjunto de filtros guardado y archivo exportado.
4. `Laboratorio` Configura la recolección de evidencia de endpoints en una cuenta de almacenamiento dedicada al laboratorio, con roles separados para ver y para descargar, y verifica que la copia del archivo de la VM llega al contenedor ([evidencia](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started)). Evidencia: archivo en el contenedor y lista de quién puede descargarlo.
5. `Laboratorio` Escribe el runbook de triage DLP con el SOC: severidades, criterios de escalamiento a RR. HH. y Legal, tiempos de respuesta y acciones de remediación por ubicación, siguiendo el ciclo de seis pasos de la [investigación de alertas](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn). Evidencia: runbook de dos páginas.
6. `Laboratorio` Completa el módulo de Learn [Investigate and Respond to Microsoft Purview Data Loss Prevention Alerts](https://learn.microsoft.com/en-us/training/modules/purview-data-loss-prevention-alerts/) y su ejercicio de incidente. Evidencia: módulo completado.
7. `Solo producción` Escala un incidente DLP de alto impacto a Data Security Investigations. Cómo hacerlo seguro: aprobación del dueño del presupuesto y de Legal, estimación previa del costo de almacenamiento y de IA, alcance limitado a las personas y fechas del incidente, roles de investigación temporales con PIM y eliminación de la investigación al cerrar; ten presente que detener la facturación elimina todas las investigaciones ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).

<a id="m3"></a>

## M3 · DLP para Copilot, IA generativa y la red

*L300 · ~8 h · Origen: Nuevo en esta edición*

La IA generativa abrió dos caminos nuevos para los datos: lo que las personas escriben, pegan o suben a una IA, y lo que la IA lee para responder. La ubicación **Microsoft 365 Copilot y Copilot Chat** —que desde octubre de 2026 también cubre Cowork— permite impedir que Copilot procese archivos y correos con ciertas etiquetas, bloquear prompts que contienen SIT, impedir búsquedas web cuando el prompt es sensible y, en vista previa, excluir el correo externo del grounding. Tiene reglas propias: solo plantilla personalizada, no se combina con otras ubicaciones, no mezcla SIT y etiquetas en una misma regla y los cambios tardan hasta cuatro horas.

Fuera de Microsoft 365, la protección llega por capas: Endpoint DLP y Edge for Business para las apps de IA de consumo, y la **seguridad de datos de red**, que inspecciona en línea el tráfico hacia apps en la nube e IA mediante Global Secure Access (GA desde septiembre de 2026) o socios SASE del Security Store. Para los agentes, Purview aplica DLP a los de Copilot Studio, Foundry y Agent 365, y la API processContent lleva las directivas a apps propias ([A1](03_Nivel_3_Avanzado.md#a1)).

Cada capa tiene su licencia, y la de la red presenta una contradicción oficial que debes conocer antes de presupuestar. La postura de IA y las directivas de un clic se profundizan en el programa de DSPM (módulos M1 a M3) y las etiquetas para Copilot, en el de Information Protection (A1).

**Por qué importa**

Copilot y los agentes amplifican la sobreexposición existente: si un archivo confidencial está mal compartido, la IA lo encuentra. A la vez, pegar información en chatbots de consumo es hoy uno de los caminos de fuga más frecuentes. Estas directivas permiten habilitar la IA con control, demostrar ante la dirección y los reguladores que los datos sensibles no salen hacia modelos no aprobados y evitar prohibiciones generales que frenan la productividad.

**Qué vas a lograr**

- Configurar una directiva para la ubicación Microsoft 365 Copilot y Copilot Chat respetando sus restricciones.
- Distinguir qué controles de Copilot incluye cada licencia y cuáles siguen en vista previa.
- Diseñar la protección por capas frente a la IA de terceros: endpoint, navegador y red.
- Comparar Global Secure Access y los socios SASE en licencias, acciones, límites y privacidad.
- Identificar qué agentes admiten DLP y cuándo se requiere pago por uso, E7 o Agent 365.

> **Atención.** **Contradicción de estado.** El blog oficial del 21 de abril de 2026 declara en disponibilidad general la DLP de prompts con SIT para Microsoft 365 Copilot y Copilot Chat ([blog](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497)), pero la página de Learn del 27 de octubre de 2026 la describe como vista previa en despliegue ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)), y la página general de DLP aún rotula toda la ubicación como vista previa. La restricción de búsqueda web se presentó como vista previa en abril, un MVP citó una GA prevista para junio ([Office 365 for IT Pros](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/)) y Learn ya no la rotula. Trátalas como vista previa hasta confirmarlo después de Ignite.

> **Atención.** **Contradicción de licencia en la red.** La [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) lista la DLP de red como pago por uso, mientras que la [página de seguridad de datos de red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) (16 de septiembre de 2026) indica que con Global Secure Access se requiere Microsoft 365 E7, o Purview E5 más Entra Internet Access, **sin** pago por uso, y que con un SASE o navegador seguro de terceros se requiere Purview E5 más pago por uso por solicitud. Solo admite auditar o bloquear, no aplica a invitados B2B y tiene límites en línea de 4 MB para texto y 3 MB para archivos. Valida con tu equipo de cuenta antes de presupuestar.

> **Novedad.** Línea de tiempo de Copilot: control por etiquetas desde noviembre de 2024; cobertura de archivos etiquetados en cualquier almacenamiento entre marzo y abril de 2026 ([MC1234661](https://office365itpros.com/2026/02/24/dlp-policy-for-copilot-storage/)); Cowork cubierto sin configuración adicional, con GA mundial entre mediados y fines de octubre de 2026 ([MC1477182](https://mc.merill.net/message/MC1477182)); y exclusión del correo externo del grounding en vista previa, con GA prevista para fines de enero de 2027 ([MC1301714](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/)). La directiva predeterminada «Protect sensitive M365 Copilot interactions» arranca en simulación ([directiva predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)).

> **Consejo Ninja.** Licencias de Copilot: impedir que Copilot procese archivos y correos etiquetados requiere E5/A5, Purview Suite, E5 IP&G u Office 365 E5; la DLP de prompts está disponible para todos los usuarios de Microsoft 365 Copilot y Copilot Chat. En agentes, los de Copilot Studio y Foundry admiten DLP, los de ChatGPT Enterprise solo clasificación e Insider Risk y los de Claude Enterprise ninguna protección ([agentes](https://learn.microsoft.com/en-us/purview/ai-agents)); Foundry y las apps de IA conectadas a Entra se cubren con Microsoft 365 E7 y Agent 365, y las instancias de Agent 365 entran en las directivas como si fueran usuarios ([Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365)).

**¿Tienes poco tiempo?**

- [Microsoft Purview DLP for Microsoft 365 Copilot and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación
- [Learn about Microsoft Purview Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Documentación
- [Use Microsoft Purview to manage data security & compliance for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents) · Documentación
- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog

### Documentación, cursos y credenciales

- [Microsoft Purview DLP for Microsoft 365 Copilot and Cowork](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 oct 2026. Ubicación "Microsoft 365 Copilot y Copilot Chat" (ahora también Cowork): bloquea búsqueda web con prompts sensibles, bloquea prompts con SIT, impide procesar archivos/correos etiquetados y, en preview, excluye correo externo del grounding.
- [Learn about Microsoft Purview Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 sep 2026. Seguridad de datos de red: integra Purview con Entra Global Secure Access y con SASE/navegadores seguros de terceros (Security Store) para descubrir, alertar y bloquear contenido sensible enviado a apps no gestionadas e IA.
- [Microsoft Purview data security and compliance protections for generative AI apps](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview) · Documentación · Oficial · Microsoft Learn. Panorama oficial de cómo Purview (DSPM, etiquetas, DLP, IRM, cumplimiento) protege Copilot, agentes y apps de IA empresariales y de terceros, con la categorización de apps soportadas.
- [Secure and govern Microsoft 365 Copilot agents](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-deployment) · Documentación · Oficial · Microsoft Learn · 3 abr 2026. Modelo de despliegue oficial en 4 pasos para asegurar agentes de Microsoft 365 Copilot: descubrir riesgos, proteger datos de grounding (incluye DLP para Copilot), proteger interacciones y gobernarlas.
- [MC1477182 - Microsoft Purview: Data Loss Prevention for Microsoft Cowork](https://mc.merill.net/message/MC1477182) · Documentación · Oficial · Nuevo · Microsoft 365 Message Center Archive (mc.merill.net) · 22 sep 2026. Aviso del Centro de mensajes: las directivas DLP para Microsoft Copilot se extienden automáticamente a Microsoft Cowork (grounding por etiquetas, bloqueo de prompts y de búsqueda web por SIT) sin configuración adicional.
- [Use Microsoft Purview to manage data security & compliance for AI agents](https://learn.microsoft.com/en-us/purview/ai-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 may 2026. Matriz de capacidades de Purview por tipo de agente (Microsoft 365 Copilot, Security Copilot, Fabric, Copilot Studio, Foundry, Entra-registered, ChatGPT/Claude Enterprise), indicando dónde aplica DLP.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview soportadas para agentes creados en Copilot Studio (DSPM, auditoría, clasificación, etiquetas, DLP, IRM, eDiscovery, retención) y pasos recomendados.
- [Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365) · Documentación · Oficial · Microsoft Learn. Capacidades de Purview para instancias de agentes de Agent 365: auditoría y clasificación automáticas, y DLP/IRM incluyendo la instancia del agente en las directivas como si fuera un usuario.

### Anuncios y blogs oficiales

- [Close the gaps: layered data protection with Microsoft Purview across endpoint, browser, and network](https://365community.online/close-the-gaps-layered-data-protection-with-microsoft-purview-across-endpoint-browser-and-network) · Blog oficial · Empleado de Microsoft · Nuevo · Nick (Nick-MSFT) · 365 Community Online (réplica de Microsoft Purview Blog) · 31 ago 2026. Post del blog de Purview (replicado) con un kit de diapositivas sobre protección en tres capas —endpoint, navegador y red— con escenarios, flujos de despliegue y arquitecturas de referencia.
- [Safeguarding Sensitive Data in Microsoft 365 Copilot Interactions: DLP for Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft-security-blog/safeguarding-sensitive-data-in-microsoft-365-copilot-interactions-dlp-for-micros/4512497) · Blog oficial · Empleado de Microsoft · Aaron Thorp · Microsoft Security Community Blog (Tech Community) · 21 abr 2026. Explica la GA de DLP para prompts de Microsoft 365 Copilot y Copilot Chat (anunciada en Ignite 2025), incluida para todos sus usuarios, y su relación con los controles por etiquetas y búsqueda web.
- [Building layered protection: New Microsoft Purview data security controls for the browser & network](https://techcommunity.microsoft.com/blog/microsoft-security-blog/building-layered-protection-new-microsoft-purview-data-security-controls-for-the/4395071) · Blog oficial · Empleado de Microsoft · Legado aún útil · Vivian Ma · Microsoft Security Community Blog (Tech Community) · 24 mar 2025. Anuncio de la estrategia de protección por capas: descubrimiento en línea vía SASE (Netskope, iboss, Palo Alto Prisma Access), DLP en línea en Edge for Business y controles para dispositivos no gestionados. *Nota:* Estados del anuncio (preview mayo-2025) superados: integración GSA GA sep-2026; consultar la doc de network data security para la lista vigente de socios

### Comunidad: blogs, libros, newsletters y eventos

- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog · MVP · Nuevo · Nikki Chapple · nikkichapple.com · 16 may 2026. Guía práctica de una MVP con seis controles DLP para Copilot e IA generativa (prompts, búsqueda web, contenido etiquetado, pegado/subida a sitios GenAI, archivos etiquetados y protección en línea en Edge).
- [DLP Policy for Copilot Can Block Web Searches](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 16 abr 2026. Análisis de la acción DLP que impide a Copilot realizar búsquedas web cuando el prompt contiene SIT, y de la directiva predeterminada "Protect sensitive M365 Copilot interactions".
- [DLP Policy for Copilot Extends to All Storage Locations](https://office365itpros.com/2026/02/24/dlp-policy-for-copilot-storage/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 24 feb 2026. Explica cómo la directiva DLP para Copilot pasó a cubrir archivos Office etiquetados en cualquier almacenamiento (local u otras nubes) gracias al Augmentation Loop de Office.
- [New DLP Rule to Block Copilot from Processing External Email](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/) · Blog · MVP · Vista previa · Nuevo · Tony Redmond · Office 365 for IT Pros · 29 jul 2026. Prueba práctica del control (preview) que excluye correos de dominios externos del grounding de Copilot para reducir inyección de prompts, con su efecto retroactivo sobre mensajes existentes. *Nota:* Según MC1301714, GA prevista a fines de enero de 2027; depende de la lista de dominios aceptados del tenant

**Manos a la obra**

1. `Laboratorio parcial` Crea en simulación una directiva en la ubicación Microsoft 365 Copilot y Copilot Chat que bloquee los prompts con un SIT (por ejemplo, tarjeta de crédito) y la búsqueda web cuando el prompt sea sensible, y pruébala con una persona de prueba en Copilot Chat ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). Limitación: los cambios tardan hasta 4 horas y la DLP de prompts no inspecciona los archivos subidos al prompt. Evidencia: prompt bloqueado o coincidencia en el panel de simulación.
2. `Laboratorio parcial` Crea una segunda directiva, separada, que impida a Copilot procesar archivos y correos con una etiqueta de prueba («Confidencial – PRUEBA»), sin mezclar SIT y etiquetas en la misma regla y con una URL de cumplimiento propia en la sugerencia. Limitación: ver el efecto exige licencias de Microsoft 365 Copilot, que la prueba E5 no trae (el sandbox de desarrollador permite comprarlas). Evidencia: configuración de la regla y, si tienes licencia, una respuesta de Copilot que omite el archivo etiquetado.
3. `Laboratorio parcial` Revisa en simulación la directiva predeterminada «Protect sensitive M365 Copilot interactions» y documenta qué cubre, a quién y qué cambiarías antes de activarla ([directiva predeterminada](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy)). Limitación: en el laboratorio solo ves configuración y simulación; el efecto real requiere licencias de Copilot. Evidencia: ficha de la directiva con tus cambios propuestos.
4. `Laboratorio` Diseña la protección por capas frente a la IA de terceros con el modelo de cuatro rutas de datos hacia la IA (escribir, pegar, adjuntar y usar dentro del documento) de la [guía de Nikki Chapple](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) y el kit de [capas de endpoint, navegador y red](https://365community.online/close-the-gaps-layered-data-protection-with-microsoft-purview-across-endpoint-browser-and-network): para cada ruta, qué control usarías (Endpoint DLP, Edge for Business, red o Copilot), con qué licencia y en qué estado. Evidencia: matriz de capas con huecos y costos.
5. `Laboratorio` Clasifica los agentes de tu organización (Copilot Studio, Foundry, Channel Agent de Teams, Agent 365, ChatGPT Enterprise y Claude Enterprise) según la protección de Purview que admiten y la licencia que requieren, con la [matriz de agentes](https://learn.microsoft.com/en-us/purview/ai-agents), la guía de [Copilot Studio](https://learn.microsoft.com/en-us/purview/ai-copilot-studio) y el [modelo para agentes de Copilot](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-sc-agents-deployment). Evidencia: inventario de agentes con su cobertura y sus brechas.
6. `Solo producción` Seguridad de datos de red con Global Secure Access: en un piloto, habilita el [reenvío del tráfico](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) de Internet para un grupo pequeño y crea una directiva de red solo de auditoría para apps de IA no gestionadas ([red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn), [escenario de IA](https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security)). Requiere Microsoft 365 E7, o Purview E5 más Entra Internet Access. Cómo hacerlo seguro: Acceso condicional en solo informe, grupo piloto informado, sin invitados B2B, espera de hasta 24 horas para la distribución, revisión de eventos en el explorador de actividad y reversión del perfil de reenvío.
7. `Solo producción` SASE o navegador seguro de terceros del Security Store: requiere la licencia del socio y pago por uso por solicitud. Cómo hacerlo seguro: integración con un grupo piloto, solo auditoría, revisión de privacidad de lo que el socio almacena (parte de la configuración, incluidos identificadores de usuario), presupuesto con alertas y plan de reversión deshabilitando la directiva ([red](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn)).

**¿Quieres profundizar?**

- [New DLP Rule to Block Copilot from Processing External Email](https://office365itpros.com/2026/07/29/dlp-external-email-copilot/) · Blog
- [DLP Policy for Copilot Can Block Web Searches](https://office365itpros.com/2026/04/16/dlp-policy-for-copilot-web/) · Blog
- [DLP Policy for Copilot Extends to All Storage Locations](https://office365itpros.com/2026/02/24/dlp-policy-for-copilot-storage/) · Blog

<a id="m4"></a>

## M4 · Protección adaptativa con Insider Risk

*L300 · ~5 h · Origen: Nuevo en esta edición (la configuración de Insider Risk se profundiza en su propio programa)*

La **protección adaptativa** une dos mundos: Insider Risk Management calcula un nivel de riesgo para cada persona (Elevated, Moderate o Minor) y DLP aplica controles distintos según ese nivel, sin listas manuales. La integración con DLP está disponible sin rótulo de vista previa; las de Data Lifecycle Management y Acceso condicional siguen en vista previa. La DLP adaptativa solo actúa en Exchange, Teams y dispositivos, y no admite sugerencias de directiva.

La configuración rápida crea, en hasta 72 horas, una directiva de Insider Risk, los niveles de riesgo, una directiva de Acceso condicional en modo solo informe, una de retención y dos directivas DLP en modo de prueba: bloqueo para Elevated y auditoría para Moderate y Minor. Por defecto, el nivel dura siete días y mira siete días de actividad pasada (ambos configurables de 5 a 30). La guía actual separa los niveles de riesgo de personas y de agentes.

La configuración de Insider Risk, sus indicadores y su gobierno se profundizan en el programa de Insider Risk Management (módulo M3); aquí el foco es la parte de DLP y su impacto en la operación y la privacidad.

**Por qué importa**

Los controles estáticos obligan a elegir entre proteger poco a todos o molestar a todos. Con niveles de riesgo, el bloqueo se concentra en quien muestra señales de exfiltración —por ejemplo, alguien que renunció y descarga en masa— mientras el resto trabaja con menos fricción. Es una forma medible de reducir riesgo sin multiplicar quejas, siempre con la supervisión de RR. HH., Legal y privacidad.

**Qué vas a lograr**

- Explicar cómo los niveles de riesgo de Insider Risk se convierten en condiciones de DLP.
- Ejecutar la configuración rápida y revisar las directivas que crea en modo de prueba.
- Ajustar la duración y la ventana de detección de los niveles de riesgo a un escenario real.
- Evaluar el impacto en privacidad: seudonimización en Insider Risk frente a nombres reales en DLP.

> **Atención.** La DLP adaptativa solo actúa en Exchange, Teams y dispositivos, aunque agregues otras ubicaciones, y no admite sugerencias de directiva ([Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection), [guía de configuración](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide)). La integración con DLP no lleva rótulo de vista previa; las de Data Lifecycle Management y Acceso condicional sí (página del 26 de junio de 2026).

> **Atención.** Privacidad: los nombres se seudonimizan en Insider Risk por defecto, pero aparecen reales en las alertas DLP y en el explorador de actividad ([Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Inclúyelo en la evaluación de impacto y acuerda con RR. HH., Legal y privacidad quién puede ver esas alertas. Insider Risk no está disponible en las nubes de gobierno de EE. UU.

> **Consejo Ninja.** La configuración rápida tarda hasta 72 horas (la personalizada, hasta 36; desactivarla, hasta 6) y crea dos directivas DLP en modo de prueba —una para Teams y Exchange y otra para dispositivos— con bloqueo para Elevated y auditoría para Moderate y Minor ([Adaptive Protection en DLP](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn)). Para Elevated también crea una directiva de retención que preserva 120 días lo que se elimine.

> **Novedad.** La guía actual separa los niveles de riesgo para personas y para agentes ([guía de configuración](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide)). La configuración de Insider Risk, sus indicadores y el seguimiento de agentes riesgosos se profundizan en el programa de Insider Risk Management (M3 y A1).

**¿Tienes poco tiempo?**

- [Help dynamically mitigate risks with Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Documentación
- [Learn about Adaptive Protection in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn) · Documentación
- [Implement Adaptive Protection in Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/m365-compliance-irm-adaptive-protection/) · Curso

### Documentación, cursos y credenciales

- [Help dynamically mitigate risks with Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Explica Adaptive Protection: niveles de riesgo interno (Elevated, Moderate, Minor) calculados por IRM que aplican dinámicamente controles de DLP, gestión del ciclo de vida de datos (preview) y Acceso condicional (preview).
- [Adaptive Protection configuration guide](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide) · Documentación · Oficial · Microsoft Learn. Configuración recomendada de niveles de riesgo y de directivas DLP adaptativas para Teams/Exchange y endpoints, ahora con niveles separados para usuarios y agentes.
- [Learn about Adaptive Protection in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn) · Documentación · Oficial · Microsoft Learn. Cómo aparece la condición "Insider risk level for Adaptive Protection is" en reglas DLP de Exchange, Teams y Dispositivos, y qué directivas crea la configuración rápida.
- [Implement Adaptive Protection in Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/m365-compliance-irm-adaptive-protection/) · Curso · Oficial · Microsoft Learn. Módulo de Learn (~52 min) para configurar Adaptive Protection: niveles de riesgo, integración con DLP y Acceso condicional, y supervisión.

**Manos a la obra**

1. `Laboratorio parcial` Activa la configuración rápida de Adaptive Protection en el tenant de prueba y, pasadas hasta 72 horas, revisa las dos directivas DLP en modo de prueba, la directiva de Acceso condicional en solo informe y la de retención ([Adaptive Protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)). Limitación: para que aparezcan niveles de riesgo necesitas actividad simulada (descargas masivas, copias a USB o a un recurso de red) de una persona de prueba. Evidencia: captura de las directivas y del nivel asignado.
2. `Laboratorio parcial` Reproduce un escenario de salida: carga la renuncia sintética de la persona «vendedor que renuncia» con el [conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data) y, al día siguiente, descarga en masa desde SharePoint y copia a un recurso de red desde la VM; comprueba si la regla de Elevated habría bloqueado ([Adaptive Protection en DLP](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn)). Limitación: el laboratorio no reproduce semanas de comportamiento real. Evidencia: línea de tiempo de la persona con su nivel y sus coincidencias.
3. `Laboratorio` Redacta la matriz de controles por nivel de riesgo (Elevated, Moderate y Minor) para Exchange, Teams y dispositivos de tu organización, justifica la duración del nivel y la ventana de detección elegidas (de 5 a 30 días) e indica qué ve cada rol y cuándo interviene RR. HH. ([guía de configuración](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection-guide)). Evidencia: matriz de una página.
4. `Laboratorio` Completa el módulo de Learn [Implement Adaptive Protection in Insider Risk Management](https://learn.microsoft.com/en-us/training/modules/m365-compliance-irm-adaptive-protection/) y su evaluación. Evidencia: módulo completado.
5. `Solo producción` Habilita la DLP adaptativa en producción para un grupo piloto aprobado. Cómo hacerlo seguro: aprobación de Legal, privacidad, RR. HH. y, si aplica, de la representación de los trabajadores; directivas primero en simulación; seudonimización activa en Insider Risk; revisión de los niveles con RR. HH.; y monitoreo de los bloqueos por nivel durante un mes antes de ampliar.

<a id="reto-intermedio"></a>

## Reto del nivel

**De la simulación al bloqueo con evidencia.** Toma la directiva del reto inicial, mide su tasa de falsos positivos y ajústala en una copia v2 (confianza, instancias, excepciones o etiquetas); agrega una directiva para Copilot y la protección adaptativa en modo de prueba, y escribe el runbook de triage con el SOC. Entregables: tabla de precisión antes y después, directivas v2 en simulación, runbook de dos páginas y una nota con el costo de pago por uso que implicaría extender la protección al navegador y a la red.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. En los tipos de información confidencial, ¿qué valores corresponden a los niveles de confianza baja, media y alta?
   - a) ≤65, 75 y 85
   - b) 50, 70 y 90
   - c) 25, 50 y 75
   - d) 60, 80 y 100

2. ¿Qué advierte la guía oficial sobre la clasificación bajo demanda?
   - a) Solo funciona en modo de simulación
   - b) Puede disparar acciones de directivas activas sobre el contenido reclasificado
   - c) No admite SIT personalizados
   - d) Requiere pago por uso

3. ¿Qué es cierto sobre la analítica DLP (vista previa)?
   - a) Genera recomendaciones en tiempo real
   - b) Se actualiza cada semana y da sus primeras recomendaciones a los 7 días sobre 30 días de datos
   - c) Activa directivas en modo de bloqueo de forma automática
   - d) Puede activarla cualquier rol de solo lectura

4. ¿Qué estado tiene el diagnóstico guiado de DLP al corte de noviembre de 2026?
   - a) Retirado
   - b) Vista previa privada
   - c) Solo para tenants de Government
   - d) Disponible en general desde octubre de 2026; sus recomendaciones de Security Copilot requieren E5 y licencia de Copilot elegible

5. Según la página general de DLP, ¿cuánto tiempo se conservan las alertas DLP?
   - a) 30 días en Defender y 6 meses en Purview
   - b) Un año en ambos portales
   - c) 6 meses en el portal de Defender y 30 días en el panel de alertas DLP de Purview
   - d) 90 días en ambos portales

6. ¿Cuál es el intervalo de agregación de las alertas DLP con E5 frente a E3?
   - a) 1 minuto con E5 y 15 minutos con E3
   - b) 15 minutos con E5 y 1 hora con E3
   - c) 5 minutos en ambos casos
   - d) 1 hora con E5 y 24 horas con E3

7. ¿Qué es cierto sobre el explorador de actividad?
   - a) Muestra la actividad en tiempo real
   - b) Muestra 30 días, con 60 a 90 minutos de demora en los servicios principales
   - c) Conserva un año de datos
   - d) Solo muestra actividad de endpoints

8. ¿Qué afirmación sobre la ubicación Microsoft 365 Copilot y Copilot Chat es correcta?
   - a) DLP escanea los archivos subidos al prompt
   - b) Se pueden combinar SIT y etiquetas en la misma regla
   - c) Solo está en la plantilla personalizada y no se combina con otras ubicaciones
   - d) Los cambios se aplican al instante

9. Para la seguridad de datos de red con Global Secure Access, ¿qué licencia indica la página de red de Purview?
   - a) Solo pago por uso
   - b) Microsoft 365 E3
   - c) Un SASE de terceros obligatorio
   - d) Microsoft 365 E7, o Purview E5 más Entra Internet Access, sin pago por uso

10. ¿Quiénes pueden usar la DLP que bloquea prompts con SIT en Copilot?
   - a) Solo los clientes con E5
   - b) Solo los clientes con E7
   - c) Todos los usuarios de Microsoft 365 Copilot y Copilot Chat
   - d) Solo los clientes con Purview Suite

11. Según la matriz de agentes de Purview (mayo de 2026), ¿qué agentes no admiten DLP?
   - a) Los de Copilot Studio
   - b) Los de Microsoft Foundry
   - c) El Channel Agent de Teams
   - d) Los de ChatGPT Enterprise y Claude Enterprise

12. ¿Qué ubicaciones admite hoy la DLP adaptativa?
   - a) Todas las ubicaciones
   - b) Exchange, Teams y dispositivos
   - c) Solo SharePoint y OneDrive
   - d) Solo Copilot

13. ¿Qué directivas DLP crea la configuración rápida de la protección adaptativa?
   - a) Dos directivas en modo de prueba: bloqueo para Elevated y auditoría para Moderate y Minor
   - b) Una directiva en bloqueo para todos los niveles
   - c) Ninguna: solo crea una directiva de Acceso condicional en modo activo
   - d) Directivas de red para Global Secure Access

14. En la protección adaptativa, ¿dónde aparecen los nombres reales de las personas aunque Insider Risk los seudonimice?
   - a) En ningún lugar
   - b) Solo en los informes de RR. HH.
   - c) En las alertas DLP y en el explorador de actividad
   - d) Solo en Defender for Endpoint

15. ¿Qué acciones admite la seguridad de datos de red?
   - a) Solo auditar o bloquear
   - b) Cifrar y poner en cuarentena
   - c) Bloquear con invalidación y justificación
   - d) Etiquetar de forma automática

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

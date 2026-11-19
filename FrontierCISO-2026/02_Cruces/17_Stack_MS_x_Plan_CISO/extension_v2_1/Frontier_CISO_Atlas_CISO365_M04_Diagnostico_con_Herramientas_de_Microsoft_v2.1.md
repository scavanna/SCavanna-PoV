# Diagnóstico con herramientas de Microsoft

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M04 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. El diagnóstico no cambia

El diagnóstico es el del núcleo: 59 funciones calificadas con evidencia, 42 criterios Zero Trust, la pila de herramientas, la cobertura por entorno y los contratos. Esta edición agrega dos cosas: herramientas de Microsoft que aportan evidencia y un inventario de capacidades con su licencia y su despliegue.

## 2. Herramientas de evaluación

| Herramienta | Qué evalúa | Qué alimenta en el diagnóstico | Funciones | Estado | Fuente |
|---|---|---|---|---|---|
| Zero Trust Assessment | Módulo de PowerShell que compara la configuración del inquilino de Microsoft 365 y Azure con recomendaciones en siete pilares (identidad, dispositivos, red, datos, infraestructura, operaciones de seguridad e IA); genera informes locales sin remediar, exportables al Zero Trust Workshop. | Hoja Zero Trust del libro de diagnóstico: identidades, dispositivos, datos y red. | GES-M3.1 | Documentado en Microsoft Learn como proyecto comunitario mantenido por empleados de Microsoft, sin soporte oficial; sin etiqueta de disponibilidad general ni de versión preliminar. | https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview |
| Zero Trust Workshop | Herramienta interactiva de planificación del despliegue de Zero Trust por pilares, con priorización de tareas y planes de implementación; se alimenta con los resultados del Zero Trust Assessment. | Planificación del despliegue por pilar; complementa la hoja Zero Trust. | GES-M3.1 | No confirmado: solo se halló su sitio en microsoft.github.io (GitHub de Microsoft, fuera de los dominios admitidos); la URL indicada es la página de Learn que lo menciona. Sin página propia en Learn. | https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview |
| Microsoft Secure Score | Postura de seguridad de identidades, aplicaciones y dispositivos de Microsoft 365 en el portal de Defender, con acciones recomendadas puntuadas, historial y comparación con organizaciones similares (Entra ID, Defender for Endpoint, Identity, Office 365, Cloud Apps, Exchange, SharePoint, Teams, Information Protection). | Funciones de identidades, dispositivos, correo y aplicaciones. | OPE-PR-01 · OPE-PR-04 · OPE-PR-05 | Sin etiqueta de versión preliminar (disponibilidad general no declarada expresamente). | https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score |
| Identity Secure Score y recomendaciones de Microsoft Entra | Porcentaje de alineación de la configuración de identidad con las recomendaciones de Microsoft (recalculado cada 24 h) y recomendaciones diarias con planes de acción (MFA, autenticación heredada, roles con privilegios mínimos, credenciales de aplicaciones). | Funciones de identidad y de acceso privilegiado. | GES-M2.2 · OPE-PR-01 · OPE-PR-02 | Identity Secure Score sin etiqueta de versión preliminar. Recomendaciones (overview-recommendations, 2026-04-28): mezcla de recomendaciones en disponibilidad general y en versión preliminar pública. | https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score |
| Iniciativas y métricas de Microsoft Security Exposure Management | Seguimiento de la exposición por áreas mediante iniciativas con puntuación, objetivo, tendencia e historial, métricas y recomendaciones asociadas (de Secure Score o Defender for Cloud). | Inventario, exposición y supervisión del análisis de riesgo. | OPE-ID-01 · OPE-ID-02 · GOB-G5.1 | Función sin etiqueta de versión preliminar; algunas iniciativas concretas en versión preliminar pública. | https://learn.microsoft.com/en-us/security-exposure-management/initiatives |
| Puntuación de seguridad de Microsoft Defender for Cloud (secure score clásico y Cloud Secure Score) | Postura de seguridad de Azure, AWS y Google Cloud: el modelo clásico se basa en los controles de Microsoft cloud security benchmark; el Cloud Secure Score del portal de Defender pondera riesgo y criticidad de activos. | Postura de nube y paridad de control entre entornos (K123). | OPE-ID-03 · OPE-PR-09 | Sin etiqueta de versión preliminar; las recomendaciones en versión preliminar no computan. Los dos modelos no son comparables entre sí. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls |
| Cumplimiento regulatorio de Microsoft Defender for Cloud con Microsoft cloud security benchmark | Evaluación continua de recursos frente a estándares en el panel de cumplimiento regulatorio; MCSB asignado por defecto; integración de datos con Microsoft Purview Compliance Manager. | Cumplimiento continuo y línea base por entorno (K141). | GOB-G3.2 · GES-M3.2 | MCSB por defecto en disponibilidad general; MCSB v2 en versión preliminar pública. Añadir estándares adicionales requiere un plan de pago. | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance |
| Microsoft Purview Compliance Manager | Evaluaciones normativas predefinidas o personalizadas (más de 360 plantillas), acciones de mejora y puntuación de cumplimiento basada en riesgo, con alcance multinube. | Marcos, requisitos y cumplimiento. | GOB-G2.1 · GOB-G3.1 · GOB-G3.2 | Sin etiqueta de versión preliminar; las evaluaciones disponibles dependen de la licencia. | https://learn.microsoft.com/en-us/purview/compliance-manager |
| Optimización del SOC de Microsoft Sentinel (SOC optimization) | Recomendaciones recalculadas cada 24 h sobre cobertura de detección (amenazas, MITRE ATT&CK, riesgo) y valor de los datos (tablas poco usadas, plan de datos, coste de ingesta). | Calidad de la detección y gestión de la telemetría. | OPE-DE-02 · OPE-DE-05 | Sin etiqueta de versión preliminar; disponible en el portal de Defender (Sentinel deja Azure portal después de 2027-03-31). | https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access |
| Evaluaciones de riesgo de datos de Microsoft Purview Data Security Posture Management (data risk assessments) | Evaluaciones predeterminadas o personalizadas que identifican y corrigen la sobreexposición de datos sensibles, además de métricas de postura y observabilidad de aplicaciones y agentes de IA. | Descubrimiento y protección de datos; datos usados por la IA. | OPE-ID-06 · OPE-PR-06 · OPE-ID-07 | No etiquetadas como versión preliminar en la página general de DSPM; la página específica no pudo abrirse, estado detallado no confirmado. | https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about |
| Configuration analyzer de Microsoft Defender for Office 365 | Compara directivas antispam, antimalware, antiphishing, Safe Links y Safe Attachments con los perfiles Standard y Strict de las directivas preestablecidas; incluye análisis de deriva de configuración (hasta 90 días). | Protección del correo y la colaboración. | OPE-PR-05 | Sin etiqueta de versión preliminar; aplica a buzones en la nube y a Defender for Office 365 Plan 1 y Plan 2. | https://learn.microsoft.com/en-us/defender-office-365/configuration-analyzer-for-security-policies |

## 3. Cómo usarlas sin confundir puntaje con evidencia

1. **Una puntuación no es un nivel de evidencia.** Una puntuación alta indica configuración alineada con una recomendación; sostiene el nivel «Implementado» de la función. El nivel «Probado» exige una prueba.
2. **La puntuación cubre lo que el producto ve.** Lo que está fuera de la plataforma, o en un entorno sin conectar, no aparece. Por eso el diagnóstico pide la cobertura por entorno.
3. **Se anota el valor y la fecha.** La hoja «Diagnóstico con Microsoft» del libro tiene una celda para cada herramienta: es la línea base.
4. **Se repite con la misma herramienta.** La comparación entre dos mediciones vale si la herramienta y el alcance son los mismos.

## 4. Inventario de capacidades: licenciado no es desplegado

En la hoja Capacidades se registra, para cada una de las 50, si está licenciada y cuánto está desplegada: No, Piloto, Parcial, Completa. De ahí salen tres hallazgos típicos de un diagnóstico sobre esta plataforma:

| Hallazgo | Qué indica | Qué sigue |
|---|---|---|
| Capacidad licenciada y sin desplegar | Se paga por un control que no opera | Resultado clave de adopción en el ciclo 1 o 2 |
| Capacidad desplegada y sin operar | No hay tareas por cadencia ni dueño | Instalar la operación: documento M05 «Operación por cadencias: excelencia operacional» |
| Función cubierta en Azure y sin cobertura en otro entorno del alcance | La regla no es la misma en todos los entornos (K123) | Complemento o verificación: documento M03 «Cobertura multicloud: hasta dónde llega Microsoft fuera de Microsoft» |
| Dos herramientas para la misma función | Solapamiento (K122) | Decidir cuál queda, con su costo de transición |

## 5. Pasos del diagnóstico, en los primeros 60 días del ciclo 1

El diagnóstico es el primer tramo del ciclo 1. Entre los días 61 y 90 se ejecutan los primeros resultados clave, y el ciclo cierra con el informe de los 90 días.

| Días | Qué se hace | Dónde se registra |
|:--:|---|---|
| 1 a 10 | Definir los entornos en el alcance y el plan de licencias. | `Frontier_CISO_Atlas_CISO365_Edicion_Microsoft_v2.1.xlsx` · Parámetros |
| 5 a 20 | Inventariar las capacidades: licencia y despliegue. | Hoja Capacidades |
| 10 a 30 | Ejecutar las herramientas de evaluación y anotar los valores. | Hoja Diagnóstico con Microsoft |
| 11 a 40 | Calificar las funciones y los criterios Zero Trust con esa evidencia. | `Frontier_CISO_Atlas_CISO365_Diagnostico_v2.0.xlsx` |
| 30 a 50 | Probar las coberturas «No confirmado» que afecten a funciones críticas. | Hoja Capacidades, columna Nota |
| 41 a 55 | Confirmar la fuente de cada indicador elegido y tomar la línea base. | Hoja Indicadores × Microsoft |
| 51 a 60 | Leer el resumen y confirmar los resultados clave del ciclo 1. | Hojas Resumen y OKR × Microsoft |
| 1 a 60 | Marcar qué guías del repositorio están en el alcance y designar al dueño de cada producto. | Hoja Guías del repositorio |

## 6. Microsoft como proveedor

El núcleo pide gobernar cada servicio externalizado con 14 comprobaciones. Varias aplican también a un proveedor de plataforma: dueño interno designado, evidencia periódica, localización de los datos, plan de salida y uso de IA declarado. La concentración de funciones críticas en un mismo proveedor se mide con KX14 y con K27, y el límite lo fija el directorio.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

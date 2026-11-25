# Fuentes, supuestos y silencios de la edición Microsoft

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M09 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Fuentes

| Tema | Fuente | Fecha |
|---|---|---|
| Cobertura por entorno, guías de operación y herramientas de evaluación | Documentación oficial de Microsoft (Microsoft Learn y blogs oficiales): 50 capacidades, 11 guías y 11 herramientas. La fuente de cada capacidad está en el documento M03 «Cobertura multicloud: hasta dónde llega Microsoft fuera de Microsoft». | 15 de noviembre de 2026 |
| Licencias | Catálogo de seguridad de Microsoft validado frente a fuentes oficiales, de los archivos del proyecto. | 4 de noviembre de 2026 |
| Tareas por cadencia | TheNextCISO GM-24 V7.1, plano B: instancias de dominio de productividad, XDR, endpoints, identidades, datos, SIEM y nube. | 14 de noviembre de 2026 |
| Tareas por cadencia y procedimientos | 12 guías de excelencia operacional del autor, por producto: Defender for Office 365, Defender XDR, Defender for Endpoint, Intune, Defender for Identity, Entra, Purview Information Protection, Purview Data Loss Prevention, Sentinel, Defender for Cloud Apps, Purview Insider Risk Management, Purview Data Lifecycle Management y Records Management. Diez son borradores localizados en OneDrive; las de riesgo interno y de ciclo de vida de los datos son las guías 17 y 16 del repositorio. El detalle está en el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron». | Borradores: del 27 de febrero al 27 de abril de 2026; Intune, 8 de noviembre de 2026. Repositorio: 11 de noviembre de 2026 |
| Marco de excelencia operacional | Marcos de excelencia operacional para la oficina del CISO, del autor: gobernanza de las operaciones de seguridad, marco maestro y ensayo con el manifiesto de seis principios. | 28 de febrero de 2026 |
| Guías del repositorio | Repositorio del autor SCavanna-PoV (https://github.com/scavanna/SCavanna-PoV), carpeta `ExcelenciaOperacional_NinjaTraining_KPIsOKRs`: 23 guías de excelencia operacional con 833 acciones y 184 indicadores técnicos, un puente con el plan 1.0 y los 15 programas Ninja. Se leyó el paquete `Repositorio_GitHub_Pages_CISO365_ExcelenciaOperacional_Ninja_2026.zip`, de 311 archivos. El detalle está en el documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación». | Consolidado el 12 de noviembre de 2026; guías validadas el 11 de noviembre de 2026 |
| Formación | Serie Ninja Training de Seguridad Microsoft, edición 2026, del autor: 15 programas, 387 módulos y 2165 ejercicios. | 8 de noviembre de 2026 |
| Núcleo | Modelo Operativo CISO 365 versión 2.0, revisión 2: cuatro ciclos trimestrales. | 15 de noviembre de 2026 |

## 2. Supuestos

| ID | Tema | Supuesto | En qué se apoya | A qué afecta | Qué lo haría revisar |
|---|---|---|---|---|---|
| SUPM-01 | Cobertura fuera de Microsoft | La cobertura por entorno se verificó en documentación oficial de Microsoft con fecha de corte al 15 de noviembre de 2026. Donde la documentación no lo afirma con claridad, el valor es «no confirmado». | Investigación de cobertura: 50 capacidades, cinco entornos. | Hojas Capacidades y Funciones × Microsoft; documento 03. | Cambios en la documentación de cada producto; prueba en el entorno del cliente. |
| SUPM-02 | Microsoft Ignite | Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar nombres, estados de vista previa, licencias y fechas. | Calendario público del evento. | Todas las capacidades, en especial las de IA y agentes. | Cierre del evento: revisar las 50 capacidades. |
| SUPM-03 | Licencias | La inclusión por plan (E3, E5 y E7) es una lectura del catálogo validado del 4 de noviembre de 2026. No reemplaza los términos de producto ni la cotización vigente. | Catálogo de seguridad de Microsoft validado el 4 de noviembre de 2026. | Hoja Capacidades, columnas de licencia. | Cambios de planes o de términos de producto. |
| SUPM-04 | Tareas por cadencia y guías del repositorio | Las tareas por cadencia provienen del plano B de GM-24 V7.1, de diez guías de excelencia operacional del autor (borradores de febrero a abril de 2026) y de las guías 16 y 17 de su repositorio, validadas el 11 de noviembre de 2026. La equivalencia entre las tareas de las guías y las del plano B es una propuesta de esta edición: una tarea se considera cubierta cuando una fila del libro tiene el mismo objeto y el mismo propósito, aunque la cadencia sea otra. La correspondencia de las 23 guías del repositorio con dominios, capacidades y funciones también es una propuesta. El puente del repositorio se construyó sobre la versión 1.0 del plan: sus fases se tradujeron a los ciclos trimestrales. | GM-24 V7.1, siete dominios; diez guías del autor; repositorio del autor (23 guías, 833 acciones). | Hojas Operación por cadencias, Tareas de las guías del autor, Guías del repositorio, Acciones de las guías e Indicadores técnicos; documentos M05, M10 y M11. | Actualización de las guías de operación oficiales, de las guías del autor o del repositorio; publicación de un puente del repositorio para la versión 2. |
| SUPM-05 | Formación | La serie Ninja Training 2026 es una guía de estudio independiente del autor, basada en material público; no es una publicación oficial de Microsoft. Las horas son estimadas. La cantidad de ejercicios y su entorno de práctica se tomaron del repositorio del autor. | Serie Ninja Training de Seguridad Microsoft 2026 (15 programas, 387 módulos y 2165 ejercicios), en el repositorio del autor. | Hojas Formación, Plan de formación y Guías del repositorio; documentos M06 y M11. | Actualización trimestral de la serie. |
| SUPM-06 | Dónde se mide cada indicador | La fuente del dato y el tipo de medición se asignaron por función, salvo en los 42 indicadores principales, que tienen fuente propia. Es una guía inicial. | Modelo de esta edición. | Hoja Indicadores × Microsoft; documento 07. | Línea base del diagnóstico: confirmar cada fuente. |
| SUPM-07 | Retiros y cambios con fecha | Hay cambios con fecha que afectan a la operación: Sentinel queda solo en el portal de Defender después del 31 de marzo de 2027; el catálogo unificado y el gobierno de datos clásico de Purview quedan en mantenimiento hasta el 12 de noviembre de 2027. | Documentación oficial consultada. | Capacidades MS-SIE-01 y MS-DAT-05. | Avisos de retiro de cada producto. |
| SUPM-08 | Concentración en un proveedor | Adoptar una plataforma única simplifica la integración y aumenta la dependencia de un proveedor. El modelo lo mide con K27 y KX14 y pide un límite aprobado por el directorio. | Núcleo 2.0: principios y decisiones de impacto. | Narrativas; hoja Funciones × Microsoft. | Revisión semestral del modelo de provisión (RT13). |

## 3. Qué revalidar después de Microsoft Ignite

1. Nombre, estado y licencia de las 50 capacidades, en especial las de IA y agentes.
2. Las 64 celdas de cobertura «no confirmado».
3. Las fechas de retiro y de cambio de portal.
4. Los programas de formación que dependen de productos en vista previa.

## 4. Silencios de la verificación de cobertura

Lo que la documentación oficial consultada no permitió confirmar:

1. PIM: no hay documentación de gobierno nativo de roles de Google Cloud, de AWS IAM ni de Active Directory local, ni anuncio de PIM multinube.
2. Defender for Identity: no se documentan controladores de dominio en VM de AWS o Google Cloud ni proveedores de identidad distintos de Okta.
3. Intune: no se aclara si administra VM Windows cliente en AWS o Google Cloud, ni si BitLocker, Windows LAPS y App Control aplican a Windows Server.
4. Defender for Office 365: no se confirma protección de Plan 1/Plan 2 para buzones locales ni para correo en la nube de terceros.
5. Contradicciones entre páginas oficiales: etiquetado de AWS RDS en Data Map; postura de IA en Google Vertex AI (página de postura frente a matriz multinube).
6. DSPM: no se nombra AWS ni se enumeran las aplicaciones de IA de terceros cubiertas; la página no muestra fecha.
7. Microsoft Sentinel data lake: la página abierta no declara su estado de disponibilidad.
8. Automatización de Sentinel: no se documentan acciones concretas sobre AWS, Google Cloud o sistemas locales.
9. Defender for Cloud: no se detalla qué planes de servicios de plataforma se pueden activar en el conector de Google Cloud.
10. Defender EASM: no se encontró estado ni aviso de retiro; la página de novedades no pudo abrirse.
11. Exposure Management: sin estado ni precio por conector para la disponibilidad general.
12. Azure Backup y Site Recovery: no se aclara el soporte de MARS/MABS en VM de AWS o Google Cloud ni de Site Recovery desde Google Cloud.
13. Azure Key Vault: no se describe el uso desde cargas en AWS o Google Cloud.
14. Microsoft Priva: no hay página oficial abierta con fechas de retiro de Subject Rights Requests, Consent Management, Privacy Assessments y Tracker Scanning; la cobertura fuera de Microsoft 365 no se confirma.
15. Guías de operación: Microsoft Intune y Microsoft Purview (protección de la información y DLP) no tienen guía de operación oficial con cadencias; Defender for Cloud y Microsoft Entra tienen guías sin tabla de cadencias (las secciones de identidad, autenticación y gobierno de la guía de Entra no se abrieron).
16. Zero Trust Workshop: sin página en dominios oficiales admitidos (solo microsoft.github.io).

## 5. Otros límites de esta edición

1. **La columna Microsoft 365 no se verificó.** Refleja el alcance nativo de cada producto y no formó parte de la investigación de cobertura.
2. **La cobertura de una función es la mejor entre sus capacidades.** No mide paridad funcional entre entornos.
3. **La asignación de capacidades a funciones es una propuesta del autor.** No proviene de una publicación de Microsoft.
4. **La fuente de medición se asignó por función**, salvo en los 42 indicadores principales.
5. **La equivalencia entre las tareas de las guías del autor y las del plano B es una propuesta de esta edición.** De las 379 tareas leídas, 234 se consideraron ya cubiertas. La lista completa está en el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron» y en la hoja «Tareas de las guías del autor».
6. **Los procedimientos de las guías del autor no se revalidaron** contra la documentación oficial vigente. Los borradores tienen fecha de febrero a abril de 2026; el de Intune, de noviembre. Las guías del repositorio declaran, acción por acción, si están verificadas en la documentación oficial o si son una propuesta: esta edición reproduce esa declaración y no la comprobó.
7. **El puente del repositorio se escribió para el plan 1.0.** La ubicación de las acciones en los cuatro ciclos y la relación de los indicadores técnicos con los indicadores del CISO son una lectura de esta edición. En 62 de los 184 indicadores técnicos, el indicador del CISO que propone el puente pertenece a una función que esta edición asocia con la guía.
8. **Solo dos guías del repositorio se integraron tarea por tarea**: riesgo interno y ciclo de vida de los datos. En 10 productos, las filas del libro provienen del borrador anterior de la guía; 11 guías no tienen filas en la hoja Operación por cadencias.
9. **El paquete leído no se comparó archivo por archivo con el repositorio público.** Coinciden la carpeta, las cifras y la fecha de consolidación. No se leyeron el programa de resiliencia ante ransomware ni las otras carpetas del repositorio.
10. **El dominio de nube no tiene una guía del autor**, ni entre los borradores ni en el repositorio.
11. **No se usaron datos de ningún cliente.** El libro llega vacío: el despliegue, el alcance y las personas los carga cada organización.
12. **Los precios no se incluyen.** Las referencias de licencia indican inclusión, no costo.
13. **No es una publicación oficial de Microsoft.**

## 6. Registro de cambios

| Revisión | Fecha | Cambio |
|:--:|:--:|---|
| 1 | 15 de noviembre de 2026 | Primera entrega de la edición Microsoft. |
| 2 | 15 de noviembre de 2026 | Se leyeron las guías de excelencia operacional del autor que faltaban. Las tareas pasan de 217 a 278; 123 filas indican la guía donde está el procedimiento; se agregan las cadencias semestral y anual, la hoja «Tareas de las guías del autor», el bloque 8 de la hoja Resumen y el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron». Se confirmó que la hoja Resumen tiene dos gráficos. No cambian el núcleo, las capacidades, la cobertura, las licencias, la formación ni la medición. |
| 3 | 15 de noviembre de 2026 | El núcleo pasa a cuatro ciclos trimestrales, con el diagnóstico dentro del ciclo 1. Se incorporan las guías de riesgo interno y de ciclo de vida de los datos del repositorio del autor: las tareas pasan de 278 a 325 y las prácticas, de 46 a 69. Se agregan las hojas «Guías del repositorio», «Acciones de las guías» e «Indicadores técnicos», el bloque 9 de la hoja Resumen, el bloque de ejercicios de la hoja Formación y el documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación». En las hojas Formación y Guías del repositorio, la fila de totales queda separada de la tabla por una fila en blanco. No cambian las capacidades, la cobertura, las licencias, las funciones, los indicadores ni los resultados clave. |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

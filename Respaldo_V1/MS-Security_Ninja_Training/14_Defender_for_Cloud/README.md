# Microsoft Defender for Cloud Ninja Training · Edición 2026

*Diseñar, desplegar, operar y optimizar Defender for Cloud en Azure, AWS, GCP y servidores con Arc: postura CNAPP, Defender for Servers Plan 2 capacidad por capacidad, protección de cargas de IA, respuesta a incidentes, Sentinel, Security Copilot y automatización.*

> **Noviembre de 2026:** conviven dos modelos de gestión y facturación: el clásico, por plan y desde el portal de Azure, y la gestión de planes en el portal de Defender con Defender Workload Units (DWU, 5 USD al mes cada una), en vista previa desde el 20 de octubre y sin reversión documentada. Defender for Cloud en el portal de Defender es GA desde el 5 de mayo, la facturación de Defender for Servers cambió el 1 de noviembre y, desde el 1 de julio, la seguridad de los agentes de IA exige Agent 365, que queda **fuera de alcance**: aquí aprendes la protección a nivel de modelo y la postura de IA. Microsoft Ignite (17 al 20 de noviembre) puede cambiar estados de vista previa. Empieza por [Qué cambió](00_Programa.md#cambios), los [planes y precios](00_Programa.md#planes-precios) y la [matriz de capacidades](00_Programa.md#capacidades).

Fuentes verificadas al 7 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 41 | 5 + comunidad | 873 | ~236 | 327 | 81 | 23 |

**Para quién:** Seguridad en la nube: arquitectura, plataforma, SOC, DevSecOps y FinOps.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Base.md](01_Nivel_1_Base.md) | Nivel 1 · Base · Fundamentos y despliegue · 9 módulos · ~43 h · evaluación y reto del nivel |
| [02_Nivel_2_Avanzado.md](02_Nivel_2_Avanzado.md) | Nivel 2 · Avanzado · Diseñar, desplegar y operar · 9 módulos · ~58 h · evaluación y reto del nivel |
| [03_Nivel_3_Experto.md](03_Nivel_3_Experto.md) | Nivel 3 · Experto · Proteger la IA, responder y automatizar · 9 módulos · ~61 h · evaluación y reto del nivel |
| [03b_Track_Especializacion_por_workload.md](03b_Track_Especializacion_por_workload.md) | Track · Especialización por workload · De cero a experto en cada plan · 7 módulos · ~48 h · evaluación y reto del nivel |
| [04_Track_Operacion_y_excelencia.md](04_Track_Operacion_y_excelencia.md) | Track · Operación y excelencia · Operar la seguridad en la nube con excelencia · 4 módulos · ~20 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Defender_for_Cloud_Ninja_Training_2026.html](Defender_for_Cloud_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Defender_for_Cloud_Ninja_Training_2026_Plan_y_catalogo.xlsx](Defender_for_Cloud_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Base · Fundamentos y despliegue:** [P0 Prerrequisitos y CNAPP](01_Nivel_1_Base.md#p0) · [B0 Cómo aprender y certificarte](01_Nivel_1_Base.md#b0) · [B1 Planes, portales y precios](01_Nivel_1_Base.md#b1) · [B2 Foundational CSPM y MCSB](01_Nivel_1_Base.md#b2) · [B3 Incorporación multinube](01_Nivel_1_Base.md#b3) · [B4 Defender for Servers P1 y P2](01_Nivel_1_Base.md#b4) · [B5 Mapa de planes de cargas](01_Nivel_1_Base.md#b5) · [B6 Primeras alertas e inventario](01_Nivel_1_Base.md#b6) · [B7 Laboratorio y línea base](01_Nivel_1_Base.md#b7)
- **Nivel 2 · Avanzado · Diseñar, desplegar y operar:** [M1 Diseño y arquitectura a escala](02_Nivel_2_Avanzado.md#m1) · [M2 Defender CSPM avanzado](02_Nivel_2_Avanzado.md#m2) · [M3 Servers P2: MDE y sin agente](02_Nivel_2_Avanzado.md#m3) · [M4 Servers P2: JIT, FIM y más](02_Nivel_2_Avanzado.md#m4) · [M5 Defender for Containers](02_Nivel_2_Avanzado.md#m5) · [M6 Storage y bases de datos](02_Nivel_2_Avanzado.md#m6) · [M7 Plano de control, apps y APIs](02_Nivel_2_Avanzado.md#m7) · [M8 DevOps y code-to-cloud](02_Nivel_2_Avanzado.md#m8) · [M9 Gestión de alertas a escala](02_Nivel_2_Avanzado.md#m9)
- **Nivel 3 · Experto · Proteger la IA, responder y automatizar:** [A1 Postura de IA (AI-SPM)](03_Nivel_3_Experto.md#a1) · [A2 Defender for AI Services](03_Nivel_3_Experto.md#a2) · [A3 Respuesta a incidentes](03_Nivel_3_Experto.md#a3) · [A4 Sentinel y portal de Defender](03_Nivel_3_Experto.md#a4) · [A5 Automatización y remediación](03_Nivel_3_Experto.md#a5) · [A6 Security Copilot y agentes](03_Nivel_3_Experto.md#a6) · [A7 Hunting: KQL, ARG y exposición](03_Nivel_3_Experto.md#a7) · [A8 Costos, cobertura y valor](03_Nivel_3_Experto.md#a8) · [A9 Casos de uso de punta a punta](03_Nivel_3_Experto.md#a9)
- **Track · Especialización por workload · De cero a experto en cada plan:** [W1 Containers a fondo](03b_Track_Especializacion_por_workload.md#w1) · [W2 Storage y datos sensibles](03b_Track_Especializacion_por_workload.md#w2) · [W3 Bases de datos a fondo](03b_Track_Especializacion_por_workload.md#w3) · [W4 Plano de control y CIEM](03b_Track_Especializacion_por_workload.md#w4) · [W5 Apps, APIs y serverless](03b_Track_Especializacion_por_workload.md#w5) · [W6 DevOps a fondo](03b_Track_Especializacion_por_workload.md#w6) · [W7 Multinube e híbrido](03b_Track_Especializacion_por_workload.md#w7)
- **Track · Operación y excelencia · Operar la seguridad en la nube con excelencia:** [O1 Modelo operativo y RACI](04_Track_Operacion_y_excelencia.md#o1) · [O2 KPI e informes ejecutivos](04_Track_Operacion_y_excelencia.md#o2) · [O3 Cumplimiento y evidencia](04_Track_Operacion_y_excelencia.md#o3) · [O4 Mejora continua e integrador](04_Track_Operacion_y_excelencia.md#o4)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y repositorios](05_Comunidad.md#c2) · [C3 Recursos en español](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Defender for Cloud? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para diseñar, desplegar, operar y optimizar la plataforma de protección de aplicaciones nativas de la nube (CNAPP) de Microsoft en Azure, AWS, GCP y servidores locales con Azure Arc: documentación de Microsoft Learn, notas de versión, blogs y webinars del equipo de producto, la serie *Defender for Cloud in the Field*, los laboratorios oficiales de GitHub y el trabajo de MVP y empleados de Microsoft. Tiene dos focos de profundidad: **Defender for Servers Plan 2, capacidad por capacidad**, y la **protección de cargas de IA** con la postura de IA de Defender CSPM y Defender for AI Services. Todo está verificado al 7 de noviembre de 2026.

El programa construye **tres niveles de capacidad —base, avanzada y experta—** y les suma dos tracks: el de **especialización por workload**, que lleva de cero a experto cada plan que puedes activar —contenedores, Storage, bases de datos, plano de control, aplicaciones y APIs, DevOps y multinube—, y el de **operación y excelencia**, que aplica esos niveles al trabajo diario: modelo operativo, KPI, cumplimiento con evidencia y mejora continua. Son 41 módulos y unas 236 horas, más una sección de comunidad, y cubren de forma explícita diseño, arquitectura, despliegue, operación y optimización, gestión de alertas, respuesta a incidentes, integración con Security Copilot y con Microsoft Sentinel, automatización de la respuesta y casos de uso. Cada nivel y cada track cierran con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, al estilo de los Ninja de Tech Community. Al terminar tendrás lo que pide un comité antes de ampliar la cobertura: un diseño documentado, planes desplegados como código, servidores y cargas de IA protegidos con evidencia, alertas afinadas que llegan a Sentinel, respuesta automatizada y un tablero de KPI y costos.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD, cambian con frecuencia y dependen de tu contrato, canal, región y moneda: confírmalos en la página oficial y con tu proveedor antes de presupuestar. El contenido regulatorio es una referencia y no constituye asesoría legal: las decisiones de cumplimiento corresponden a tus áreas de Legal, riesgo y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

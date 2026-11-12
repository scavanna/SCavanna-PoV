# Microsoft Purview DSPM y seguridad de datos para IA Ninja Training · Edición 2026

*Postura de seguridad de datos y preparación para la IA: DSPM unificada, sobreexposición, protección de Copilot y agentes, IA de terceros con pago por uso, Security Copilot, Data Security Investigations, SOC, métricas y gobierno de la privacidad en MCSA.*

> **Noviembre de 2026:** la DSPM unificada de Microsoft Purview está en disponibilidad general desde mayo de 2026 y las experiencias classic se retiran a fines de enero de 2027. La observabilidad de IA y el riesgo interno para agentes requieren Microsoft 365 E7 o Agent 365, y la IA de terceros se gestiona con pago por uso. Empieza por [Qué cambió](00_Programa.md#cambios) y por la tabla de [licencias](00_Programa.md#licencias).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 124 | ~80 | 88 | 53 | 13 |

**Para quién:** Seguridad de datos y gobierno de la IA.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Ver la postura y la exposición · 5 módulos · ~17 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Proteger Copilot, agentes e IA de terceros · 4 módulos · ~27 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Agentes de IA, postura de IA, regulación y SOC · 4 módulos · ~21 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~11 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~4 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_DSPM_IA_Ninja_Training_2026.html](Purview_DSPM_IA_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_DSPM_IA_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_DSPM_IA_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Ver la postura y la exposición:** [P0 Prerrequisitos y licencias](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 DSPM hoy](01_Nivel_1_Inicial.md#i1) · [I2 DSPM para IA](01_Nivel_1_Inicial.md#i2) · [I3 Riesgo de datos y exposición](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Proteger Copilot, agentes e IA de terceros:** [M1 Interacciones de Copilot](02_Nivel_2_Intermedio.md#m1) · [M2 Agentes y Agent 365](02_Nivel_2_Intermedio.md#m2) · [M3 IA de terceros](02_Nivel_2_Intermedio.md#m3) · [M4 SharePoint y sobreexposición](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · Agentes de IA, postura de IA, regulación y SOC:** [A1 Agentes de Security Copilot](03_Nivel_3_Avanzado.md#a1) · [A2 Defender for Cloud y AI-SPM](03_Nivel_3_Avanzado.md#a2) · [A3 Gobierno de IA y regulación](03_Nivel_3_Avanzado.md#a3) · [A4 Automatización y SOC](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y privacidad MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y canales](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de la seguridad de datos para la IA? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para conocer la postura de seguridad de tus datos y prepararlos para Microsoft 365 Copilot y los agentes de IA. Encontrarás documentación de Microsoft Learn, avisos del Message Center, blogs y webinars de los equipos de producto, laboratorios y el trabajo de MVP y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para quienes operan estas capacidades por razones distintas: el líder de seguridad de datos, el comité o centro de excelencia de IA, los administradores de Microsoft 365 y SharePoint que corrigen la sobreexposición, el SOC que investiga y el área de privacidad que cuida a las personas. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, al estilo de los Ninja de Tech Community.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre privacidad, captura de contenido, monitoreo y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

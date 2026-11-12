# Microsoft Purview Compliance Manager Ninja Training · Edición 2026

*Del puntaje a la evidencia defendible: puntuación de cumplimiento, evaluaciones y licencias, plantillas regulatorias propias o generadas desde el PDF de una norma, multinube, IA, reportes ejecutivos, automatización y normativa de MCSA para equipos de GRC.*

> **Noviembre de 2026:** las plantillas regulatorias generadas con IA desde el PDF de una norma llegaron a disponibilidad general en octubre de 2026, Compliance Manager evalúa apps y agentes de IA con plantillas como EU AI Act, ISO/IEC 42001 y NIST AI RMF, y desde agosto cubre Anthropic Claude Enterprise. Recuerda: Microsoft 365 E5 incluye la Data Protection Baseline y **tres** plantillas premium, no «todas». Empieza por [Qué cambió](00_Programa.md#cambios), la tabla de [licencias](00_Programa.md#licencias) y las [plantillas para MCSA](00_Programa.md#plantillas-mcsa).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 113 | ~63 | 95 | 54 | 12 |

**Para quién:** GRC, cumplimiento y auditoría.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~17 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Plantillas propias, multinube, IA y dirección · 4 módulos · ~17 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Automatizar, mapear y sostener · 4 módulos · ~17 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~10 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~2 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_Compliance_Manager_Ninja_Training_2026.html](Purview_Compliance_Manager_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_Compliance_Manager_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_Compliance_Manager_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Purview y el portal](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Puntuación y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Plantillas regulatorias](01_Nivel_1_Inicial.md#i2) · [I3 Acciones y evidencias](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Plantillas propias, multinube, IA y dirección:** [M1 Evaluaciones personalizadas](02_Nivel_2_Intermedio.md#m1) · [M2 Multinube y Defender for Cloud](02_Nivel_2_Intermedio.md#m2) · [M3 Cumplimiento para IA](02_Nivel_2_Intermedio.md#m3) · [M4 Reportes para la dirección](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · Automatizar, mapear y sostener:** [A1 Automatización y APIs](03_Nivel_3_Avanzado.md#a1) · [A2 Mapeo de controles](03_Nivel_3_Avanzado.md#a2) · [A3 Cumplimiento continuo](03_Nivel_3_Avanzado.md#a3) · [A4 Normativa regional](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y normativa MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de Compliance Manager? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para gestionar el cumplimiento regulatorio con Microsoft Purview Compliance Manager: documentación de Microsoft Learn, avisos del Message Center, videos de Microsoft Mechanics, el Ninja oficial de 2023 y el trabajo de MVPs y especialistas, todo verificado al 6 de noviembre de 2026. Y como el cumplimiento se juega en la normativa local, incluye el panorama de privacidad, ciberseguridad y sector financiero de México, Centroamérica y Sudamérica (sin Brasil).

Está pensada para quienes operan Compliance Manager por razones distintas: equipos de GRC y cumplimiento, auditoría interna, dueños de controles de TI, seguridad y nube, privacidad y el comité de riesgos. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y como los reguladores ya miran la IA, el recorrido llega a las plantillas de IA, las evaluaciones de agentes y las plantillas generadas desde el PDF de una norma.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

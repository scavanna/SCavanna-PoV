# Microsoft Sentinel Ninja Training · Edición 2026

*Reconstrucción completa de la serie inicial, intermedia y avanzada, ampliada a Security Copilot, agentes, MCP y Azure Logic Apps. Material oficial de Microsoft y de referentes de la comunidad, verificado y ordenado como un curso.*

> **Noviembre de 2026:** esta edición reconstruye el Ninja de Sentinel con los cambios de 2025 y 2026: Sentinel en el portal de Defender, data lake y graph, detecciones personalizadas, incident cases, UEBA behaviors, Security Copilot incluido en Microsoft 365 E5, agentes, servidor MCP y Agent Loop en Logic Apps. ¿Ya hiciste el Ninja original? Empieza por [Qué cambió desde el original](00_Programa.md#cambios).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 41 | 4 + comunidad | 760 | ~237 | 145 | 51 | 37 |

**Para quién:** SOC, ingeniería de detección y automatización.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 7 módulos · ~37 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Arquitectura, datos, detección y operación · 13 módulos · ~76 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Ingeniería de plataforma y contenido · 9 módulos · ~59 h · evaluación y reto del nivel |
| [04_Nivel_4_Experto_agentico.md](04_Nivel_4_Experto_agentico.md) | Nivel 4 · Experto agéntico · SOAR avanzado, Security Copilot, agentes y MCP · 7 módulos · ~59 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales, libros y recursos en español · 5 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Sentinel_Ninja_Training_2026.html](Sentinel_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Sentinel_Ninja_Training_2026_Plan_y_catalogo.xlsx](Sentinel_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Prerrequisitos](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender y soporte](01_Nivel_1_Inicial.md#i0) · [I1 Sentinel hoy](01_Nivel_1_Inicial.md#i1) · [I2 Cómo se usa](01_Nivel_1_Inicial.md#i2) · [I3 Despliegue y primeros pasos](01_Nivel_1_Inicial.md#i3) · [I4 KQL esencial](01_Nivel_1_Inicial.md#i4) · [I5 Laboratorios](01_Nivel_1_Inicial.md#i5)
- **Nivel 2 · Intermedio · Arquitectura, datos, detección y operación:** [M1 Workspaces y tenants](02_Nivel_2_Intermedio.md#m1) · [M2 Recolección de datos](02_Nivel_2_Intermedio.md#m2) · [M3 Logs, niveles y costos](02_Nivel_2_Intermedio.md#m3) · [M4 Enriquecimiento](02_Nivel_2_Intermedio.md#m4) · [M5 Transformación de logs](02_Nivel_2_Intermedio.md#m5) · [M6 Migración](02_Nivel_2_Intermedio.md#m6) · [M7 Analítica y detecciones](02_Nivel_2_Intermedio.md#m7) · [M8 Workbooks y reportes](02_Nivel_2_Intermedio.md#m8) · [M9 Incidentes](02_Nivel_2_Intermedio.md#m9) · [M10 Hunting](02_Nivel_2_Intermedio.md#m10) · [M11 UEBA](02_Nivel_2_Intermedio.md#m11) · [M12 Salud y optimización](02_Nivel_2_Intermedio.md#m12) · [M13 Automatización esencial](02_Nivel_2_Intermedio.md#m13)
- **Nivel 3 · Avanzado · Ingeniería de plataforma y contenido:** [A1 ASIM](03_Nivel_3_Avanzado.md#a1) · [A2 KQL avanzado](03_Nivel_3_Avanzado.md#a2) · [A3 Casos de uso](03_Nivel_3_Avanzado.md#a3) · [A4 Contenido como código](03_Nivel_3_Avanzado.md#a4) · [A5 Conectores CCF](03_Nivel_3_Avanzado.md#a5) · [A6 APIs](03_Nivel_3_Avanzado.md#a6) · [A7 Notebooks y ML](03_Nivel_3_Avanzado.md#a7) · [A8 Data lake y graph](03_Nivel_3_Avanzado.md#a8) · [A9 Multi-inquilino y MSSP](03_Nivel_3_Avanzado.md#a9)
- **Nivel 4 · Experto agéntico · SOAR avanzado, Security Copilot, agentes y MCP:** [X1 SOAR con Logic Apps](04_Nivel_4_Experto_agentico.md#x1) · [X2 Security Copilot](04_Nivel_4_Experto_agentico.md#x2) · [X3 Copilot + Logic Apps](04_Nivel_4_Experto_agentico.md#x3) · [X4 Plugins y promptbooks](04_Nivel_4_Experto_agentico.md#x4) · [X5 Agentes](04_Nivel_4_Experto_agentico.md#x5) · [X6 Servidor MCP](04_Nivel_4_Experto_agentico.md#x6) · [X7 Proyecto integrador](04_Nivel_4_Experto_agentico.md#x7)
- **Comunidad · Referentes, canales, libros y recursos en español:** [C1 Referentes](05_Comunidad.md#c1) · [C2 YouTube y podcasts](05_Comunidad.md#c2) · [C3 Libros](05_Comunidad.md#c3) · [C4 En español](05_Comunidad.md#c4) · [C5 Mantenerse al día](05_Comunidad.md#c5)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Sentinel? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para dominar Sentinel de punta a punta: documentación de Microsoft Learn, anuncios y blogs de los equipos de producto, webinars de la Microsoft Security Community, laboratorios y repositorios de GitHub, y el trabajo de MVPs y empleados de Microsoft que enseñan el producto todos los días.

Puedes seguirla de principio a fin o saltar directamente a tu rol. Cada nivel cierra con una evaluación de conocimientos y, si alcanzas el 80 %, puedes generar tu certificado de finalización, como en el Ninja original. Y como el SOC ya no termina en el playbook, el recorrido continúa hasta el SOC agéntico: Security Copilot, agentes, el servidor MCP de Sentinel y la automatización con Azure Logic Apps.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

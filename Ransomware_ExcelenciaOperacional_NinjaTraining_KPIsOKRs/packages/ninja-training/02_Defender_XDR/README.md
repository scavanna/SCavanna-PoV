# Microsoft Defender XDR Ninja Training · Edición 2026

*Defender for Office 365, Endpoint, Identity y Microsoft Entra ID Protection de cero a experto, con integración con Sentinel, automatización, playbooks de respuesta, hunting, ingeniería de detecciones, Security Copilot y un track de excelencia operacional del SOC.*

> **Noviembre de 2026:** esta edición reconstruye el Ninja de Defender XDR con los cambios de 2025 y 2026: incident cases, ISOC en vista previa, sensor v3.x de Defender for Identity, retiro de las directivas de riesgo heredadas de Entra ID Protection (1 de octubre), AIR de Defender for Endpoint integrado al antivirus (1 de septiembre), Security Copilot incluido en Microsoft 365 E5 y agentes. ¿Ya hiciste el Ninja oficial? Empieza por [Qué cambió](00_Programa.md#cambios); si lideras un SOC, por el [Marco de excelencia del SOC](00_Programa.md#excelencia-soc).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 38 | 4 + comunidad | 295 | ~250 | 219 | 60 | 37 |

**Para quién:** SOC, respuesta a incidentes, endpoint, correo e identidad.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 10 módulos · ~54 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Operar, investigar y responder · 10 módulos · ~76 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Respuesta, automatización e ingeniería · 8 módulos · ~74 h · evaluación y reto del nivel |
| [04_Nivel_4_Excelencia_del_SOC.md](04_Nivel_4_Excelencia_del_SOC.md) | Nivel 4 · Excelencia del SOC · Operación de clase mundial · 7 módulos · ~40 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Defender_XDR_Ninja_Training_2026.html](Defender_XDR_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Defender_XDR_Ninja_Training_2026_Plan_y_catalogo.xlsx](Defender_XDR_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Prerrequisitos](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Defender XDR hoy](01_Nivel_1_Inicial.md#i1) · [I2 Licencias, piloto y roles](01_Nivel_1_Inicial.md#i2) · [I3 MDO: fundamentos](01_Nivel_1_Inicial.md#i3) · [I4 MDE: fundamentos](01_Nivel_1_Inicial.md#i4) · [I5 MDI: fundamentos](01_Nivel_1_Inicial.md#i5) · [I6 ID Protection: fundamentos](01_Nivel_1_Inicial.md#i6) · [I7 KQL y búsqueda avanzada](01_Nivel_1_Inicial.md#i7) · [I8 Laboratorios](01_Nivel_1_Inicial.md#i8)
- **Nivel 2 · Intermedio · Operar, investigar y responder:** [M1 Incidentes y alertas](02_Nivel_2_Intermedio.md#m1) · [M2 MDO: investigación](02_Nivel_2_Intermedio.md#m2) · [M3 MDE: ASR y protección](02_Nivel_2_Intermedio.md#m3) · [M4 MDI: postura y respuesta](02_Nivel_2_Intermedio.md#m4) · [M5 ID Protection: riesgo y CA](02_Nivel_2_Intermedio.md#m5) · [M6 Vulnerabilidades y exposición](02_Nivel_2_Intermedio.md#m6) · [M7 AIR e interrupción](02_Nivel_2_Intermedio.md#m7) · [M8 Integración con Sentinel](02_Nivel_2_Intermedio.md#m8) · [M9 Hunting](02_Nivel_2_Intermedio.md#m9) · [M10 Detecciones y ajuste](02_Nivel_2_Intermedio.md#m10)
- **Nivel 3 · Avanzado · Respuesta, automatización e ingeniería:** [A1 Playbooks de respuesta](03_Nivel_3_Avanzado.md#a1) · [A2 Automatización y Logic Apps](03_Nivel_3_Avanzado.md#a2) · [A3 Hunting e inteligencia](03_Nivel_3_Avanzado.md#a3) · [A4 APIs](03_Nivel_3_Avanzado.md#a4) · [A5 Ingeniería y purple team](03_Nivel_3_Avanzado.md#a5) · [A6 Security Copilot y agentes](03_Nivel_3_Avanzado.md#a6) · [A7 Multi-inquilino y MDR](03_Nivel_3_Avanzado.md#a7) · [A8 Proyecto integrador](03_Nivel_3_Avanzado.md#a8)
- **Nivel 4 · Excelencia del SOC · Operación de clase mundial:** [S1 Modelo operativo](04_Nivel_4_Excelencia_del_SOC.md#s1) · [S2 Procesos e incidentes](04_Nivel_4_Excelencia_del_SOC.md#s2) · [S3 Métricas y tableros](04_Nivel_4_Excelencia_del_SOC.md#s3) · [S4 Madurez y ejercicios](04_Nivel_4_Excelencia_del_SOC.md#s4) · [S5 Detección como proceso](04_Nivel_4_Excelencia_del_SOC.md#s5) · [S6 Automatización e IA](04_Nivel_4_Excelencia_del_SOC.md#s6) · [S7 Gobierno y reporte](04_Nivel_4_Excelencia_del_SOC.md#s7)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y español](05_Comunidad.md#c2) · [C3 Mantenerse al día](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Defender XDR? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para dominar la detección y respuesta extendida de Microsoft en correo, endpoints e identidades: documentación de Microsoft Learn, anuncios de los equipos de producto, webinars y el Virtual Ninja Show, laboratorios y repositorios de GitHub, y el trabajo de MVP y empleados de Microsoft que enseñan el producto todos los días.

Puedes seguirla de principio a fin o por rol. Cada nivel cierra con una evaluación de conocimientos y, si alcanzas el 80 %, puedes generar tu certificado de finalización, como en el Ninja oficial. Y como un SOC de primer nivel no se define solo por la tecnología, el recorrido suma un track de excelencia operacional —modelo operativo, procesos, métricas, madurez, IA con supervisión humana y gobierno— basado en la versión pública del Security Adoption Framework de Microsoft y en marcos abiertos.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

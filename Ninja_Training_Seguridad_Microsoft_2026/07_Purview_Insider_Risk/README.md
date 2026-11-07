# Microsoft Purview Insider Risk Management Ninja Training · Edición 2026

*Riesgo interno con privacidad por diseño: indicadores y conectores, políticas por escenario, triage en la cola unificada, evidencia forense, Protección adaptativa, IA y agentes, Defender XDR, Triage Agent de Security Copilot y gobierno con RR. HH., Legal y privacidad.*

> **Noviembre de 2026:** la pestaña «Alerts (classic)» de Insider Risk Management se deprecó el 1 de octubre de 2026 y la cola unificada, con el Triage Agent integrado, es ahora la experiencia de trabajo; Risky AI usage y Risky Agents llevan el riesgo interno a la IA y a los agentes. Recuerda: desde el 1 de octubre de 2025 Microsoft 365 E5 Compliance se llama Microsoft Purview Suite, y Microsoft Defender Suite **no** incluye IRM. Empieza por [Qué cambió](00_Programa.md#cambios), la tabla de [licencias](00_Programa.md#licencias) y el [proceso de casos con privacidad](00_Programa.md#gobierno-casos).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 102 | ~75 | 95 | 53 | 15 |

**Para quién:** Riesgo interno: seguridad, RR. HH., Legal y privacidad.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos con privacidad por diseño · 5 módulos · ~18 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Políticas, investigación y respuesta proporcional · 4 módulos · ~23 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · IA, agentes, SOC y automatización · 4 módulos · ~20 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~10 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~4 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_Insider_Risk_Ninja_Training_2026.html](Purview_Insider_Risk_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_Insider_Risk_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_Insider_Risk_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos con privacidad por diseño:** [P0 Prerrequisitos y auditoría](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Privacidad y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Indicadores y conectores](01_Nivel_1_Inicial.md#i2) · [I3 Triage y casos](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Políticas, investigación y respuesta proporcional:** [M1 Políticas por escenario](02_Nivel_2_Intermedio.md#m1) · [M2 Investigación y forense](02_Nivel_2_Intermedio.md#m2) · [M3 Protección adaptativa](02_Nivel_2_Intermedio.md#m3) · [M4 RR. HH., Legal y eDiscovery](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · IA, agentes, SOC y automatización:** [A1 IA y agentes](03_Nivel_3_Avanzado.md#a1) · [A2 Defender XDR y Sentinel](03_Nivel_3_Avanzado.md#a2) · [A3 Triage Agent](03_Nivel_3_Avanzado.md#a3) · [A4 Automatización y APIs](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de Insider Risk Management? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para detectar, investigar y responder al riesgo interno en Microsoft 365 sin perder de vista a las personas: documentación de Microsoft Learn, avisos del Centro de mensajes, blogs del equipo de producto, videos de Microsoft Mechanics, la ruta oficial de SC-401 y el trabajo de MVP y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para el equipo de riesgo interno —analistas e investigadores— y para quienes deciden con él: RR. HH., Legal, privacidad y el SOC, que recibe las alertas en Defender XDR. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, al estilo del Ninja original. Y como el riesgo interno ya no es solo humano, el recorrido llega a la IA generativa, a los agentes y al Triage Agent de Security Copilot.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

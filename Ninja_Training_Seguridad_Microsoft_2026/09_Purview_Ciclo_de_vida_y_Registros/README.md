# Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026

*Retención, registros y archivo en Microsoft 365 de punta a punta: directivas y etiquetas, plan de archivos, eliminación con prueba, eventos, buzones inactivos, Copilot e IA, Microsoft Graph, holds de eDiscovery y gobierno con Legal y privacidad.*

> **Noviembre de 2026:** la retención ya no es solo correo y archivos. Las interacciones con Copilot y otras apps de IA tienen ubicaciones propias con pago por uso, los registros de llamadas de Teams necesitan directivas por PowerShell desde abril, la limpieza prioritaria exige tres aprobaciones desde julio, los buzones inactivos reciben un delay hold de 30 días desde agosto y el archivo de expansión automática llega a 3 TB para licencias de nivel E5 desde mediados de octubre. Empieza por [Qué cambió](00_Programa.md#cambios) y por la tabla de [Licencias](00_Programa.md#licencias).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 86 | ~61 | 99 | 59 | 6 |

**Para quién:** Gestión documental, registros y retención.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~16 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Automatizar y eliminar con evidencia · 4 módulos · ~17 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · IA, APIs, holds y regulación · 4 módulos · ~15 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Programa, métricas y gobierno · 3 módulos · ~9 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~4 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_Lifecycle_Records_Ninja_Training_2026.html](Purview_Lifecycle_Records_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_Lifecycle_Records_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_Lifecycle_Records_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Prerrequisitos y licencias](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Directivas y etiquetas](01_Nivel_1_Inicial.md#i1) · [I2 Retención por carga de trabajo](01_Nivel_1_Inicial.md#i2) · [I3 Registros y plan de archivos](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Automatizar y eliminar con evidencia:** [M1 Autoaplicación de etiquetas](02_Nivel_2_Intermedio.md#m1) · [M2 Revisión de eliminación](02_Nivel_2_Intermedio.md#m2) · [M3 Retención por eventos](02_Nivel_2_Intermedio.md#m3) · [M4 Archivo, inactivos y PST](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · IA, APIs, holds y regulación:** [A1 Retención de Copilot e IA](03_Nivel_3_Avanzado.md#a1) · [A2 APIs y automatización](03_Nivel_3_Avanzado.md#a2) · [A3 Holds y eDiscovery](03_Nivel_3_Avanzado.md#a3) · [A4 Regulación y multigeografía](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Programa, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y normativa MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja del ciclo de vida de los datos y la gestión de registros en Microsoft Purview? Esta guía te lleva de los principios de retención a un programa de registros que resiste una auditoría. Reúne, ordenados como un curso, la documentación de Microsoft Learn, los anuncios del equipo de producto, los webinars de la Microsoft Security Community y el trabajo de MVPs y empleados de Microsoft que enseñan retención y registros todos los días.

Puedes seguirla de punta a punta o por tu rol: gestión de registros, cumplimiento, Legal, privacidad, dueños de datos o administración de Exchange, SharePoint y Teams. Cada nivel cierra con una evaluación y, si alcanzas el 80 %, puedes generar tu certificado de finalización. Y como la retención ya no termina en el correo y los archivos, el recorrido llega hasta las interacciones con Copilot y otras apps de IA, la automatización con Microsoft Graph y el gobierno con Legal y privacidad en MCSA (México, Centroamérica y Sudamérica).

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

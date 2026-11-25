# Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026

*Clasificación, etiquetas de confidencialidad y cifrado en Microsoft 365 y más allá: SIT, EDM y clasificadores, etiquetado automático, contenedores, reuniones y Fabric, escáner, Copilot y agentes, DKE y Customer Key, SOC, métricas y gobierno en MCSA.*

> **Noviembre de 2026:** el auto-etiquetado de SharePoint y OneDrive sube a 500.000 archivos por día (agosto) y a simulaciones de 20 millones de elementos (septiembre), Copilot exige los derechos de uso VIEW y EXTRACT sobre contenido cifrado (documentación del 3 de noviembre), DKE documenta sus límites con Copilot, Loop y reuniones (27 de octubre) y las directivas de archivo de Defender for Cloud Apps se retiran el **6 de enero de 2027**. Empieza por [Qué cambió](00_Programa.md#cambios), la tabla de [Licencias](00_Programa.md#licencias) y la [Matriz de etiquetado y cifrado](00_Programa.md#matriz-etiquetado).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 133 | ~78 | 94 | 57 | 12 |

**Para quién:** Protección de la información y dueños de datos.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~19 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Automatizar y proteger · 4 módulos · ~24 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · IA, código, claves y SOC · 4 módulos · ~20 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Programa, métricas y gobierno · 3 módulos · ~11 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~4 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_Information_Protection_Ninja_Training_2026.html](Purview_Information_Protection_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_Information_Protection_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_Information_Protection_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Portal, permisos y facturación](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Qué incluye E3, E5 y E7](01_Nivel_1_Inicial.md#i1) · [I2 Clasificación de datos](01_Nivel_1_Inicial.md#i2) · [I3 Taxonomía y publicación](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Automatizar y proteger:** [M1 Etiquetado automático](02_Nivel_2_Intermedio.md#m1) · [M2 Cifrado y control de uso](02_Nivel_2_Intermedio.md#m2) · [M3 Contenedores, Teams y Fabric](02_Nivel_2_Intermedio.md#m3) · [M4 Escáner y Cloud Apps](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · IA, código, claves y SOC:** [A1 Copilot y agentes](03_Nivel_3_Avanzado.md#a1) · [A2 PowerShell, Graph y SDK](03_Nivel_3_Avanzado.md#a2) · [A3 Customer Key y DKE](03_Nivel_3_Avanzado.md#a3) · [A4 Monitoreo y SOC](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Programa, métricas y gobierno:** [O1 Modelo operativo y adopción](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno y normativa MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Purview Information Protection? Esta guía te lleva de los tipos de información confidencial a un programa de etiquetado y cifrado que resiste una auditoría y que Microsoft 365 Copilot respeta. Reúne, ordenados como un curso, la documentación de Microsoft Learn, los anuncios del equipo de producto, la ruta Ninja oficial, los laboratorios de SC-401 y el trabajo de MVPs y empleados de Microsoft que enseñan clasificación, etiquetas y cifrado todos los días.

Puedes seguirla de punta a punta o por tu rol: protección de la información, dueños de datos, cumplimiento, administración de Exchange, SharePoint y Teams, SOC o gestión del cambio. Cada nivel cierra con una evaluación y, si alcanzas el 80 %, puedes generar tu certificado de finalización, como en los Ninja de Tech Community. Y como un error de cifrado puede dejar a las personas sin acceso a su propio contenido, cada práctica empieza con etiquetas de prueba, pilotos y un plan de reversión.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

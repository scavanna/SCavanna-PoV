# Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026

*Del caso a la evidencia defendible: eDiscovery unificado, retenciones legales, conjuntos de revisión, exportación con cadena de custodia, Audit Standard y Premium, evidencia de Copilot y agentes, Data Security Investigations e integración con el SOC.*

> **Noviembre de 2026:** el eDiscovery clásico ya no existe (retiro completo el 31 de agosto de 2025), las exportaciones de búsquedas expiran a los 14 días desde el 16 de febrero de 2026 y la API AuditLogQuery de Microsoft Graph llegó a disponibilidad general en octubre de 2026, antes del retiro de `Search-UnifiedAuditLog` el 15 de octubre de 2027. Empieza por [Qué cambió](00_Programa.md#cambios) y la tabla de [cambios y retiros 2024–2027](00_Programa.md#cambios-retiros).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 97 | ~70 | 93 | 57 | 7 |

**Para quién:** Legal, investigaciones y forense.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~16 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Preservar, revisar, investigar y producir · 4 módulos · ~21 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · IA, automatización y SOC · 4 módulos · ~20 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~9 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~4 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_eDiscovery_Audit_Ninja_Training_2026.html](Purview_eDiscovery_Audit_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_eDiscovery_Audit_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_eDiscovery_Audit_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Prerrequisitos y licencias](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 eDiscovery unificado](01_Nivel_1_Inicial.md#i1) · [I2 Audit Standard y Premium](01_Nivel_1_Inicial.md#i2) · [I3 Búsqueda y KeyQL](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Preservar, revisar, investigar y producir:** [M1 Holds y custodios](02_Nivel_2_Intermedio.md#m1) · [M2 Review sets y analítica](02_Nivel_2_Intermedio.md#m2) · [M3 Audit para investigaciones](02_Nivel_2_Intermedio.md#m3) · [M4 Exportación y custodia](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · IA, automatización y SOC:** [A1 IA y agentes como evidencia](03_Nivel_3_Avanzado.md#a1) · [A2 Graph y PowerShell](03_Nivel_3_Avanzado.md#a2) · [A3 IR, Sentinel y Defender XDR](03_Nivel_3_Avanzado.md#a3) · [A4 Security Copilot y DSI](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de eDiscovery y Audit? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para preservar, encontrar, revisar y producir información de Microsoft 365 con criterio legal y técnico, y para reconstruir con el registro de auditoría quién hizo qué, cuándo y desde dónde. Documentación de Microsoft Learn, avisos del Message Center, webinars de la Microsoft Security Community, el Ninja oficial de eDiscovery y el trabajo de MVPs y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para quienes operan estas capacidades por razones distintas: Legal y litigios, investigaciones internas, cumplimiento y registros, auditoría interna, privacidad y el SOC, que usa la auditoría como fuente de investigación. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y como la evidencia ya no es solo correo y documentos, el recorrido llega a Copilot, los agentes, Data Security Investigations y Security Copilot.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

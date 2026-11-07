# Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026

*Supervisa comunicaciones con privacidad por diseño: políticas y clasificadores, revisión y remediación, Copilot y apps de IA con pago por uso, Information Barriers, conectores, auditoría y supervisión regulada, con el modelo operativo que exigen Legal, RR. HH. y privacidad.*

> **Noviembre de 2026:** Communication Compliance ya supervisa Microsoft 365 Copilot (con licencias de Copilot y sin pago por uso) y, con pago por uso, Copilot Studio, Fabric, Security Copilot y apps de IA como ChatGPT Enterprise o Claude Enterprise (desde agosto de 2026). Information Barriers estrenó en septiembre de 2026 un reporte de cumplimiento que incluye SharePoint Embedded, y `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027: migra tu evidencia a la API AuditLogQuery de Microsoft Graph. Empieza por [Qué cambió](00_Programa.md#cambios), la tabla de [licencias](00_Programa.md#licencias) y la de [gobierno y privacidad](00_Programa.md#gobierno-privacidad).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 92 | ~57 | 81 | 51 | 12 |

**Para quién:** Cumplimiento de comunicaciones y supervisión regulatoria.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~17 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · IA, barreras, privacidad e integración · 4 módulos · ~16 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Evidencia, conectores y supervisión regulada · 4 módulos · ~14 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~8 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~2 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_Communication_Compliance_Ninja_Training_2026.html](Purview_Communication_Compliance_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_Communication_Compliance_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_Communication_Compliance_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Portal y permisos](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Canales y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Políticas y clasificadores](01_Nivel_1_Inicial.md#i2) · [I3 Revisión y remediación](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · IA, barreras, privacidad e integración:** [M1 Copilot y apps de IA](02_Nivel_2_Intermedio.md#m1) · [M2 Information Barriers](02_Nivel_2_Intermedio.md#m2) · [M3 Privacidad y roles](02_Nivel_2_Intermedio.md#m3) · [M4 Insider Risk y eDiscovery](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · Evidencia, conectores y supervisión regulada:** [A1 Conectores de terceros](03_Nivel_3_Avanzado.md#a1) · [A2 Reportes y auditoría](03_Nivel_3_Avanzado.md#a2) · [A3 Power Automate y APIs](03_Nivel_3_Avanzado.md#a3) · [A4 Supervisión financiera](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de Communication Compliance e Information Barriers? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para detectar, revisar y remediar comunicaciones de riesgo en correo, Teams, Viva Engage, Microsoft 365 Copilot y otras apps de IA, y para impedir que grupos que no deben comunicarse colaboren en Teams, SharePoint y OneDrive. Documentación de Microsoft Learn, anuncios oficiales, avisos del Message Center, el Ninja oficial de 2022 y el trabajo de MVPs y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para equipos que operan estas capacidades por razones distintas: cumplimiento y conducta, supervisión regulada (por ejemplo, en el sector financiero), RR. HH., Legal, privacidad y los administradores de colaboración que mantienen las barreras de información. Puedes seguirla completa o por rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y una regla atraviesa todo el recorrido: supervisar a personas reales exige aprobación previa y políticas de prueba con alcance acotado.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

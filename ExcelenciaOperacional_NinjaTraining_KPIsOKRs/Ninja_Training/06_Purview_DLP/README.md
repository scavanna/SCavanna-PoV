# Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026

*Prevención de pérdida de datos de punta a punta: Exchange, SharePoint, OneDrive y Teams, endpoints y navegadores, red, Copilot y agentes, protección adaptativa, integración con el SOC, Security Copilot y la operación diaria del programa DLP.*

> **Noviembre de 2026:** desde inicios de octubre, una regla integrada de ajuste de alertas registra las señales DLP como *behaviors* en Defender XDR, en lugar de alertas e incidentes; la API heredada `/security/alerts` de Microsoft Graph dejó de responder el 15 de octubre; y la ubicación «Instances» de Defender for Cloud Apps se retira el 6 de enero de 2027. Copilot y Cowork, la red con Global Secure Access, Edge for Business y FTP/SFTP ya forman parte del alcance de DLP. Empieza por [Qué cambió](00_Programa.md#cambios) y la tabla de [Licencias](00_Programa.md#licencias).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 18 | 4 + comunidad | 124 | ~87 | 100 | 57 | 18 |

**Para quién:** Prevención de pérdida de datos.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 5 módulos · ~26 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Ajustar, investigar y extender · 4 módulos · ~25 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Código, SOC y clasificación a escala · 4 módulos · ~22 h · evaluación y reto del nivel |
| [04_Nivel_4_Operacion.md](04_Nivel_4_Operacion.md) | Nivel 4 · Operación · Modelo operativo, métricas y gobierno · 3 módulos · ~11 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 2 módulos · ~3 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Purview_DLP_Ninja_Training_2026.html](Purview_DLP_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Purview_DLP_Ninja_Training_2026_Plan_y_catalogo.xlsx](Purview_DLP_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Portal, roles y prueba](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Ubicaciones y licencias](01_Nivel_1_Inicial.md#i1) · [I2 Diseño y simulación](01_Nivel_1_Inicial.md#i2) · [I3 Endpoints y navegadores](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio · Ajustar, investigar y extender:** [M1 Ajuste y falsos positivos](02_Nivel_2_Intermedio.md#m1) · [M2 Alertas e investigación](02_Nivel_2_Intermedio.md#m2) · [M3 Copilot, IA y red](02_Nivel_2_Intermedio.md#m3) · [M4 Protección adaptativa](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado · Código, SOC y clasificación a escala:** [A1 DLP como código](03_Nivel_3_Avanzado.md#a1) · [A2 SOC: Defender XDR y Sentinel](03_Nivel_3_Avanzado.md#a2) · [A3 EDM, huellas y OCR](03_Nivel_3_Avanzado.md#a3) · [A4 Security Copilot y agentes](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación · Modelo operativo, métricas y gobierno:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Purview Data Loss Prevention? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para diseñar, desplegar, ajustar y operar DLP en toda la superficie por donde hoy viajan los datos: correo, SharePoint, OneDrive y Teams, equipos Windows y macOS, navegadores, la red, Fabric y Power BI, repositorios locales, Microsoft 365 Copilot y los agentes. Documentación de Microsoft Learn, avisos del Centro de mensajes, blogs de los equipos de producto, laboratorios oficiales y el trabajo de MVPs y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para el equipo de DLP y seguridad de datos, el SOC que recibe sus señales en Defender XDR, los equipos de endpoint y de red y los dueños de datos de las áreas de negocio. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en los Ninja de Tech Community. Y una regla de oro atraviesa todo el recorrido: simulación y auditoría antes de bloquear.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

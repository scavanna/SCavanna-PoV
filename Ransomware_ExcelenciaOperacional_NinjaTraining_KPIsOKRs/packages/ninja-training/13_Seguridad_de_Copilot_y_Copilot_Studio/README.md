# Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio Ninja Training · Edición 2026

*Proteger, gobernar y auditar Microsoft 365 Copilot, Copilot Chat, los agentes y Copilot Studio solo con herramientas de Microsoft: centro de administración, SharePoint Advanced Management, Purview, Entra, Intune, Defender, Sentinel y Power Platform, sin depender de Agent 365.*

> **Noviembre de 2026:** Microsoft Learn ya llama «Microsoft Copilot» a Microsoft 365 Copilot y «Microsoft Copilot Chat» a Microsoft 365 Copilot Chat, y la app pasó a ser la app Microsoft Copilot en copilot.cloud.microsoft (MC1454108, 13 de agosto de 2026); las licencias y los precios conservan el nombre anterior. Desde el 31 de julio Restricted SharePoint Search no admite nuevas habilitaciones (usa Restricted Content Discovery), desde mayo Copilot Studio crea un Entra Agent ID para cada agente nuevo y desde el 1 de julio la seguridad de agentes en Defender exige Agent 365, que queda **fuera de alcance**: aquí aprendes las alternativas incluidas en tus licencias. Microsoft Ignite (17 al 20 de noviembre) puede cambiar estados de vista previa. Empieza por [Qué cambió](00_Programa.md#cambios), las [licencias](00_Programa.md#licencias) y [qué queda fuera](00_Programa.md#fuera-de-alcance).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 34 | 4 + comunidad | 502 | ~184 | 219 | 60 | 30 |

**Para quién:** Seguridad y gobierno de la IA: Microsoft 365, Power Platform, datos, SOC y cumplimiento.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 9 módulos · ~42 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Proteger · 8 módulos · ~52 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Detectar, auditar y responder · 8 módulos · ~54 h · evaluación y reto del nivel |
| [04_Nivel_4_Gobierno_y_operacion_continua.md](04_Nivel_4_Gobierno_y_operacion_continua.md) | Nivel 4 · Gobierno y operación continua · Operar la IA con excelencia · 6 módulos · ~30 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Seguridad_Copilot_Copilot_Studio_Ninja_Training_2026.html](Seguridad_Copilot_Copilot_Studio_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Seguridad_Copilot_Copilot_Studio_Ninja_Training_2026_Plan_y_catalogo.xlsx](Seguridad_Copilot_Copilot_Studio_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 IA generativa, RAG y agentes](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender y pedir ayuda](01_Nivel_1_Inicial.md#i0) · [I1 Cómo funciona Copilot](01_Nivel_1_Inicial.md#i1) · [I2 Licencias y superficie](01_Nivel_1_Inicial.md#i2) · [I3 Copilot Control System](01_Nivel_1_Inicial.md#i3) · [I4 Modelo de amenazas](01_Nivel_1_Inicial.md#i4) · [I5 Sobreexposición y despliegue](01_Nivel_1_Inicial.md#i5) · [I6 Identidad y dispositivos](01_Nivel_1_Inicial.md#i6) · [I7 Laboratorio y línea base](01_Nivel_1_Inicial.md#i7)
- **Nivel 2 · Intermedio · Proteger:** [M1 SharePoint Advanced Management](02_Nivel_2_Intermedio.md#m1) · [M2 DSPM para IA](02_Nivel_2_Intermedio.md#m2) · [M3 Etiquetas y cifrado](02_Nivel_2_Intermedio.md#m3) · [M4 DLP para Copilot](02_Nivel_2_Intermedio.md#m4) · [M5 Agentes en Microsoft 365](02_Nivel_2_Intermedio.md#m5) · [M6 Entornos de Copilot Studio](02_Nivel_2_Intermedio.md#m6) · [M7 Directivas de datos y acceso](02_Nivel_2_Intermedio.md#m7) · [M8 Shadow AI e IA de terceros](02_Nivel_2_Intermedio.md#m8)
- **Nivel 3 · Avanzado · Detectar, auditar y responder:** [A1 Auditoría de Copilot y agentes](03_Nivel_3_Avanzado.md#a1) · [A2 Retención y eDiscovery](03_Nivel_3_Avanzado.md#a2) · [A3 Riesgo interno y CC para IA](03_Nivel_3_Avanzado.md#a3) · [A4 Defender XDR para la IA](03_Nivel_3_Avanzado.md#a4) · [A5 Sentinel para la IA](03_Nivel_3_Avanzado.md#a5) · [A6 Copilot Studio avanzado](03_Nivel_3_Avanzado.md#a6) · [A7 Identidades de agentes](03_Nivel_3_Avanzado.md#a7) · [A8 Red teaming y respuesta](03_Nivel_3_Avanzado.md#a8)
- **Nivel 4 · Gobierno y operación continua · Operar la IA con excelencia:** [O1 Marcos de gobierno de IA](04_Nivel_4_Gobierno_y_operacion_continua.md#o1) · [O2 Modelo operativo y RACI](04_Nivel_4_Gobierno_y_operacion_continua.md#o2) · [O3 Ciclo de vida de agentes](04_Nivel_4_Gobierno_y_operacion_continua.md#o3) · [O4 Métricas e informes](04_Nivel_4_Gobierno_y_operacion_continua.md#o4) · [O5 Automatizar la gobernanza](04_Nivel_4_Gobierno_y_operacion_continua.md#o5) · [O6 Regulación de IA en MCSA](04_Nivel_4_Gobierno_y_operacion_continua.md#o6)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y repositorios](05_Comunidad.md#c2) · [C3 Recursos en español](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de la seguridad de Copilot y de los agentes? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para proteger, gobernar y auditar Microsoft 365 Copilot, Copilot Chat, los agentes que viven en Microsoft 365 y Copilot Studio: documentación de Microsoft Learn, avisos del Message Center, blogs y webinars de los equipos de producto, laboratorios oficiales, repositorios de GitHub y el trabajo de MVP y empleados de Microsoft. Todo está verificado al 6 de noviembre de 2026 y usa solo herramientas de Microsoft.

Es un programa transversal: lo recorren juntos quienes administran Microsoft 365 y Power Platform, protegen los datos, cuidan la identidad, operan el SOC y responden por el cumplimiento y la privacidad. Son 34 módulos y unas 184 horas en cuatro niveles, más una sección de comunidad. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, al estilo de los Ninja de Tech Community. Al terminar tendrás lo que pide un comité antes de ampliar Copilot y los agentes: evidencia de que los datos, las identidades, los agentes y las interacciones están bajo control.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal ni laboral: las decisiones sobre captura de prompts, monitoreo, retención y normativa corresponden a tus áreas de Legal, privacidad y RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

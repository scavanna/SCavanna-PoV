# Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026

*Del chat de seguridad al SOC agéntico: Security Copilot independiente y embebido, todos los agentes de Microsoft y de partners, promptbooks, plugins, Logic Apps, MCP, Copilot Studio y Foundry, con gobierno, costos y métricas de valor.*

> **Noviembre de 2026:** Security Copilot viene incluido en Microsoft 365 E5 y E7 (400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000), el inventario de esta edición registra 23 agentes de Microsoft (tres ya retirados) más los de partners del Security Store, la plataforma se extiende con agentes propios, MCP, Copilot Studio y Foundry, y Project Perception llegó al portal de Defender en vista previa limitada. Microsoft Ignite (17 al 20 de noviembre) puede cambiar estados: verifica antes de recomendar. ¿Vienes del Ninja de 2024? Empieza por [Qué cambió](00_Programa.md#cambios) y por el [inventario de agentes](00_Programa.md#inventario-agentes).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 30 | 4 + comunidad | 274 | ~146 | 159 | 60 | 22 |

**Para quién:** SOC agéntico, ingeniería de seguridad, automatización.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 8 módulos · ~31 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Security Copilot en cada rol · 7 módulos · ~35 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Extender y automatizar · 7 módulos · ~46 h · evaluación y reto del nivel |
| [04_Nivel_4_SOC_agentico.md](04_Nivel_4_SOC_agentico.md) | Nivel 4 · SOC agéntico · Del SOC tradicional al SOC agéntico · 5 módulos · ~31 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~3 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Security_Copilot_Ninja_Training_2026.html](Security_Copilot_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Security_Copilot_Ninja_Training_2026_Plan_y_catalogo.xlsx](Security_Copilot_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Prerrequisitos de IA](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 Qué es hoy](01_Nivel_1_Inicial.md#i1) · [I2 Licencias y capacidad](01_Nivel_1_Inicial.md#i2) · [I3 Experiencia independiente](01_Nivel_1_Inicial.md#i3) · [I4 Experiencias embebidas](01_Nivel_1_Inicial.md#i4) · [I5 Prompting para seguridad](01_Nivel_1_Inicial.md#i5) · [I6 Laboratorio y primeros usos](01_Nivel_1_Inicial.md#i6)
- **Nivel 2 · Intermedio · Security Copilot en cada rol:** [M1 SOC: triage e investigación](02_Nivel_2_Intermedio.md#m1) · [M2 Inteligencia de amenazas](02_Nivel_2_Intermedio.md#m2) · [M3 Identidad y acceso](02_Nivel_2_Intermedio.md#m3) · [M4 Endpoints y vulnerabilidades](02_Nivel_2_Intermedio.md#m4) · [M5 Datos y cumplimiento](02_Nivel_2_Intermedio.md#m5) · [M6 Agentes de Microsoft](02_Nivel_2_Intermedio.md#m6) · [M7 Gobierno, costos y auditoría](02_Nivel_2_Intermedio.md#m7)
- **Nivel 3 · Avanzado · Extender y automatizar:** [A1 Promptbooks personalizados](03_Nivel_3_Avanzado.md#a1) · [A2 Plugins: KQL, API, GPT, MCP](03_Nivel_3_Avanzado.md#a2) · [A3 Logic Apps](03_Nivel_3_Avanzado.md#a3) · [A4 Agentes personalizados](03_Nivel_3_Avanzado.md#a4) · [A5 MCP de Sentinel](03_Nivel_3_Avanzado.md#a5) · [A6 Power Platform/Copilot Studio](03_Nivel_3_Avanzado.md#a6) · [A7 Foundry y pro-code](03_Nivel_3_Avanzado.md#a7)
- **Nivel 4 · SOC agéntico · Del SOC tradicional al SOC agéntico:** [X1 Hacia el SOC agéntico](04_Nivel_4_SOC_agentico.md#x1) · [X2 Casos de uso, métricas y ROI](04_Nivel_4_SOC_agentico.md#x2) · [X3 Seguridad de IA y agentes](04_Nivel_4_SOC_agentico.md#x3) · [X4 Operar un parque de agentes](04_Nivel_4_SOC_agentico.md#x4) · [X5 Proyecto integrador](04_Nivel_4_SOC_agentico.md#x5)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y recursos en español](05_Comunidad.md#c2) · [C3 Mantenerse actualizado](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de Microsoft Security Copilot y llevar a tu SOC al modelo agéntico? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos —documentación de Microsoft Learn, anuncios de los equipos de producto, la Security Copilot Skilling Series, laboratorios oficiales, repositorios de GitHub y el trabajo de MVPs y empleados de Microsoft— y los convierte en un recorrido con práctica, evaluación y plan semanal.

Es el programa de integración de la serie: Security Copilot vive en Defender, Sentinel, Entra, Intune y Purview, y es la puerta hacia los agentes, MCP, Copilot Studio y Foundry. Cada nivel cierra con una evaluación y, si alcanzas el 80 %, puedes generar tu certificado de finalización, como en el Ninja oficial. El último nivel te acompaña en la transición del SOC tradicional al SOC agéntico, con métricas, gobierno y un proyecto integrador.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

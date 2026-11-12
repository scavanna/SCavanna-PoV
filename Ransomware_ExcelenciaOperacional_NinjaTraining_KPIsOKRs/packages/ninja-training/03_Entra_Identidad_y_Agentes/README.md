# Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026

*Identidad y acceso con Microsoft Entra de cero a experto: autenticación resistente al phishing, acceso condicional, identidad híbrida, PIM, gobernanza, identidades de carga de trabajo, ITDR y un track para preparar el tenant para agentes de IA.*

> **Noviembre de 2026:** las passkeys son el método predeterminado desde el 1 de septiembre y Microsoft deja de entregar SMS y voz en 2027; las políticas de riesgo heredadas de ID Protection se retiraron el 1 de octubre; Connect Sync exige la versión 2.6.84.0 antes del 7 de abril de 2027; y Entra Agent ID y Agent 365 están en disponibilidad general. ¿Tu organización se prepara para agentes de IA? Empieza por [Preparación del tenant para agentes de IA](00_Programa.md#preparacion-agentes), [Licencias de identidad](00_Programa.md#licencias) y [Qué cambió](00_Programa.md#cambios).

Fuentes verificadas al 6 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 31 | 4 + comunidad | 272 | ~225 | 163 | 59 | 15 |

**Para quién:** Identidad y acceso, arquitectura, gobierno de agentes.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos · 8 módulos · ~59 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Proteger, gobernar y observar · 8 módulos · ~70 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Cargas de trabajo, amenazas y arquitectura · 5 módulos · ~50 h · evaluación y reto del nivel |
| [04_Nivel_4_Identidad_para_agentes_de_IA.md](04_Nivel_4_Identidad_para_agentes_de_IA.md) | Nivel 4 · Identidad para agentes de IA · Preparar el tenant para agentes · 7 módulos · ~40 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Entra_Identidad_Ninja_Training_2026.html](Entra_Identidad_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Entra_Identidad_Ninja_Training_2026_Plan_y_catalogo.xlsx](Entra_Identidad_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos:** [P0 Protocolos y tokens](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender Entra](01_Nivel_1_Inicial.md#i0) · [I1 Entra hoy y licencias E5](01_Nivel_1_Inicial.md#i1) · [I2 Administración del tenant](01_Nivel_1_Inicial.md#i2) · [I3 Autenticación sin phishing](01_Nivel_1_Inicial.md#i3) · [I4 Acceso condicional esencial](01_Nivel_1_Inicial.md#i4) · [I5 Identidad híbrida](01_Nivel_1_Inicial.md#i5) · [I6 Laboratorios de práctica](01_Nivel_1_Inicial.md#i6)
- **Nivel 2 · Intermedio · Proteger, gobernar y observar:** [M1 Acceso condicional avanzado](02_Nivel_2_Intermedio.md#m1) · [M2 ID Protection](02_Nivel_2_Intermedio.md#m2) · [M3 PIM: roles, grupos y alertas](02_Nivel_2_Intermedio.md#m3) · [M4 Gobernanza y externos](02_Nivel_2_Intermedio.md#m4) · [M5 Apps y consentimiento](02_Nivel_2_Intermedio.md#m5) · [M6 Monitoreo y registros](02_Nivel_2_Intermedio.md#m6) · [M7 Dispositivos e identidad](02_Nivel_2_Intermedio.md#m7) · [M8 Global Secure Access](02_Nivel_2_Intermedio.md#m8)
- **Nivel 3 · Avanzado · Cargas de trabajo, amenazas y arquitectura:** [A1 Identidades de carga](03_Nivel_3_Avanzado.md#a1) · [A2 ITDR](03_Nivel_3_Avanzado.md#a2) · [A3 Identidad como código](03_Nivel_3_Avanzado.md#a3) · [A4 Arquitectura y privilegios](03_Nivel_3_Avanzado.md#a4) · [A5 Respuesta a incidentes](03_Nivel_3_Avanzado.md#a5)
- **Nivel 4 · Identidad para agentes de IA · Preparar el tenant para agentes:** [X1 Identidad: plano de control](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1) · [X2 Microsoft Entra Agent ID](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) · [X3 Acceso y permisos de agentes](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) · [X4 Ciclo de vida y Agent 365](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) · [X5 Security Copilot en Entra](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) · [X6 Copilot Studio y Foundry](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) · [X7 Proyecto: tenant para agentes](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y recursos en español](05_Comunidad.md#c2) · [C3 Mantenerse actualizado](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de identidad? Microsoft Entra no tiene un Ninja Training oficial, y esta guía llena ese hueco con el mismo espíritu: reúne, ordenados como un curso, los mejores recursos públicos para dominar la identidad y el acceso con Entra —documentación de Microsoft Learn, anuncios del equipo de producto, laboratorios oficiales, repositorios de GitHub y el trabajo de MVPs y empleados de Microsoft— y los convierte en práctica verificable en tu laboratorio.

La edición 2026 tiene un foco claro: preparar a tu organización para adoptar agentes de IA con la identidad como plano de control. Puedes recorrer los tres niveles y el track de agentes de principio a fin o saltar a la ruta de tu rol. Cada nivel cierra con una evaluación de conocimientos y un reto integrador; si alcanzas el 80 %, puedes generar tu certificado de finalización del nivel, como en los Ninja oficiales.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Seguridad de agentes de IA en Microsoft Foundry Ninja Training · Edición 2026

*Diseñar, construir, desplegar y operar agentes de IA seguros en Azure: Microsoft Foundry, Foundry Agent Service, Agent Framework, guardrails, API Management como AI gateway, red Zero Trust, datos, evaluaciones, observabilidad, detección y gobierno, sin depender de Agent 365.*

> **Noviembre de 2026:** el nuevo Foundry Agent Service (la «Agent Service v2» de la infografía) es GA desde el 16 de marzo; los agentes clásicos se retiran el 31 de marzo de 2027 y los workflows de Foundry, el 1 de diciembre de 2026. Los content filters ahora son guardrails, la detección de ataques en documentos sigue desactivada por defecto y, desde el 30 de septiembre, los prompts de las trazas van a la tabla protegida AppGenAIContent. Desde el 1 de julio, la postura y la detección de amenazas a nivel de agente en Defender exigen Agent 365, que queda **fuera de alcance**: aquí aprendes las alternativas incluidas en tus licencias. Microsoft Ignite (17 al 20 de noviembre) puede cambiar estados de vista previa. Empieza por la [infografía corregida](00_Programa.md#infografia-corregida), [qué cambió](00_Programa.md#cambios), la [frontera de licencias](00_Programa.md#licencias-frontera) y el [plan integrado](../Plan_Arquitectura_Segura_Agentes_IA_Azure.md).

Fuentes verificadas al 7 de noviembre de 2026 · Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026

| Módulos | Niveles | Recursos únicos | Horas estimadas | Ejercicios | Preguntas | Referentes |
|---|---|---|---|---|---|---|
| 28 | 4 + comunidad | 472 | ~151 | 188 | 60 | 29 |

**Para quién:** Arquitectura de IA, plataforma de Azure, desarrollo, seguridad de datos, SOC y gobierno de la IA.

## Cómo está organizada esta serie

| Archivo | Contenido |
|---|---|
| [00_Programa.md](00_Programa.md) | Cómo usar la guía, por qué este programa, formato Ninja, qué cambió, rutas por rol, plan de entrenamiento, laboratorio y mapa de módulos |
| [01_Nivel_1_Inicial.md](01_Nivel_1_Inicial.md) | Nivel 1 · Inicial · Fundamentos de la arquitectura segura · 7 módulos · ~32 h · evaluación y reto del nivel |
| [02_Nivel_2_Intermedio.md](02_Nivel_2_Intermedio.md) | Nivel 2 · Intermedio · Construir y desplegar con seguridad · 7 módulos · ~48 h · evaluación y reto del nivel |
| [03_Nivel_3_Avanzado.md](03_Nivel_3_Avanzado.md) | Nivel 3 · Avanzado · Probar, detectar y responder · 7 módulos · ~45 h · evaluación y reto del nivel |
| [04_Nivel_4_Gobierno_y_operacion.md](04_Nivel_4_Gobierno_y_operacion.md) | Nivel 4 · Gobierno y operación · Gobernar y operar la IA en Azure · 4 módulos · ~20 h · evaluación y reto del nivel |
| [05_Comunidad.md](05_Comunidad.md) | Comunidad · Referentes, canales y cómo mantenerse al día · 3 módulos · ~6 h |
| [06_Evaluaciones_y_respuestas.md](06_Evaluaciones_y_respuestas.md) | Todas las evaluaciones con respuesta correcta, explicación y fuente |
| [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md) | Qué se puede practicar en el laboratorio, qué solo en producción y cómo hacerlo con riesgo controlado; índice de ejercicios |
| [08_Cierre_glosario_y_fuentes.md](08_Cierre_glosario_y_fuentes.md) | Próximos pasos, glosario, metodología, fuentes y puntos a confirmar |
| [Seguridad_Agentes_IA_Foundry_Ninja_Training_2026.html](Seguridad_Agentes_IA_Foundry_Ninja_Training_2026.html) | Versión web interactiva: progreso, búsqueda y filtros, evaluaciones con corrección y certificado |
| [Seguridad_Agentes_IA_Foundry_Ninja_Training_2026_Plan_y_catalogo.xlsx](Seguridad_Agentes_IA_Foundry_Ninja_Training_2026_Plan_y_catalogo.xlsx) | Libro de Excel: plan de estudio con seguimiento y avance, plan semanal, ejercicios, catálogo con enlaces, hoja de respuestas, matriz de laboratorio, tablas de referencia, referentes y cambios |
| [Anexo_Entorno_de_practica.md](../Anexo_Entorno_de_practica.md) | Anexo común: cómo armar el entorno de práctica con los créditos de Visual Studio Enterprise y una prueba de Microsoft 365 E5 |

## Mapa de módulos

- **Nivel 1 · Inicial · Fundamentos de la arquitectura segura:** [P0 Modelos, RAG, agentes y MCP](01_Nivel_1_Inicial.md#p0) · [F0 Cómo usar y ruta integrada](01_Nivel_1_Inicial.md#f0) · [F1 Foundry por dentro](01_Nivel_1_Inicial.md#f1) · [F2 Arquitectura por capas](01_Nivel_1_Inicial.md#f2) · [F3 Modelado de amenazas](01_Nivel_1_Inicial.md#f3) · [F4 Identidad y acceso](01_Nivel_1_Inicial.md#f4) · [F5 Laboratorio seguro](01_Nivel_1_Inicial.md#f5)
- **Nivel 2 · Intermedio · Construir y desplegar con seguridad:** [M1 Agent Framework seguro](02_Nivel_2_Intermedio.md#m1) · [M2 Foundry Agent Service](02_Nivel_2_Intermedio.md#m2) · [M3 Guardrails y contenido](02_Nivel_2_Intermedio.md#m3) · [M4 APIM como AI gateway](02_Nivel_2_Intermedio.md#m4) · [M5 Red Zero Trust](02_Nivel_2_Intermedio.md#m5) · [M6 Datos y conocimiento](02_Nivel_2_Intermedio.md#m6) · [M7 Gobierno de modelos](02_Nivel_2_Intermedio.md#m7)
- **Nivel 3 · Avanzado · Probar, detectar y responder:** [A1 Evaluaciones y red teaming](03_Nivel_3_Avanzado.md#a1) · [A2 Observabilidad de agentes](03_Nivel_3_Avanzado.md#a2) · [A3 Defender for Cloud y Foundry](03_Nivel_3_Avanzado.md#a3) · [A4 Purview para Foundry](03_Nivel_3_Avanzado.md#a4) · [A5 Detección y respuesta](03_Nivel_3_Avanzado.md#a5) · [A6 Cadena de suministro de IA](03_Nivel_3_Avanzado.md#a6) · [A7 Multiagente y A2A](03_Nivel_3_Avanzado.md#a7)
- **Nivel 4 · Gobierno y operación · Gobernar y operar la IA en Azure:** [O1 Marcos y gobierno de la IA](04_Nivel_4_Gobierno_y_operacion.md#o1) · [O2 Modelo operativo y RACI](04_Nivel_4_Gobierno_y_operacion.md#o2) · [O3 FinOps y abuso de recursos](04_Nivel_4_Gobierno_y_operacion.md#o3) · [O4 Proyecto integrador](04_Nivel_4_Gobierno_y_operacion.md#o4)
- **Comunidad · Referentes, canales y cómo mantenerse al día:** [C1 Referentes](05_Comunidad.md#c1) · [C2 Canales y repositorios](05_Comunidad.md#c2) · [C3 Recursos en español](05_Comunidad.md#c3)

## Cómo empezar

¿Quieres convertirte en Ninja de la seguridad de agentes de IA en Azure? Esta guía te ayuda a llegar. Parte de una infografía muy difundida, «Secure Architecture for AI Agents — Microsoft Azure», la revisa capa por capa con fuentes públicas y la convierte en un curso: documentación de Microsoft Learn, arquitecturas de referencia del Azure Architecture Center, laboratorios oficiales en GitHub (AI-Gateway, Microsoft Agent Framework, PyRIT, AI Landing Zones y la arquitectura baseline de Foundry), blogs y videos de los equipos de producto y el trabajo de MVP y empleados de Microsoft. Todo está verificado al 7 de noviembre de 2026.

Es el programa complementario de la serie: enseña a fondo lo propio de Microsoft Foundry y de Azure —plataforma, Foundry Agent Service, Agent Framework, guardrails, API Management como AI gateway, red Zero Trust, datos, evaluaciones, observabilidad, cadena de suministro y multiagente— y solo los puntos de integración de lo que otros programas ya enseñan: Defender for Cloud, Purview, Entra, Sentinel, Defender XDR y Security Copilot. Son 28 módulos y unas 151 horas en cuatro niveles, más una sección de comunidad. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, al estilo de los Ninja de Tech Community. El último reto es el proyecto integrador: la arquitectura de la infografía, corregida y desplegada en tu laboratorio, con evidencia por capa.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD y sin impuestos, y cambian: confírmalos en la calculadora de precios de Azure antes de presupuestar. La infografía analizada pertenece a su autor y se usa solo como material de estudio. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal: las decisiones corresponden a tus áreas de Legal, privacidad y cumplimiento. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

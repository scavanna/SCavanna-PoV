# Análisis trazable del texto fuente

## Perfil de fuente

- **Localizador**: `Amenazas.md`, conservado como fuente original.
- **Tipo**: texto expositivo generado previamente; mezcla de taxonomía, ejemplos, matriz de gobierno y metodología.
- **Idioma**: español con terminología técnica en inglés; alta confianza.
- **Género**: mixto técnico y negocio–estrategia.
- **Propósito dominante**: explicar y proponer una arquitectura de trazabilidad.
- **Alcance**: ransomware, amenazas, riesgo, privacidad, ATT&CK, LINDDUN, modelado y priorización.
- **Exclusiones**: no contiene activos reales, apetito cuantitativo, probabilidades, datos de incidentes ni controles implantados.

## Segmentos normalizados

1. Taxonomía: actor, amenaza/evento, vulnerabilidad, activo y riesgo.
2. Catálogo macro: malware, identidad, web/API, DoS, insider, terceros, vulnerabilidades/configuración, físico/ambiental, fallos/errores, integridad/intercepción e IA.
3. Catálogos técnicos y de privacidad: ATT&CK y LINDDUN.
4. Gobierno: seis escenarios con controles, privacidad e indicadores.
5. Modelado: cuatro preguntas, métodos, priorización y validación.

## Afirmaciones materialmente útiles

| ID | Afirmación normalizada | Tipo | Estado |
|---|---|---|---|
| CLM-001 | Ransomware puede representarse como malware o comportamiento de impacto; por sí solo no expresa un escenario completo de riesgo. | Interpretación técnica | Conservada, matizada |
| CLM-002 | Un enunciado útil de riesgo identifica contexto, activo, evento, causas, consecuencia y horizonte. | Síntesis de riesgo | Conservada |
| CLM-003 | Las organizaciones no suelen disponer de una única lista universal; combinan catálogos ejecutivos, técnicos y de privacidad. | Recomendación analítica | Conservada |
| CLM-004 | ATT&CK describe comportamiento adversario; no es un registro corporativo de amenazas ni de riesgos. | Distinción de función | Conservada |
| CLM-005 | LINDDUN estructura amenazas de privacidad y necesita conectarse con base legal, titular, tratamiento y obligaciones. | Distinción de función | Conservada |
| CLM-006 | El modelado necesita definición del sistema, identificación, tratamiento y validación. | Proceso | Conservada |
| CLM-007 | Los resultados técnicos deben traducirse a exposición económica/operativa y trazarse a controles con evidencia. | Gobernanza | Conservada |

## Correcciones y precisiones

| ID | Texto a corregir | Tratamiento documental |
|---|---|---|
| CON-001 | “El ransomware se clasifica estrictamente como una amenaza” | Evitar “estrictamente”: ransomware es una clase de malware/ataque. `T1486` representa una técnica de cifrado con impacto, no todo ransomware ni un actor. Puede aparecer en el nombre abreviado de un escenario de riesgo sin ser ontológicamente el riesgo. |
| CON-002 | “Riesgo = probabilidad de que una amenaza explote una vulnerabilidad y su impacto” | Reformular según ISO 27005 como efecto de incertidumbre sobre objetivos o combinación de probabilidad/posibilidad y consecuencia. La existencia de una vulnerabilidad es una precondición frecuente, no una fórmula universal. |
| CON-003 | El catálogo de 11 categorías se presenta como completo/exhaustivo | Clasificarlo como catálogo semilla curado, no lista normativa ni exhaustiva. Añadir terrorismo, fraude, violaciones de cumplimiento, dependencias, errores de terceros y categorías emergentes según el contexto. |
| CON-004 | ISO/IEC 27005 “Anexo A” se usa como catálogo vigente | No presumir que ISO/IEC 27005:2022 contiene un catálogo de amenazas obligatorio en Anexo A. Usar la edición aplicable y fuentes internas licenciadas. |
| CON-005 | ATT&CK tiene cantidades fijas y “más de 200/400” | No fijar conteos: la base de conocimiento cambia. Registrar versión/fecha de extracción. |
| CON-006 | `LINDDUN` equivale a una lista completa de privacidad | Tratar sus siete tipos como lente de análisis. `Non-compliance` no sustituye inventario legal ni DPIA. Versiones recientes también refieren no intervención (`unawareness/unintervenability`). |
| CON-007 | “Sobre la amenaza no tienes control” | Es demasiado categórico. No siempre se controla el ecosistema, pero sí la capacidad, exposición, señales, disuasión, acuerdos, prueba de controles y respuesta. |
| CON-008 | Falta de control técnico eleva “automáticamente” el riesgo residual | La reevaluación requiere reglas, evidencia, umbrales y aprobación del propietario; no debe ser un automatismo narrativo. |
| CON-009 | MAESTRO se mezcla con OWASP/MITRE como si fuera la misma clase | MAESTRO es de CSA para IA agéntica; ATLAS es base MITRE; OWASP LLM Top 10 es catálogo de riesgos de aplicaciones LLM. Registrar funciones separadas. |
| CON-010 | CVSS + EPSS estima la probabilidad completa del riesgo | CVSS mide severidad técnica; EPSS estima probabilidad de explotación a corto plazo. Ninguno cuantifica por sí solo impacto empresarial, exposición específica ni pérdida anual. |

## Ambigüedades y lagunas

| ID | Ambigüedad/laguna | Acción requerida |
|---|---|---|
| AMB-001 | “Amenaza / evento” fusiona causa y ocurrencia | Separar `fuente amenaza`, `evento amenazante`, `escenario` e `incidente`. |
| AMB-002 | Controles se presentan como fórmulas probadas | Añadir dueño, alcance, modo, frecuencia, evidencia y última prueba. |
| AMB-003 | “72 h GDPR” no es una regla universal para todo contexto | Tratar plazos como obligación jurisdictional verificable; el timer se activa cuando se determine aplicabilidad. |
| GAP-001 | No se identifica sector, jurisdicción ni apetito | Parametrizar antes de usar el catálogo en decisiones. |
| GAP-002 | No hay inventario de activos o límites de confianza | Es obligatorio para el modelado técnico. |
| GAP-003 | No hay estimaciones ni datos de pérdida | FAIR y otras cuantificaciones requieren supuestos explícitos y calibración. |
| GAP-004 | No hay evidencia de controles ni estado de implantación | Marcar como `propuesto`, no `efectivo`. |

## Resultado del control de calidad

- Trazabilidad de afirmaciones: alta respecto del texto suministrado.
- Evidencia externa: limitada a referencias oficiales en `docs/05-marcos`; validar criterios legales y versiones antes de auditoría.
- Hallazgo principal: la fuente es una buena arquitectura conceptual inicial, pero contiene simplificaciones y afirmaciones que no deben convertirse en requisitos sin contexto.

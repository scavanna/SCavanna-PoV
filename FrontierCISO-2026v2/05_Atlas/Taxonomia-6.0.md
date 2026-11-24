# Taxonomía Frontier 6.0: consulta rápida

[Atlas](README.md) · [Biblioteca](../README.md)

La tabla consolida los códigos de la **6.0 confirmada**. Las glosas en español son ayudas de lectura, no nombres nuevos ni una nueva versión de la taxonomía.

## X · Territorios: desde dónde se mira

| Código | Perspectiva |
| --- | --- |
| `T01` | Criterio propio, juicio y metacognición. |
| `T02` | Liderazgo, personas, incentivos, autoridad y organización. |
| `T03` | Estrategia, resultados, negocio e inversión. |
| `T04` | Riesgo, exposición, apetito, continuidad y resiliencia. |
| `T05` | Arquitectura, controles, ingeniería y fronteras técnicas. |
| `T06` | Operación de seguridad, SOC, investigación y respuesta. |
| `T07` | IA, agentes, autonomía y autoridad no humana. |
| `T08` | Confianza, aseguramiento, evidencia y transparencia. |

## Y · Dominios: qué se está tratando

| Código | Objeto |
| --- | --- |
| `D01` | Gobierno de ciberseguridad: dirección, políticas y supervisión. |
| `D02` | Gestión, cuantificación, tratamiento y aceptación del riesgo. |
| `D03` | Cumplimiento de obligaciones legales, regulatorias y contractuales. |
| `D04` | Portafolio, presupuesto, prioridades e inversión en seguridad. |
| `D05` | Identidad, autenticación, autorización y gestión de privilegios. |
| `D06` | Clasificación, DLP, cifrado y protección de la información. |
| `D07` | Ingeniería de privacidad y protección de datos personales. |
| `D08` | Infraestructura, redes y segmentación. |
| `D09` | Dispositivos, puesto de trabajo, correo, colaboración y navegación. |
| `D10` | Nube, plataformas, cargas y configuraciones. |
| `D11` | Aplicaciones, software y ciclo de desarrollo seguro. |
| `D12` | Inteligencia y modelado de amenazas. |
| `D13` | Vulnerabilidades y exposición: activo, postura y reducción de brechas. |
| `D14` | Monitoreo, telemetría y detección. |
| `D15` | Respuesta a incidentes y coordinación de crisis. |
| `D16` | Continuidad y recuperación demostrada de servicios. |
| `D17` | Terceros, dependencias, concentración y cadena de suministro. |
| `D18` | Tecnología operacional y seguridad de procesos industriales. |
| `D19` | IoT y sistemas ciberfísicos no exclusivamente industriales. |
| `D20` | Protección de sistemas de IA y agentes, herramientas y datos. |
| `D21` | IA para defensa y operaciones de seguridad. |
| `D22` | IA como instrumento de evaluación y pruebas autorizadas. |
| `D23` | IA para crear reglas, políticas y automatización de seguridad. |
| `D24` | Profesión, talento, factores humanos y cultura. |
| `D25` | Arquitectura empresarial de seguridad y Zero Trust. |
| `D26` | Criptografía, claves, certificados, agilidad y transición poscuántica. |
| `D27` | Seguridad física, instalaciones, ambiente y soportes. |
| `D28` | Aseguramiento, medición, pruebas y evidencia de eficacia. |

## Z · Función y subfunciones: qué resultado se busca

| Función | Subfunciones del Atlas |
| --- | --- |
| `GV` · Gobernar | `GV01` contexto y estrategia; `GV02` autoridad; `GV03` políticas; `GV04` apetito y aceptación; `GV05` programas e inversión; `GV06` obligaciones; `GV07` supervisión y reporte; `GV08` aseguramiento independiente; `GV09` terceros; `GV10` ética y rendición. |
| `ID` · Identificar | `ID01` inventario/clasificación; `ID02` dependencias y criticidad; `ID03` amenazas y exposición; `ID04` escenarios y cuantificación; `ID05` capacidades y brechas. |
| `PR` · Proteger | `PR01` identidad/autorización; `PR02` datos y privacidad; `PR03` arquitectura segura; `PR04` desarrollo y cambios; `PR05` personas y procedimientos; `PR06` resiliencia de infraestructura y protección física/ambiental. |
| `DE` · Detectar | `DE01` observabilidad; `DE02` ingeniería de detección; `DE03` búsqueda y mejora; `DE04` cobertura y calidad. |
| `RS` · Responder | `RS01` preparación y coordinación; `RS02` contención y evidencia; `RS03` comunicación de crisis; `RS04` incidentes con terceros. |
| `RC` · Recuperar | `RC01` restauración técnica; `RC02` continuidad y modo degradado; `RC03` validación del retorno; `RC04` aprendizaje y mejora; `RC05` comunicación y restitución de confianza. |

## H · Evolución: qué está cambiando

`H01` fundacional, `H02` en evolución, `H03` emergente y `H04` convergente. En 6.0 los cuatro son horizontes. Elegir uno no implica progresión, superioridad ni una calificación de madurez. Los restantes elementos del eje —catalizadores, inhibidores, mecanismos, contexto y variables— se consultan en el catálogo, con el estado del modelo a la vista.

## Criterios para casos con más de un dominio

- Si el caso aplica una disciplina a un objeto —por ejemplo, gobierno de IA— clasificá por la disciplina (`D01`) y dejá el objeto como secundario (`D20`). Si trata del control técnico sobre el objeto, ese objeto es primario.
- Si evalúa el **método** de prueba o medición, usá `D28`; si mide la eficacia de un control concreto, el dominio del control es primario. Si la pregunta es conformidad con una obligación, distinguí `D03` de la gestión general de evidencia.
- La arquitectura de referencia se clasifica en `D25`. El control que la concreta pertenece al dominio de su objeto. En un acceso Zero Trust distinguí quién accede (`D05`) de por dónde se conecta (`D08`).
- Elegí la subfunción después de decidir el resultado y revisala si cambia el dominio. No trasplantes una regla o un código de la 6.1 candidata.

[Catálogo 6.0 en CSV](artefactos/taxonomia_v6_0_catalogo.csv), con código, nombre, definiciones y alcance.

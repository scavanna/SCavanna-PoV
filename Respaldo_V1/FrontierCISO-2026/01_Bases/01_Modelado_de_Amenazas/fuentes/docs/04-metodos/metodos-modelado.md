# Métodos de modelado de amenazas

## Principio de selección

No existe un método único “correcto”. Combinar un enfoque de sistema, uno de atacante/riesgo y uno de privacidad cuando corresponda, manteniendo el mismo escenario y trazando cada conclusión a evidencia.

## Proceso base

Las cuatro preguntas del Threat Modeling Manifesto son útiles como ciclo: qué se construye, qué puede fallar, qué se hará y si la respuesta funciona. Para producción documental, añadir propietarios, supuestos, evidencia y cadencia.

1. Describir sistema, activos, usuarios, datos, dependencias, fronteras y objetivos.
2. Identificar amenazas, abuso y fallos con una lente estructurada.
3. Priorizar escenarios y definir tratamiento.
4. Verificar requisitos, controles y riesgo residual.

## Métodos y artefactos

| Método/artefacto | Tipo y foco | Salida | Usar cuando | No sustituye |
|---|---|---|---|---|
| STRIDE | lente por elemento de software | amenazas S/T/R/I/D/E por elemento | DFD, API, app, cloud, integraciones | cuantificación, privacidad completa, modelado de atacante |
| PASTA | proceso de siete etapas centrado en riesgo/ataque | escenarios y análisis alineados al negocio | regulación, impacto y decisiones complejas | evidencia de control ni estándar de riesgo |
| Attack trees | descomposición jerárquica AND/OR | rutas a un objetivo adversario | escenarios críticos o ciberfísicos | cobertura global automática |
| Abuse/misuse cases | conducta no autorizada orientada a objetivos | casos de abuso, requisitos negativos | funcionalidades con usuario/negocio | análisis de toda arquitectura |
| OCTAVE/asset-centric | evaluación organizacional | activos, prácticas, riesgos | programas y procesos de negocio | DFD detallado o técnica de detección |
| VAST | modelado escalable app/operación | vistas de aplicación y operación | DevSecOps a escala | taxonomía universal |
| TRIKE | requisitos, usuarios, activos y aceptabilidad | matriz de acceso/riesgo | auditoría y autorización | inteligencia de amenaza completa |
| LINDDUN | privacidad por tipos/árboles | amenazas de privacidad y mitigaciones | DPIA, datos personales, inferencia | análisis legal completo |
| MAESTRO | IA agéntica en capas | amenazas y propagación entre capas | agentes, herramientas, memoria, modelos | evaluación técnica ATT&CK/ATLAS completa |
| Data-flow diagrams | artefacto de arquitectura | elementos, flujos, almacenes, límites | casi todo sistema técnico | método de enumeración |
| ATT&CK | base de conocimiento de comportamiento | técnicas, grupos, software, mitigaciones/detecciones | SOC, emulación, detección | registro de riesgo o método por sí solo |
| CAPEC | patrones de ataque | mecanismos y atributos de ataque | AppSec, pruebas, traducción de debilidades | riesgo empresarial |
| ATLAS | conocimiento adversario para IA/ML | técnicas/estudios de ataque IA | modelos, pipelines, sistemas IA | método empresarial general |
| DREAD | puntuación cualitativa histórica | score de cinco factores | triage simple con cautela | decisión de inversión defensiva |
| CVSS | severidad técnica de vulnerabilidad | vector/base/temporal/ambiental | priorizar vulnerabilidades | probabilidad de riesgo o impacto negocio |
| EPSS | probabilidad estimada de explotación | score y percentil a 30 días | priorizar exposición de CVE | impacto y probabilidad de escenario completo |
| FAIR | modelo de factores y cuantificación | frecuencia, magnitud, pérdida anual | comparar inversión y escenarios | método para descubrir amenazas |
| NIST 800-30 / ISO 27005 | proceso de evaluación/gestión del riesgo | contexto, análisis, tratamiento, seguimiento | integrar resultados al ERM/ISMS | manual de modelado de arquitectura |

## STRIDE: cautelas

Aplicar STRIDE por elemento y conexión del DFD, no como lista global. La letra E (“Elevation of Privilege”) no es sinónimo de todo incidente de identidad. Repudiation se relaciona con trazabilidad y evidencia; no toda exigencia de no repudio es igual en privacidad, donde la negabilidad puede ser deseable.

## PASTA en siete etapas

1. Definir objetivos, alcance y criterios.
2. Definir arquitectura técnica.
3. Descomponer aplicación/sistema.
4. Analizar amenazas e inteligencia.
5. Analizar vulnerabilidades y debilidades.
6. Modelar/analizar ataques.
7. Analizar y gestionar riesgo residual.

## Combinaciones recomendadas

| Contexto | Combinación mínima |
|---|---|
| Aplicación/API | DFD + STRIDE + OWASP/CAPEC + CVSS/EPSS donde aplique |
| Programa/activo crítico | OCTAVE/ISO 27005 + PASTA o attack trees + FAIR si hay decisión económica |
| Identidad/fraude | abuse cases + ATT&CK + controles IAM/antifraude |
| Privacidad | data map/DFD + LINDDUN + DPIA y requisitos legales |
| SOC/validación | ATT&CK + detecciones + Purple Team/BAS + evidencia de control |
| Agente de IA | arquitectura por capas + MAESTRO + ATLAS + LINDDUN + STRIDE/abuse cases |
| Terceros | modelo de confianza/dependencia + cadena de suministro + SLA/evidencia |

## Salida mínima aceptable

- Diagrama/modelo versionado.
- Activos, fronteras, supuestos y cambios.
- Amenazas/casos de abuso con ID.
- Escenario causa–evento–consecuencia.
- Decisión de tratamiento y dueño.
- Requisitos y controles con prueba.
- Riesgo inherente/residual y fecha.
- Hallazgos, excepciones y siguiente revisión.

## Antipatrones

- Modelar solo vulnerabilidades o CVEs.
- Usar ATT&CK como lista exhaustiva de amenazas.
- Registrar “ransomware” como riesgo sin activo/impacto.
- Puntuar sin criterios ni evidencia.
- Confundir diseño de control con operación efectiva.
- Realizar una sola sesión y nunca actualizarla.
- Copiar requisitos de privacidad sin mapear tratamientos ni titulares.

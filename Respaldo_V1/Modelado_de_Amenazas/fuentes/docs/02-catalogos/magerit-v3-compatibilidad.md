# Núcleo MAGERIT v3 y ampliaciones no oficiales

## Posición del repositorio

**Adaptación NO OFICIAL.** MAGERIT v3 es el estándar de oro interno por origen, lenguaje, estructura de amenazas y criterios de valoración. El repositorio no reemplaza ni reinterpreta la metodología oficial: conserva sus códigos y añade capas externas de detalle, tecnología, privacidad, IA y gobierno.

## Catálogo base verificado

La tabla de contenidos del **Libro II: Catálogo de Elementos** de MAGERIT v3 lista 57 entradas de amenazas:

- 3 de desastres naturales (`N`), incluidas `N.*` genérica.
- 12 de origen industrial (`I`), incluidas `I.*` genérica.
- 18 de errores/fallos no intencionados (`E`).
- 24 de ataques intencionados (`A`).

De ellas, 55 corresponden a entradas con código numérico y 2 son categorías comodín (`N.*`, `I.*`). Por ello, afirmar que son “cerca de 30” depende de la edición, selección o agregación utilizada; no coincide con las 57 entradas publicadas en el índice de MAGERIT v3. Los comodines no deben contabilizarse como un nuevo mecanismo específico de amenaza.

El listado exacto de entrada se conserva en `data/magerit-v3-amenazas.csv`.

## Regla de compatibilidad

| Nivel | Identificador | Regla |
|---|---|---|
| MAGERIT oficial | `[N/E/I/A].<n>` | No modificar código, familia, nombre ni semántica. |
| Agrupación temática moderna | `DOM-*` | Puede agrupar varias amenazas MAGERIT sin sustituirlas. |
| Ampliación no oficial | `EXT-*` | Namespace separado; solo se usa si no encaja sin pérdida en MAGERIT. |
| Escenario organizativo | `RS-*` | Combina activos, evento, dependencias, degradación e impacto. |
| Técnica externa | ID de origen | ATT&CK/CAPEC/ATLAS/OWASP conservan su ID y versión. |
| Caso de uso | `UC-*` | Actividad de mantenimiento, modelado o validación. |

No reutilizar numeraciones MAGERIT para amenazas nuevas. Una extensión debe declarar el código MAGERIT base más próximo, la justificación para no forzarlo y un mapeo inverso.

## Extensiones del estado del arte

Las nuevas capacidades pueden extender el catálogo sin romper su núcleo:

- ransomware, wiper, supply-chain compromise y doble extorsión como especializaciones/escenarios;
- phishing, AitM, robo de sesión y abuso de identidad;
- API, nube, secretos, identidad federada, SaaS y dependencias OSS;
- IA/ML y agentes: prompt injection, poisoning, extracción, tool misuse, memoria y agencia excesiva;
- privacidad: linking, identifying, detecting, disclosure, unawareness/unintervenability;
- eventos climáticos, concentración regional y dependencia crítica del ecosistema;
- fraude digital, abuso de lógica, desinformación y manipulación de decisiones;
- amenazas a control plane, repositorios, pipelines CI/CD y telemetry.

## Dimensiones y valoración MAGERIT

La adaptación mantiene la valoración MAGERIT por activo, amenaza y dimensión. Cualquier equivalencia con CIA o con impacto económico se documenta como proyección adicional, no como sustitución de la escala original.

Campos preservados o compatibles:

- activo y dependencias;
- dimensión degradada;
- amenaza y origen;
- probabilidad/frecuencia;
- impacto acumulado/repercutido;
- riesgo inherente y residual;
- salvaguardas, eficacia y tratamiento;
- responsabilidad y evidencia.

## Uso didáctico con ransomware

La guía `docs/07-guia-didactica/guia-metodologia-ransomware.md` muestra cómo transformar el núcleo MAGERIT en escenarios, controles, playbooks y decisiones. Los ejemplos empresarial y OT no asignan los códigos de forma automática: los validan contra activos, precondiciones, evidencia y consecuencias.

## Algoritmo de clasificación

1. Intentar asignar una o más amenazas MAGERIT sin forzar equivalencias.
2. Si hay una especialización moderna, conservar el código MAGERIT base y registrar el detalle externo (`MAGERIT_base` + `external_mapping`).
3. Si no existe base razonable, crear `EXT-*`, dejando el mapeo MAGERIT vacío y explicando la razón.
4. Formular el escenario `RS-*` con activo/proceso, dependencia, evento, degradación y consecuencia.
5. Valorar primero con MAGERIT; añadir traducciones ejecutivas/FAIR/LINDDUN/ATT&CK como capas.
6. Registrar versión de cada fuente externa y evidencia de aplicabilidad.

## Ejemplo: ransomware

- Núcleos MAGERIT posibles: `[A.8] Difusión de software dañino`, `[A.11] Acceso no autorizado`, `[A.18] Destrucción de información`, `[A.19] Divulgación de información`, `[A.29] Extorsión`, y `[A.24] Denegación de servicio` según escenario.
- Extensión: `EXT-001 Ransomware moderno/doble extorsión`.
- Técnica: ATT&CK `T1486` como comportamiento de impacto, más técnica de acceso/movimiento/exfiltración comprobada.
- Riesgo: degradación de servicio ERP/negocio y pérdida financiera, no “ransomware” aislado.

## Fuentes oficiales

- Portal PAe MAGERIT: https://administracionelectronica.gob.es/documentacion/metodologias-guias/pae-magerit
- Libro I · Método, MAGERIT v3: enlace oficial publicado desde el portal PAe.
- Libro II · Catálogo de Elementos, MAGERIT v3: https://administracionelectronica.gob.es/content/dam/pae/pae-home/documentos/documentacion/metodologias-y-guias/mageritv3/2012_Magerit_v3_libro2_catalogo-de-elementos_es_NIPO_630-12-171-8.pdf

Fecha de consulta: 2026-11-18. La vigencia, interpretación y aplicabilidad deben verificarse frente al ENS y los textos oficiales vigentes en el momento de uso.

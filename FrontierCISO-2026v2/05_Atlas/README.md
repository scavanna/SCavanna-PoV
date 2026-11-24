# Atlas: ubicar un problema sin confundir versiones

[Biblioteca](../README.md) · [Taxonomía Frontier 6.0](Taxonomia-6.0.md)

El Atlas ayuda a describir un problema y encontrar conocimiento, no a certificar que una práctica funciona. Usá **Frontier Taxonomía 6.0** para una clasificación nueva: es la base confirmada por el autor que pudo verificarse. Mantené **AI CISO Atlas 5.3** cuando una fuente o un cruce ya está expresado en 5.3.

| Si necesitás… | Usá… | Límite |
| --- | --- | --- |
| Clasificar un caso nuevo para trabajo CISO | Frontier 6.0: 8 territorios, 28 dominios, 6 funciones, 34 subfunciones editoriales y cuatro horizontes. | La taxonomía no acredita la corrección de un mapeo ni equivalencia con un estándar. |
| Interpretar una referencia Atlas 5.3, como el comparativo Microsoft por dominio | Handoff v6 FINAL: estructura 5.3 y documentación de Core Ontology 1.0. | El cierre documenta una ontología propuesta. El catálogo canónico de 32 subfunciones de 5.3 no está reproducido íntegramente en el handoff. No rellenarlo desde 6.0. |
| Consultar un grafo o un corpus clasificado como referencia | Conservar el alcance de la fuente y exigir revisión de la relación antes de usarla como hecho. | Frontier 1.4, la taxonomía 6.1, la ontología 2.2.0 y su grafo se revisaron como **candidatos**, no se adoptan en esta edición. |

## Clasificá un caso

1. **X · Territorio.** Elegí la perspectiva de responsabilidad. Nombrar IA en el texto no basta para una clasificación como sistemas autónomos.
2. **Y · Dominio.** Elegí el objeto principal. Si evaluás una obligación, la conformidad es distinta de probar eficacia técnica. Si definís política para agentes, separá el gobierno de la protección del agente y sus herramientas.
3. **Z · Resultado.** Elegí función y subfunción por lo que buscás lograr. Los códigos de subfunción del Atlas son editoriales: no son los identificadores oficiales de subcategorías NIST CSF.
4. **H · Evolución.** Explicá qué mueve o estabiliza la práctica y si es fundacional, en evolución, emergente o convergente. H no es una escala de madurez.
5. **Contraste.** Guardá referencia, versión, justificación y la evidencia que haría cambiar la coordenada. Si la fuente no alcanza, marcá el eje incierto; no lo completes por simetría.

**Ejemplo ficticio:** demostrar que facturación vuelve con datos íntegros después de una interrupción. Perspectiva `T04` Riesgo y resiliencia; objeto `D16` Continuidad y recuperación; resultado `RC03` Validación de recuperación y retorno seguro. `H01` solo si estamos describiendo una práctica consolidada; si el problema es incorporar dependencias de IA, describí ese cambio antes de elegir H.

| Objeto y versión | X · Y · Z · H | Justificación y referencia | Alternativa o incertidumbre | Revisor |
| --- | --- | --- | --- | --- |
| | | | | |

## Separá el dato de la interpretación

- **Taxonomía** asigna coordenadas; **ontología** define entidades y relaciones; **corpus** contiene textos y evidencia; **grafo** materializa afirmaciones que requieren revisión. No son versiones del mismo archivo.
- Una relación propuesta no es un hecho. Para reutilizarla se requiere fuente, tipo y dirección de la relación, confianza y aprobación humana. No hagas migraciones implícitas entre 5.3 y 6.0.
- No leas como una sola colección los **739** elementos categorizados en el Atlas candidato, los **379** pre-ensayos GM-24 V7.1, ni los **1.404** elementos de la biblioteca cognitiva.

## Catálogos locales

| Si necesitás… | Abrí… |
| --- | --- |
| Buscar coordenadas de la base Frontier confirmada | [Catálogo Frontier 6.0 en CSV](artefactos/taxonomia_v6_0_catalogo.csv), complementario a la [consulta rápida](Taxonomia-6.0.md). |
| Interpretar una coordenada 5.3 ya publicada | [Estructura 5.3 del handoff v6](artefactos/taxonomy_v5_3_structure.json). No completa el catálogo canónico de las 32 subfunciones. |
| Ver tipos admitidos y sus relaciones en el handoff | [Core Ontology 1.0](artefactos/ontology.json), [diccionario de entidades](artefactos/entity_dictionary.json) y [diccionario de relaciones](artefactos/relationship_dictionary.json). Son referencias del modelo documentado, no un motor ni un grafo aprobado. |

Para ubicar conocimiento y evaluar formación, ver [Desarrollo profesional](../06_Desarrollo-CISO/README.md).

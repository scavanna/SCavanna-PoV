# Modelado de amenazas · MAGERIT v3 ampliado

Edición de trabajo con corte al **18 de noviembre de 2026**. Es una adaptación **no oficial**: conserva los códigos de MAGERIT y separa las extensiones de esta colección. Las matrices sirven para diseñar y verificar controles, no para certificar cobertura.

## Cómo modelar y tratar un escenario

1. **Delimitá el servicio.** Identificá dueño, activos, flujos y dependencias. Usá la [guía de método](fuentes/docs/07-guia-didactica/guia-metodologia.md) y elegí una [lente de modelado](fuentes/docs/04-metodos/metodos-modelado.md) acorde con la decisión.
2. **Formulá el riesgo.** Describí causa, condición, evento e impacto. Una amenaza como ransomware no es por sí sola un riesgo. Para el vocabulario y su aplicación, usá el [glosario](fuentes/docs/01-dominio/glosario.md) y los [criterios de compatibilidad MAGERIT](fuentes/docs/02-catalogos/magerit-v3-compatibilidad.md).
3. **Elegí el tratamiento.** Consultá la categoría y los IDs de amenaza aplicables. Recorré las cuatro fases: **I** inventario, **P** prevención y protección, **D** detección y **R** respuesta y recuperación.
4. **Comprobá y decidí.** Registrá prueba, evidencia, dueño y riesgo residual. Si no hay evidencia o fecha, registrá la brecha en lugar de declarar el control eficaz. La [matriz de gobierno](fuentes/docs/06-gobierno/matriz-gobierno.md) ayuda a asignar quién decide y quién verifica.

## Catálogos y matrices

| Si necesitás… | Usá… |
| --- | --- |
| Agrupar la exposición | [Guía de las 15 categorías](fuentes/docs/02-catalogos/catalogo-amenazas.md), [CSV de categorías](fuentes/data/amenazas.csv) y [matriz de ciclo por categoría](fuentes/docs/09-estado-del-arte/01-categorias-15/matriz-estado-del-arte-15-categorias.xlsx). |
| Registrar amenazas con su ID | [57 entradas MAGERIT](fuentes/data/magerit-v3-amenazas.csv), incluidos dos comodines, y [22 extensiones](fuentes/data/extensiones-amenazas.csv), identificadas aparte. La [matriz ampliada](fuentes/docs/09-estado-del-arte/02-magerit-v3-ampliado/matriz-estado-del-arte-magerit-v3-ampliado.xlsx) cubre las cuatro fases de los 79 IDs. |
| Ver el tratamiento y su prueba | [Tratamiento por categoría y amenaza](integracion_ABC/tratamiento-por-categoria-y-amenaza.csv), [cobertura por fase y hoja de Excel](Cobertura_Fases_Verificada.csv) y [alcance de la validación documental](fuentes/docs/09-estado-del-arte/VALIDACION.md). Los CSV se abren en Excel o en un editor de datos. |
| Elegir una actividad práctica | [16 casos de uso](fuentes/data/casos-uso.csv) y [guía de actividades y entregables](fuentes/docs/03-casos-uso/casos-uso.md). Son actividades genéricas; no hay una correspondencia nominal 1:1 con las 79 amenazas. |
| Evaluar una capacidad Microsoft | [Mapeo de amenazas a capacidades](fuentes/docs/09-estado-del-arte/02-magerit-v3-ampliado/microsoft/mapeo-microsoft-magerit-v3-ampliado.xlsx) y [catálogo de 43 capacidades](fuentes/docs/09-estado-del-arte/03-capacidades-microsoft/catalogo-capacidades-microsoft.xlsx). Confirmá licencia, entorno, autorización y eficacia antes de adoptarlas. |

## Plantillas y ejemplos

- **Registro:** [esquema](fuentes/data/schema-registro.yaml), [ficha de análisis MAGERIT](fuentes/templates/plantilla-analisis-magerit.yaml), [matriz activo–amenaza](fuentes/templates/matriz-activo-amenaza.csv) y [registro de salvaguardas](fuentes/templates/registro-salvaguardas.csv).
- **Respuesta:** [playbook genérico](fuentes/templates/playbook-generico.yaml) y [plantilla defensiva de ransomware](fuentes/templates/playbook-ransomware.yaml). Son plantillas de documentación, no automatizaciones.
- **Ransomware:** [guía metodológica](fuentes/docs/07-guia-didactica/guia-metodologia-ransomware.md), [escenario YAML](fuentes/data/escenario-ransomware.ejemplo.yaml), [mapa multivista](fuentes/data/mapa-ransomware-multivista.csv), [caso empresarial híbrido](fuentes/docs/08-ejemplos/ransomware-empresa-hibrida.md) y [caso industrial OT](fuentes/docs/08-ejemplos/ransomware-ot-industrial.md). No sustituyen un plan de respuesta aprobado ni las decisiones de seguridad física.
- **Referencias:** [marcos y organizaciones](fuentes/docs/05-marcos/marcos-organizaciones.md), [tabla de métodos](fuentes/data/metodos.csv), [fuentes por ID](fuentes/data/referencias.csv) y [gobernanza de las extensiones](fuentes/docs/02-catalogos/adaptacion-no-oficial.md).

El criterio de selección deja fuera la fuente de discusión inicial, su revisión preliminar, los generadores y los índices de directorio sin contenido propio. Esta edición se consulta sin ejecutar código ni volver a la carpeta original.

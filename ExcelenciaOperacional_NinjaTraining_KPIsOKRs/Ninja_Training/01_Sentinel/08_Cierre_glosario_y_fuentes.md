# Cierre, glosario y fuentes

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja no es un estado, es un hábito. Sentinel, Defender y Security Copilot publican novedades cada semana: dedica media hora semanal a las páginas de novedades y al blog de Sentinel, mira los webinars que te interesen y vuelve a esta guía cuando necesites profundizar.

Si encuentras un enlace roto, un dato desactualizado o un recurso que debería estar aquí, anótalo y compártelo con tu equipo: la guía está pensada para mantenerse viva con revisiones periódicas, como el Ninja original. Para preguntas técnicas, la comunidad de Sentinel en Tech Community, Microsoft Q&A y la Microsoft Security Community son los mejores lugares.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| AMA | Azure Monitor Agent: agente que recolecta datos de Windows y Linux mediante reglas de recolección de datos. |
| ASIM | Advanced Security Information Model: esquemas y parsers de normalización en tiempo de consulta. |
| Agent Loop | Capacidad de Azure Logic Apps para crear flujos de agente autónomos o conversacionales con modelos de IA. |
| CCF | Codeless Connector Framework: marco para crear conectores sin código (antes Codeless Connector Platform). |
| Content hub | Catálogo de soluciones de Sentinel con conectores, reglas, libros, búsquedas y playbooks. |
| Custom detection | Detección personalizada del portal de Defender sobre datos de Sentinel y Defender XDR; camino recomendado para reglas nuevas. |
| Data lake | Nivel de almacenamiento económico de Sentinel, con retención de hasta 12 años y consultas KQL y Spark. |
| DCR / DCE | Regla de recolección de datos y punto de conexión de recolección de Azure Monitor. |
| Entra Agent ID | Tipo de identidad de Microsoft Entra para agentes de IA. |
| GDAP | Granular Delegated Admin Privileges: delegación granular de administración entre tenants. |
| Incident case | Experiencia de gestión de casos del portal de Defender que agrupa incidentes, tareas, SLA y auditoría. |
| KQL | Kusto Query Language: lenguaje de consulta de Sentinel, Defender y Azure Data Explorer. |
| KQL job | Trabajo programado que consulta el data lake y escribe resultados en una tabla. |
| MCP | Model Context Protocol: estándar abierto para que los agentes de IA descubran y usen herramientas. |
| MTO | Gestión multi-inquilino (multitenant organization) del portal de Defender. |
| NRT | Near real time: reglas que se ejecutan cada minuto. |
| Playbook | Flujo de Azure Logic Apps que automatiza la respuesta a incidentes, alertas o entidades. |
| Promptbook | Secuencia reutilizable de prompts de Security Copilot. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot. |
| Search job | Búsqueda asíncrona sobre datos archivados o de largo plazo. |
| Security Store | Tienda de Microsoft para agentes y soluciones de seguridad de Microsoft y partners. |
| SOAR | Orquestación, automatización y respuesta de seguridad. |
| STIX / TAXII | Estándares para expresar e intercambiar inteligencia de amenazas. |
| Summary rule | Regla que agrega datos de forma programada en una tabla resumida. |
| UEBA | Análisis de comportamiento de usuarios y entidades. |
| URBAC | Control de acceso basado en roles unificado del portal de Defender. |
| Workbook | Libro interactivo de visualización basado en Azure Monitor Workbooks. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Contradicciones entre páginas oficiales señaladas en el texto: soporte de grupos GDAP en el RBAC unificado, requisito de licencia del conector de inteligencia de amenazas, estado de ASIM en la tabla de disponibilidad, métodos de autenticación del conector de Security Copilot y disponibilidad de Project Perception.
- Algunas páginas de Learn todavía mencionan julio de 2026 como fin del portal de Azure; la fecha vigente es el 31 de marzo de 2027.
- La exploración de datos del servidor MCP en tenants incorporados después del 23 de septiembre de 2026 se reportó con problemas en la comunidad y debe probarse en cada tenant.
- Las fechas de algunos videos de YouTube son aproximadas y el estado de MVP de algunos autores no pudo confirmarse; en esos casos se los etiqueta como comunidad.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

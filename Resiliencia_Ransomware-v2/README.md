# Resiliencia ante ransomware · preparación y respuesta

Kit defensivo de la **edición integrada v2.0 (12 de noviembre de 2026)**, con un único índice operativo. Adaptá el mandato, los contactos de emergencia, los requisitos de continuidad y los plazos a tu organización. **La seguridad de las personas prevalece y ningún artefacto autoriza cambios por sí solo.**

## Elegí la tarea y el libro

| Tarea | Herramienta local | Qué dejar resuelto |
| --- | --- | --- |
| Preparar el plan y la línea base | [01 · Evaluación y controles](resiliencia_v2/01-Evaluacion-y-controles.xlsx), hojas `BIA`, `Controles`, `Evaluaciones` y `Plan`. | Servicios críticos, RTO/RPO, dueño y suplente, dependencias, brecha, prueba y fecha. |
| Ejecutar la respuesta o un ensayo | [02 · Operación y pruebas](resiliencia_v2/02-Operacion-y-pruebas.xlsx), hojas `Incidentes`, `Decisiones`, `Evidencia`, `Comunicaciones`, `Pruebas` y `Competencias`. | Autoridad, cronología UTC, alcance, efecto verificado, custodia, recuperación y aceptación. |
| Priorizar por sector y preparar al equipo | [03 · Correlación de prioridades, Microsoft y Ninja](resiliencia_v2/03-Correlacion-Prioridades-FullMS-Ninja.xlsx), hojas `Prioridades_Sector_365`, `Matriz_Controles_360`, `Matriz_SOC_IR_360` y `Rutas_Ninja_Roles`. | Prioridades contrastadas con la BIA, responsables, procedimiento de referencia y práctica evaluable para titular y suplente. |

El libro 03 usa el **Plan CISO 365 v1.0** y **KPI/OKR v1.2**. No se reemplazan sus IDs por los del Plan Frontier v2.0 ni se afirma una equivalencia. El [catálogo JSON](resiliencia_v2/Catalogo-correlacion-v2.json) conserva los datos de correlación; la [guía de mapeo](resiliencia_v2/13-Mapeo-canonico-y-prioridades.md) explica su alcance. El [Plan CISO de Frontier v2 de 90/365 días](../FrontierCISO-2026v2/01_Gobierno-CISO/README.md) es una referencia complementaria, no un requisito para usar los libros de resiliencia.

## Desde la preparación hasta el retorno

1. **Preparar y evaluar.** [Mandato y activación](resiliencia_v2/01-Gobierno.md), [evaluación inicial y trimestral](resiliencia_v2/02-Evaluaciones.md) y [controles, evidencias y plan](resiliencia_v2/03-Controles-y-plan.md). Probá canales fuera de banda y no des por recuperable un servicio solo porque existen copias.
2. **Detectar, decidir y contener.** [Monitoreo y triaje](resiliencia_v2/04-Monitoreo-y-triage.md), [tarjetas PB-01 a PB-07](resiliencia_v2/05-Respuesta-y-repudio.md#3-tarjetas-de-contención) y [tarjetas breves por rol](resiliencia_v2/10-Tarjetas-de-respuesta.md). Usá el [formulario F3](resiliencia_v2/12-Formularios.md#f3-orden-de-contención--repudio) y registrá el efecto comprobado, no solo la orden.
3. **Preservar, recuperar y comunicar.** [Cadena de custodia](resiliencia_v2/06-Evidencia-y-forense.md), [continuidad y recuperación](resiliencia_v2/07-Continuidad-y-recuperacion.md) y [comunicaciones de crisis](resiliencia_v2/08-Comunicaciones.md). Reconectá únicamente después de comprobar integridad, medir tiempo y pérdida de datos y obtener aceptación de negocio; si falla algo, registrá la brecha.
4. **Ensayar y sostener.** [Pruebas E1–E3 y métricas](resiliencia_v2/09-Pruebas-y-metricas.md), [operación Full Microsoft](resiliencia_v2/14-Operacion-Full-Microsoft.md) y [formación y recursos por rol](resiliencia_v2/15-Plan-de-entrenamiento-y-recursos.md). La cobertura se demuestra con pruebas autorizadas, no con una licencia, una lectura o un resultado de curso.

**Prepará una copia fuera de banda** de los [formularios operativos](resiliencia_v2/12-Formularios.md) y las tarjetas. Guardá incidentes, evidencias y contactos reales en un repositorio aprobado y restringido, no en Git.

## Derechos de decisión

Estos códigos orientan el formulario: la autoridad efectiva la establece el mandato local. Si una misma intervención requiere más de una decisión, registralas por separado con persona, alcance y hora UTC.

| Código | Decisión | Referencia de autoridad |
| --- | --- | --- |
| `DD10` | Declarar incidente mayor. | CISO; un proveedor puede recomendar, no declarar por la organización. |
| `DD11` | Aislar o desconectar un servicio crítico. | CEO o comité ejecutivo según umbrales preautorizados; CISO y CIO/CTO coordinan. |
| `DD12` | Notificar a autoridades o afectados. | Legal, Cumplimiento y Privacidad determinan obligación y plazo; CISO aporta hechos. |
| `DD13` | Autorizar comunicación pública de crisis. | CEO, con revisión de Legal y CISO; Comunicaciones gestiona el mensaje. |
| `DD14` | Activar continuidad o recuperación ante desastres. | CEO en el modelo de referencia; CIO/CTO coordina con CISO y negocio. |
| `DD18` | Autorizar o suspender la autoridad delegada de un agente. | Dueño de negocio; CIO/CTO ejecuta con intervención de CISO y Legal. |

Para otros `DD##` citados en `Matriz_SOC_IR_360` sin definición en el capítulo de [gobierno](resiliencia_v2/01-Gobierno.md), no deduzcas la autoridad: anotá «sin equivalencia confirmada» y registrá el mandato local. Por ejemplo, `PB-07` orienta la respuesta ante un agente comprometido y `DD18` registra la decisión de suspenderlo; eso no autoriza por sí solo la desconexión de un servicio crítico (`DD11`).

## Visores para consultas y ejercicios

Abrí los HTML en un navegador, manteniendo juntas las carpetas del kit. Son herramientas locales: **no ejecutan contención ni notifican a terceros**.

- [Panel de resiliencia](resiliencia_v2/Panel-de-resiliencia.html): consulta de controles y preparación.
- [Consola local de incidente](resiliencia_v2/Consola-de-incidente.html): registro de decisiones y evidencia durante un ejercicio o una respuesta autorizada.
- [Mapa de correlación y prioridades](resiliencia_v2/Mapa-de-correlacion-y-prioridades.html): cruce por sector, fase, tecnología y formación.

[Fuentes públicas y límites de cobertura](resiliencia_v2/11-Fuentes-y-cobertura.md). Se conservan los capítulos de operación, los tres Excel, los tres visores y el catálogo. Se quitan el índice intermedio y el inventario de elaboración, sin sustituir los archivos que se necesitan para trabajar.

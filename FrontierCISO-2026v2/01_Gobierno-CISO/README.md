# Gobierno del CISO: recibir, medir, decidir

[Biblioteca](../README.md) · [Registro de gestión para copiar](Registro-de-gestion.md)

**Base:** Modelo Operativo CISO 365 Frontier v2.0, rev. 2 (15 de noviembre de 2026). Es un modelo para calibrar, independiente del proveedor. La edición Microsoft aporta una capa de implementación; no cambia el modelo.

## Primeros 90 días y plan de 365: hojas de trabajo

| Libro local | Cómo usarlo |
| --- | --- |
| [Diagnóstico v2.0](artefactos/Frontier_CISO_Atlas_CISO365_Diagnostico_v2.0.xlsx) | Fijá fecha y alcance en `Parámetros`. Completá `Funciones`, `Zero Trust`, `Pila y cobertura` y `Servicios externalizados`. Usá `Resultados` para cerrar la línea base al día 60. |
| [Plan anual y OKR v2.0](artefactos/Frontier_CISO_Atlas_CISO365_Plan_Anual_y_OKR_v2.0.xlsx) | A partir del diagnóstico, definí hitos en `Calendario` y `Puertas`, resultados en `OKR` y su dotación y presupuesto. Revisá `Resumen OKR` al cierre de los días 90, 180, 270 y 365. |
| [KPI y tablero v2.0](artefactos/Frontier_CISO_Atlas_CISO365_KPIs_y_Tablero_v2.0.xlsx) | Seleccioná los indicadores en `Catálogo`, completá `Medición` y consultá el tablero correspondiente a directorio, dirección o tecnología. |
| [KPI/OKR v1.2: perfiles y cruces anteriores](artefactos/AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx) | Consultá `Catalogo_KPI`, `KPI_Sistema_Gestion`, `Paquetes_Sector`, `OKR_Anio1` y `Plan365_Integracion` para entender los cruces que usan esa edición, como el de ransomware. No es el tablero del Plan Frontier v2.0. |

El esquema anterior usaba **H100**; el Plan Frontier usa **H90** y **H365**. El libro `Plan anual y OKR v2.0` conserva la hoja `Actividades v1.0` para interpretar referencias anteriores. Para planificación nueva, usá `Calendario` y `OKR` de v2.0, no una mezcla de hitos. Los cuatro libros están en esta colección; trabajá sobre una copia para cada organización.

## 1. Establecé una línea base en los primeros 60 días

| Ventana orientativa | Acción | Evidencia para aceptar el resultado |
| --- | --- | --- |
| Días 1–10 | Recibir personas, presupuesto, contratos, compromisos y riesgos. Delimitar entornos y servicios críticos. | Acta de recepción, inventario de entornos y contratos; dueño de la recepción. |
| Días 11–30 | Revisar las 59 funciones: 12 de gobierno, 12 de gestión y 35 servicios de operación. Asignar dueño y modelo de provisión. | Cobertura declarada por función y entorno, último artefacto verificable, responsable y fecha. |
| Días 21–40 | Evaluar la postura Zero Trust y contrastar la pila tecnológica con el alcance real. | Matriz de los 42 criterios, brechas y controles que se solapan. Los seis criterios de IA son de base provisional. |
| Días 31–50 | Contrastar los servicios externalizados con sus compromisos y capacidad de salida. | Anexo de servicio, evidencia verificable, responsable interno y ruta de transición probada cuando corresponda. |
| Días 41–60 | Medir indicadores de partida, acordar riesgos prioritarios y pedir decisiones al sponsor. | Línea base reproducible, lista de prioridades con dueño, plan del primer ciclo y decisiones a tomar. |

Los rangos se solapan. **Una función sin dueño no supera el nivel 1.** Tampoco se califica como implementado lo que no se pudo ver. Para afirmar «probado», el modelo pide una prueba, ejercicio o revisión independiente dentro de los últimos 12 meses.

Asigná criticidad de 1 a 3. Como punto de partida, el nivel objetivo es 3 para funciones críticas y 2 para las demás. Ordená por `máx(0, nivel objetivo − nivel observado) × criticidad`, sin dejar que el puntaje tape una exposición urgente. Una función inexistente, o crítica con nivel 0–1, se trata desde el primer ciclo. Registrá qué dato haría cambiar la prioridad.

## 2. Goberná cuatro ciclos, no una lista anual de proyectos

| Ciclo | Resultado | Antes de cerrarlo |
| --- | --- | --- |
| 1 · Días 1–90 · Conocer, estabilizar y ordenar | H30: acta de recepción; H60: diagnóstico base; H90: informe, mandato y plan. | Validar dueño, línea base, decisión y presupuesto para cada prioridad. Tratar exposiciones que no pueden esperar. |
| 2 · Días 91–180 · Adecuar | H180: sistema de gobierno operando. | Acordar apetito, políticas y controles por entorno; revisar contratos, dotación y cadencias. |
| 3 · Días 181–270 · Evolucionar y probar | H270: capacidades probadas. | Exigir resultados de pruebas de control, respuesta y recuperación; documentar excepciones y volver a probar las fallas críticas. |
| 4 · Días 271–365 · Demostrar y sostener | H365: rendición anual y decisiones para el siguiente año. | Mostrar tendencia, exposición residual y evidencia; decidir qué sostener, cambiar o externalizar. |

El modelo ofrece **24 objetivos y 72 resultados clave** en seis frentes: gobierno, programa/personas/presupuesto, identificar/proteger, detectar/responder/recuperar, ecosistema e IA/agentes. Usalos como repertorio: elegí un resultado por problema prioritario y definí un indicador, o un hito binario con criterio de aceptación. No uses una lista de tareas terminadas como indicador de reducción del riesgo.

## 3. Medí solo lo que cambie una decisión

El catálogo de 224 indicadores no es un tablero. Partí de la audiencia y de la decisión que debe tomar:

| Audiencia | Decisión | Evidencia útil |
| --- | --- | --- |
| Directorio y síndicos | Aceptar riesgo residual, financiar un tratamiento o cambiar el apetito. | Exposición fuera del apetito, concentración en terceros, pruebas de recuperación y efectividad de controles. |
| Dirección ejecutiva | Asignar presupuesto, resolver dependencias y sostener el plan. | Avance de resultados clave, impacto en el negocio, costo total y opción recomendada. |
| Tecnología y operación | Corregir una brecha y comprobar el efecto. | Cobertura por entorno, población y evidencia de prueba; salud de telemetría y plazos de corrección. |

Para cada KPI registrá **definición, población, fuente, dirección de mejora, línea base, meta, periodicidad y dueño**. Si falta el denominador o la medición no es confiable, registrá «sin datos», no cero. Si la línea base ya satisface una meta propuesta, pactá una meta más exigente o tratala como indicador de sostenimiento.

Para una función externalizada, elegí la variante del resultado clave y exigí **resultado medido, evidencia verificable y salida**. En co-gestión, medí el resultado propio y seguí aparte la obligación del proveedor. El contrato transfiere ejecución, no rendición de cuentas.

## Anexos y conexiones

- [Catálogo estructurado del Plan v2.0](artefactos/Frontier_CISO_Atlas_CISO365_Catalogo_v2.0.json): funciones, resultados y definiciones de indicadores para consultar por ID o para integrar a otras herramientas.
- [Desarrollo y cruce GM-24](../06_Desarrollo-CISO/GM24-unidades.md) · [Capa Microsoft](../03_Operacion-y-formacion-Microsoft/README.md).

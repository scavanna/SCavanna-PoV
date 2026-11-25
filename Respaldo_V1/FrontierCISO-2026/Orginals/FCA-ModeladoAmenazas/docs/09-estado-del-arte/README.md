# Estado del arte: mitigación por ciclo de amenaza

Fecha de corte: **2026-11-18**.

Este paquete responde a cuatro preguntas para cada registro:

1. **Identificación/inventario**: qué activos pueden verse afectados y qué debe inventariarse.
2. **Prevención/protección**: qué medidas reducen la probabilidad o degradación.
3. **Detección**: qué telemetría, controles o procesos permiten saber si ocurre.
4. **Respuesta/recuperación**: cómo contener, erradicar, recuperar y aprender.

> “Estado del arte” significa un baseline razonado para diseño y evaluación. No equivale a cobertura garantizada, lista exhaustiva ni obligación normativa. Debe contextualizarse por activos, sector, jurisdicción, arquitectura, licencia y evidencia.

## Paquetes

- `01-categorias-15/`: evaluación y Excel para las 15 categorías agregadas.
- `02-magerit-v3-ampliado/`: evaluación y Excel para las 57 entradas MAGERIT v3 más 22 extensiones no oficiales.
- `02-magerit-v3-ampliado/microsoft/`: mapeo Microsoft por las 79 amenazas y cuatro fases.
- `03-capacidades-microsoft/`: catálogo transversal de capacidades Microsoft, fuentes Learn y reglas de validación.

## Resultado de la validación previa

No existía el modelo de cuatro fases completo ni uniforme para los dos universos. La auditoría y las correcciones están documentadas en `VALIDACION.md`.

## Criterio de auditoría

El resultado se considera completo únicamente si cada registro tiene 4 filas de ciclo de vida y su respuesta declara activos, controles, evidencia, pruebas y límites. Una tecnología es una capacidad candidata, no una mitigación comprobada.

## Nota sobre los puntos 3 y 4 del encargo

Se interpreta el cuarto punto, que repite el tercero, como una segunda vista complementaria: un **catálogo transversal de capacidades Microsoft** y una **matriz requisito–producto** además del mapeo individual por amenaza. Ambas se entregan en este paquete.

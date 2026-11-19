# 09 — Mantenimiento y evolución

## Cadencias

- Por ChangeSet: validación, revisión y trazabilidad.
- Mensual durante el piloto: duplicados, relaciones rechazadas, warnings y cobertura de evidencia.
- Trimestral: revisión de mapeos externos, reglas y competency questions.
- Por release: migración, changelog, pruebas de regresión y snapshot.

## Versionado

- Patch: definición o regla aclarada sin cambiar compatibilidad.
- Minor: nuevo tipo/relación compatible.
- Major: cambio de significado, obligatoriedad o migración incompatible.
- Taxonomía, ontología, agente y currículo se versionan por separado.

## Métricas

- Tasa de ChangeSets válidos al primer intento.
- Violaciones por regla SV.
- Relaciones sin evidencia/contexto.
- Duplicados confirmados y falsos positivos.
- Extensiones propuestas/aprobadas/rechazadas.
- Acuerdo entre revisores de clasificación.
- Cobertura de competency questions.

## Deuda conocida

- Sincronizar el catálogo exacto de 32 subfunciones desde la fuente v5.3.
- Completar mapeos externos a nivel de elemento con fuente/versión.
- Mejorar calidad de evidencia, deduplicación y contradicciones.
- Definir migraciones para relaciones preexistentes.
- Implementar rollback y pruebas de aplicación transaccional más completas.
- Validar la ontología con los primeros tres ensayos antes de procesar los 120.

## Criterio para considerar RDF/OWL

Evaluar solo si hay un caso medido de interoperabilidad semántica, razonamiento formal, SHACL/OWL, federación de grafos o escala/concurrencia que SQLite no satisfaga.

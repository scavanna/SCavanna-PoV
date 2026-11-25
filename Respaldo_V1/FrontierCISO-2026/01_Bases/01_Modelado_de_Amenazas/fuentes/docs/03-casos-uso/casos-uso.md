# Catálogo de casos de uso y actividades

## Ciclo principal

1. **Preparar**: alcance, patrocinio, criterios, roles y fuentes.
2. **Descomponer**: procesos, activos, datos, interfaces, fronteras y dependencias.
3. **Identificar**: actores, amenazas, abuso, fallos, privacidad y cadenas de ataque.
4. **Analizar**: aplicabilidad, precondiciones, consecuencias y escenarios.
5. **Priorizar**: apetito, criticidad, exposición, incertidumbre y evidencia.
6. **Tratar**: evitar, reducir probabilidad, reducir consecuencia, transferir o aceptar.
7. **Verificar**: arquitectura, pruebas, purple team, ejercicios, telemetría y recuperación.
8. **Gobernar**: propietarios, excepciones, cadencia, registro residual y lecciones.

## Catálogo de actividades

| ID | Caso de uso | Disparador | Entradas | Resultado verificable | Responsables sugeridos |
|---|---|---|---|---|---|
| UC-001 | Definir alcance y criterios | Nuevo sistema/cambio mayor | objetivos, arquitectura, contexto | charter, apetito, exclusiones | CISO, negocio, arquitectura, DPO |
| UC-002 | Inventariar activos y procesos | Inicio/actualización | inventarios, CMDB, data map | activos con dueño/criticidad | asset owners, arquitectura |
| UC-003 | Dibujar DFD y trust boundaries | Arquitectura disponible | DFD, IAM, APIs, datos | modelo versionado con fronteras | arquitectura, appsec |
| UC-004 | Modelar amenazas de sistema | Nuevo diseño | UC-002/003 + método | amenaza–escenario–control | threat modeler, equipo producto |
| UC-005 | Modelar privacidad | Tratamiento personal nuevo | flujo de datos, finalidad, base | hallazgos LINDDUN/DPIA | DPO, privacidad, producto |
| UC-006 | Modelar proveedor/tercero | Alta o cambio proveedor | contrato, arquitectura, SBOM | escenario compartido y SLA | terceros, legal, seguridad |
| UC-007 | Modelar IA/agentes | Diseño o cambio de agente | herramientas, memoria, datos, permisos | mapa MAESTRO/ATLAS/LLM y abuso | AI security, ingeniería, DPO |
| UC-008 | Crear escenario ejecutivo | Amenaza material o cambio | contexto + impacto | riesgo en lenguaje de negocio | riesgo, CISO, finanzas, negocio |
| UC-009 | Cuantificar pérdida | Decisión de inversión | frecuencia, magnitud, controles | rango/distribución ALE | FAIR/risk analyst, finanzas |
| UC-010 | Diseñar controles | Amenaza priorizada | escenarios, requisitos, arquitectura | control y prueba definidos | arquitectura, ingeniería |
| UC-011 | Mapear comportamiento | Integrar threat intel/SOC | ATT&CK/CAPEC, telemetría | coberturas y gaps | SOC, detection engineering |
| UC-012 | Verificar controles | Release/cadencia | plan de prueba, evidencia | resultado y defecto | assurance, red/purple team |
| UC-013 | Probar continuidad | Simulacro/ventana crítica | RTO/RPO, runbooks | tiempo real y hallazgos | resiliencia, operaciones |
| UC-014 | Revaluar riesgo residual | Control o evidencia cambia | hallazgos, KRIs, incidentes | decisión y fecha | owner de riesgo/comité |
| UC-015 | Revisar registro | Cadencia/disparador | backlog de escenarios | decisiones, obsolescencias | risk office, CISO, DPO |

## Plantilla mínima de caso de uso

```yaml
id: UC-000
name: <verbo + objeto>
objective: <decisión o resultado>
trigger: <evento o cadencia>
scope: <incluido/excluido>
inputs: []
activities: []
roles:
  accountable: <dueño>
  responsible: []
  consulted: []
  informed: []
outputs: []
acceptance_criteria: []
evidence: []
metrics: []
exceptions: <proceso de aprobación>
next_review: YYYY-MM-DD
```

## Criterios transversales

- Registrar supuestos y contradicciones, no solo amenazas “confirmadas”.
- Separar recomendación, diseño, implantación y efectividad operativa.
- Mantener enlaces versionados a técnicas y estándares.
- No cerrar una amenaza por ausencia de detecciones; probar cobertura y plausibilidad.
- Incluir fallos accidentales, dependencia física, fraude y privacidad cuando sean relevantes.
- Repetir el modelado cuando cambia arquitectura, frontera, actor, datos, herramienta o contexto regulatorio.

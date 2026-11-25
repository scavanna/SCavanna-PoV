# Cultura, clientes, socios y proveedores

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 11 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. El plan no es solo técnico

Un plan que asigna dueños, mide comportamientos y revisa contratos cambia la forma de trabajar dentro de la organización y la relación con quienes están fuera. Esos cambios no ocurren solos: cada uno necesita una decisión explícita y alguien que la tome.

## 2. Cultura

| Dimensión | Impacto | Decisión requerida | Quién decide | Etapa |
|---|---|---|---|---|
| Cultura | Reportar sin culpa aumenta lo que la organización ve. | Adoptar la regla de reporte sin sanción para los errores de buena fe. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Cultura | Usar IA exige reglas simples y conocidas. | Aprobar la política de uso de IA y difundirla. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Cultura | La dirección se entrena para decidir en una crisis. | Participar en un ejercicio de crisis por semestre. | Directorio y síndicos · CEO, CFO y comité ejecutivo | Ciclo 1 |
| Cultura | La seguridad pasa a ser un objetivo de los ejecutivos. | Incluir objetivos de ciberseguridad en la evaluación de los ejecutivos. | Directorio y síndicos · CEO, CFO y comité ejecutivo | Ciclo 2 |
| Cultura | La seguridad entra antes del diseño, no al final. | Exigir la revisión de arquitectura antes de la puesta en producción. | CIO y CTO | Ciclo 2 |

- **Qué cambia.** La seguridad deja de ser un área que autoriza o prohíbe y pasa a ser un conjunto de responsabilidades repartidas: cada proceso y cada activo crítico tiene un dueño de riesgo.
- **Cómo se sostiene.** Con objetivos de ciberseguridad en la evaluación de los ejecutivos, formación por función y una red de referentes.
- **Cómo se mide.** Por comportamientos, no por horas de capacitación.

| ID | Indicador de cultura | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|
| K09 | Procesos y activos críticos con dueño de riesgo designado | 40 · 60 · 80 · 95 |
| K10 | Ejecutivos con objetivos de ciberseguridad en su evaluación | 10 · 30 · 60 · 90 |
| K11 | Comportamiento seguro: tasa de reporte de phishing | 10 · 25 · 45 · 65 |

## 3. Clientes

| Dimensión | Impacto | Decisión requerida | Quién decide | Etapa |
|---|---|---|---|---|
| Clientes | Un incidente obliga a informar a los clientes en plazos breves. | Aprobar el criterio y el procedimiento de notificación a clientes. | Directorio y síndicos · CEO, CFO y comité ejecutivo | Ciclo 1 |
| Clientes | Los clientes piden evidencia de seguridad. | Definir qué evidencia se entrega, a quién y con qué frecuencia. | CEO, CFO y comité ejecutivo | Ciclo 2 |
| Clientes | Los requisitos contractuales de seguridad condicionan las ventas y las renovaciones. | Asignar un dueño a los requisitos de seguridad de los contratos con clientes. | CEO, CFO y comité ejecutivo | Ciclo 2 |

Los clientes piden cada vez más evidencia de seguridad: cuestionarios, cláusulas, certificaciones y derecho de auditoría. El plan permite responder con datos del propio tablero en lugar de armar cada respuesta desde cero. El indicador K23 mide los requisitos de seguridad de clientes y contratos cumplidos.

## 4. Socios

| Dimensión | Impacto | Decisión requerida | Quién decide | Etapa |
|---|---|---|---|---|
| Socios | Las integraciones con socios abren accesos. | Exigir identidad propia, privilegio mínimo y registro en toda integración. | CIO y CTO | Ciclo 2 |
| Socios | La información compartida con socios necesita reglas. | Acordar con cada socio la clasificación y el tratamiento de lo que se comparte. | CEO, CFO y comité ejecutivo | Ciclo 3 |

## 5. Proveedores

| Dimensión | Impacto | Decisión requerida | Quién decide | Etapa |
|---|---|---|---|---|
| Proveedores | Aparecen cláusulas nuevas: auditoría, notificación, datos, subcontratación, salida e IA. | Aprobar las cláusulas mínimas para los contratos nuevos y las renovaciones. | CEO, CFO y comité ejecutivo | Ciclo 1 |
| Proveedores | Los contratos pasan a medirse por resultados. | Renegociar los contratos críticos con niveles de servicio por resultado y evidencia. | CEO, CFO y comité ejecutivo · CIO y CTO | Ciclo 2 |
| Proveedores | La dependencia de un proveedor es un riesgo que se decide. | Fijar el límite de concentración por proveedor. | Directorio y síndicos | Ciclo 2 |
| Proveedores | Todo servicio crítico debe poder dejarse. | Ensayar la salida de los servicios críticos. | CIO y CTO | Ciclo 3 |

El cambio más visible para los proveedores es que se los gobierna por resultados y se los verifica. Eso incluye a los proveedores de tecnología cuyos contratos administra otra área. El documento 06 «Funciones externalizadas: cómo gobernarlas y medirlas» tiene las comprobaciones y las cláusulas.

| ID | Indicador de terceros | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|
| K27 | Servicios críticos concentrados en un proveedor sin alternativa | 50 · 30 · 15 · 5 |
| KX01 | Servicios externalizados con dueño interno designado | 60 · 80 · 95 · 100 |
| KX03 | Cumplimiento de los niveles de servicio | 70 · 85 · 95 · 99 |
| KX14 | Funciones críticas concentradas en un mismo proveedor | 60 · 45 · 30 · 20 |

## 6. Cómo comunicar el cambio

| A quién | Qué necesita oír | Documento |
|---|---|---|
| CIO y CTO | Qué se les pide, qué reciben a cambio y cómo se reparte la propiedad de los controles. | Frontier_CISO_Atlas_CISO365_12_Narrativa_CIO_y_CTO_v2.0.md |
| CEO, CFO y comité ejecutivo | Qué riesgo se asume, cuánto cuesta, qué estructura hace falta y cómo se rinde cuentas. | Frontier_CISO_Atlas_CISO365_13_Narrativa_CEO_y_CFO_v2.0.md |
| Directorio y síndicos | Qué deben supervisar, qué decisiones les corresponden y qué evidencia van a recibir. | Frontier_CISO_Atlas_CISO365_14_Narrativa_Directorio_y_Sindicos_v2.0.md |
| Dueños de proceso y equipos | Qué responsabilidad les toca y cómo se mide. | Cadencias RT01 y RT03 |
| Proveedores | Qué evidencia se les va a pedir y con qué frecuencia. | Frontier_CISO_Atlas_CISO365_06_Funciones_Externalizadas_v2.0.md |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

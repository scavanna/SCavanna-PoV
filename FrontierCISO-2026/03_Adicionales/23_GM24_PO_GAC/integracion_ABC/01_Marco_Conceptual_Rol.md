# 01 · Marco conceptual del rol: Product Owner de control y gerente de agentes cognitivos (PO-GAC)

> **GM-24 V7.1 · Sub-plan PO-GAC** · 2026-11-14. Documento narrativo del sub-plan (no generado desde datos). Referencias DD/K4x/R/eo:OP/COE: marco interno (CISO 365 / AI CISO Atlas).

## 1. Qué es un producto-control

Un producto-control es un control de seguridad tratado como producto: tiene un **objetivo** expresado como resultado (funciones y categorías de NIST CSF 2.0), un **alcance** (un dominio Zero Trust: identidades, endpoints, aplicaciones, datos, infraestructura, red, productividad y colaboración, o el pilar transversal de visibilidad y automatización), una **tecnología** que lo realiza (en el escenario de este sub-plan, Defender for Office 365 dentro de Defender XDR) y un **modelo operativo** que lo mantiene efectivo (cadencias, evidencia, KPIs, mejora). La fórmula *función CSF × dominio Zero Trust × tecnología × modelo operativo* define el producto y, por lo tanto, su dueño.

La idea no es nueva en gestión de productos digitales; lo nuevo es aplicarla a controles de seguridad, que históricamente se "implementan" y luego se abandonan (M1.1-K05). El owner responde por la cadena **objetivo → configuración → evidencia** (M3.2-PA01) y por su backlog, su presupuesto y su retiro.

## 2. Qué es un gerente de agentes cognitivos

Los agentes cognitivos son software que percibe, razona con un modelo y actúa a través de herramientas, con un grado de autonomía configurable. Para el SOC son una tercera clase de trabajador junto a personas y proveedores. Gestionarlos exige lo que exige gestionar cualquier fuerza de trabajo —asignar tareas, dar autoridad acotada, supervisar, evaluar, desarrollar, retirar— más lo que exige gestionar software crítico: identidad propia, permisos mínimos, versionado, pruebas, observabilidad y continuidad.

El gerente de agentes (GAC) es responsable de la **flota** de agentes de su producto-control: su registro, fichas, autonomía, costo, desempeño, riesgos e incidentes. No construye necesariamente los agentes (puede hacerlo un equipo de plataforma o un proveedor), pero responde por ellos ante el dueño del riesgo y ante el CISO.

## 3. Por qué el rol es dual

Separar al owner del control del gerente de sus agentes produce agentes sin dueño de negocio o controles sin automatización gobernada. Unirlos en una persona (o en un rol con dos facetas) garantiza que quien decide qué debe lograr el control decide también qué puede delegarse a un agente y bajo qué límites. El rol es dual porque el trabajo es dual: especialista del dominio (sabe qué protege y cómo) y manager de una fuerza híbrida (sabe quién o qué lo hace y con qué autoridad).

## 4. De analista a PO-GAC: la transición

| Dimensión | Analista | PO-GAC |
|---|---|---|
| Unidad de trabajo | La tarea (triar, investigar, remediar) | El producto (objetivo, backlog, evidencia) y el trabajo de otros (humanos, agentes, proveedores) |
| Autoridad | Ejecuta dentro de procedimientos | Decide configuración, excepciones, autonomía L0–L3, aprobaciones L2; propone al dueño del riesgo lo que excede |
| Medición | SLA, volumen | KPIs del control, KRIs de la flota, costo por tarea, valor demostrado |
| Relación con la IA | Usuario de asistentes | Dueño de agentes: ficha, identidad, permisos, evaluación, revisión de desempeño, retiro |
| Relación con la dirección | Indirecta | Reporte trimestral del producto-control y de la fuerza híbrida |

## 5. Principios del rol

1. **Lo específico de Microsoft es implementación; lo agnóstico, base.** Cada capacidad tiene una base (estándar, práctica, marco) y una implementación en el escenario (Defender, Sentinel, Copilot Studio, Foundry, Agent 365, Entra Agent ID, Purview).
2. **Capacidad ≠ permiso ≠ delegación ≠ ejecución** (HC-010). Que un agente pueda hacer algo no significa que tenga permiso; que tenga permiso no significa que esté delegado; que esté delegado no significa que deba ejecutarlo sin aprobación.
3. **Nunca tratar contenido procesado como instrucción.** El agente de un SOC lee contenido hostil por diseño; la defensa es limitar lo que puede hacer con él (AMP-41).
4. **Un kill switch no probado no existe** (AMP-44). **Una reversibilidad no probada no existe** (AMP-21).
5. **Los mapeos a marcos son referencias informativas, no equivalencias** (AMP-08).
6. **El contenido V4 del GM-24 no se modifica**; el sub-plan agrega, instancia y relaciona.

## 6. Escala de autonomía

| Nivel | Definición | Condición mínima |
|---|---|---|
| L0 | Solo informa | Ficha + identidad de lectura |
| L1 | Propone; el humano ejecuta | + evaluación de calidad |
| L2 | Propone y ejecuta tras aprobación humana registrada | + límites de lote, kill switch probado, red teaming |
| L3 | Ejecuta acciones reversibles y de bajo impacto con auditoría posterior por muestreo | + KRIs con umbrales, revisión trimestral, ATO |
| L4 | Autónomo con límites estrictos | No previsto en este sub-plan |

## 7. Los dos planos del proyecto

El GM-24 (plano A) es el corpus académico: conceptos-lección, pre-ensayos, competencias y mapeo a estándares; es independiente del proveedor. Las instancias de dominio (plano B: Productividad, XDR, Endpoints, Identidades, Datos, SIEM, Nube) son el uso del corpus como marco para gobernar y gestionar capacidades que un CISO contrató; cambian con la plataforma y con las licencias. Nada del plano B modifica el plano A.

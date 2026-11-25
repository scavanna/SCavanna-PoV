# 00 · Plan de trabajo y decisiones — Sub-plan PO-GAC (V7.1)

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Objetivo
Itinerario para que un analista de ciberseguridad evolucione a **Product Owner de un control de seguridad (PO)** y **gerente de agentes cognitivos (GAC)** integrados en un SOC, sin pilotear agentes, dentro de las 24 unidades del GM-24 y sobre su base de 331 pre-ensayos.

## 2. Horas
- 42 conceptos PA nuevos: **178 h**. Lente PO-GAC sobre 91 conceptos existentes: **175 h**. Práctica guiada y capstone: **91 h**. Total: **444 h**.
- Envolvente de referencia: 50 h/unidad (1200 h); reescalado a 800 h pendiente (D07).

## 3. Distribución por unidad
| Unidad | Título | PA (n) | PA (h) | Lente (n) | Lente (h) |
|---|---|---|---|---|---|
| G1.1 | Principios de Gobierno, Contexto Organizacional y Arquetipos CISO | 1 | 4 | 2 | 4 |
| G1.2 | Desarrollo de Estrategia y Alineación con el Negocio | 1 | 4 | 4 | 6 |
| G2.1 | Selección e Integración de Marcos y Estándares | 2 | 10 | 2 | 3 |
| G2.2 | Ciclo de Vida de Políticas, Estándares y Procedimientos | 3 | 12 | 3 | 5 |
| G3.1 | Requisitos Legales, Regulatorios y Contractuales | 1 | 3 | 2 | 4 |
| G3.2 | Gestión del Cumplimiento y Aseguramiento Continuo | 1 | 4 | 4 | 6 |
| G4.1 | Gobernanza del Riesgo: Marcos y Estructuras | 2 | 8 | 4 | 6 |
| G4.2 | Definición y Comunicación del Apetito de Riesgo | 1 | 4 | 5 | 11 |
| G5.1 | Supervisión de la Evaluación y Análisis | 0 | 0 | 3 | 5 |
| G5.2 | Supervisión del Tratamiento y Aceptación | 0 | 0 | 3 | 9 |
| G6.1 | Comunicación Estratégica | 1 | 3 | 5 | 8 |
| G6.2 | Liderazgo Ético y Medición de Efectividad | 1 | 3 | 3 | 6 |
| M1.1 | Desarrollo, Gestión y Operaciones del Programa de Seguridad | 3 | 15 | 4 | 8 |
| M1.2 | Gestión Financiera, Liderazgo de Equipo y Capacitación | 3 | 11 | 5 | 8 |
| M2.1 | Gestión de Activos y Seguridad del Ciclo de Vida de los Datos | 1 | 4 | 4 | 8 |
| M2.2 | Gestión de Identidad y Acceso (IAM) y Principios de Confianza Cero | 1 | 4 | 4 | 11 |
| M3.1 | Arquitectura de Seguridad, Ingeniería y Diseño (Incl. Zero Trust) | 2 | 10 | 3 | 7 |
| M3.2 | Selección, Implementación y Evaluación de Controles | 3 | 13 | 4 | 8 |
| M4.1 | Operaciones de Seguridad, Monitorización e Inteligencia | 6 | 27 | 5 | 12 |
| M4.2 | Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes | 2 | 10 | 4 | 8 |
| M5.1 | Planificación y Preparación (Incl. BIA) | 1 | 4 | 3 | 6 |
| M5.2 | Ejecución, Post-Mortem y Comunicación | 2 | 8 | 4 | 8 |
| M6.1 | Continuidad, DRP y Resiliencia Operativa | 1 | 4 | 4 | 6 |
| M6.2 | Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM | 3 | 13 | 7 | 12 |

## 4. Decisiones
| ID | Decisión | Detalle | Estado |
|---|---|---|---|
| D07 | Horas por unidad | 50 h/unidad (1.200 h) vs. 800 h del Documento Maestro | Pendiente |
| D10 | Licencias y preview | Validar por tenant: E5/E7, P2, Agent 365, Sentinel MCP | Pendiente |
| D12 | Códigos OWASP | Verificados contra ASI 2026 v2.01 | Cerrado |
| D15 | Base 331 | Catálogo 06_Ensayos | Cerrado |
| D16 | AMP [P] | Desarrolladas en V7 | Cerrado |
| D19 | Relaciones editoriales | Sin validación ontológica aún | Pendiente |

## 5. Etapas
| Etapa | Nombre | Calendario | Conceptos clave |
|---|---|---|---|
| E0 | Fundamentos | Semanas 1–4 | G1.1-PA01, G2.1-PA01, M3.1-PA02, M4.1-PA01 |
| E1 | Operar el control | Semanas 5–10 | M4.1-PA02, M4.1-PA03, M4.1-PA04, G2.2-PA03, M3.2-PA01 |
| E2 | Gobernar agentes | Semanas 11–16 | G2.2-PA01, G2.2-PA02, AMP-17, AMP-18, M3.2-PA02, M2.2-PA01 |
| E3 | Construir y evaluar | Semanas 17–24 | M6.2-PA01, M3.2-PA03, AMP-37, M4.2-PA02, M6.2-PA02 |
| E4 | Gestionar la flota | Semanas 25–32 | M1.1-PA01, M4.1-PA05, M4.1-PA06, G4.2-PA01, M1.2-PA01 |
| E5 | Capstone | Semanas 33–40 | G6.1-PA01, M6.1-PA01, AMP-43, M5.2-PA02 |

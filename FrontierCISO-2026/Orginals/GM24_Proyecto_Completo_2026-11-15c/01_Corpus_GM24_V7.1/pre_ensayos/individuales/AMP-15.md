# Pre-ensayo · AMP-15

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 057. AMP-15 — Riesgo sistémico

**Unidad:** G4.1 Gobernanza del Riesgo: Marcos y Estructuras · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 182 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Los riesgos que se propagan por dependencias compartidas —identidad, nube, proveedores, modelos— no se gobiernan activo por activo sino a nivel de ecosistema: una falla en el proveedor de identidad o en el modelo que usan todos los agentes afecta a todo a la vez.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Los riesgos que se propagan por dependencias compartidas —identidad, nube, proveedores, modelos— no se gobiernan activo por activo sino a nivel de ecosistema: una falla en el proveedor de identidad o en el modelo que usan todos los agentes afecta a todo a la vez. La tesis es que el registro de riesgos debe incluir riesgos sistémicos con su mapa de dependencias y que el apetito debe fijar límites de concentración.

**Tensión y límites.** La tensión es que el riesgo sistémico es difícil de cuantificar y fácil de ignorar porque 'nunca pasó'. Otra tensión es que la concentración suele ser racional (un proveedor, un modelo) y la diversificación cuesta. El ensayo debe argumentar cómo decidir cuánta concentración aceptar.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: riesgo sistémico, análisis de dependencias, concentración. Implementación: mapa de dependencias de la flota (Copilot Studio, Foundry, Entra, Sentinel, modelos) y fila de riesgo sistémico en el registro con KRI de concentración.

**Evidencia y evaluación.** Evidencia: mapa de dependencias y registro con al menos un riesgo sistémico tratado. Se evalúa la identificación de puntos únicos de falla.

**Puentes.** Se apoya en HC-023 (concentración); se relaciona con AMP-48, M6.1-PA01 y G4.1-PA02.

**Recomendaciones de práctica y ejercitación.**
1. Dibujar el mapa de dependencias compartidas de la flota.
2. Registrar el riesgo sistémico con KRI de concentración y tratamiento.
3. Simular la caída de una dependencia y medir el alcance.

**Próximos pasos.**
- Vincular con la operación degradada (M6.1-PA01).
- Revisar el apetito de concentración con el comité.
- Actualizar al incorporar proveedores.

**Relación con los conceptos de la(s) unidad(es) G4.1.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| G4.1-K01 | K | Enfoque Organizacional | misma unidad |
| G4.1-K02 | K | Integración ERM | misma unidad |
| G4.1-K03 | K | Tres Líneas de Defensa | misma unidad |
| G4.1-K04 | K | Gestión Avanzada | misma unidad |
| G4.1-K05 | K | Marcos de Riesgo | misma unidad |
| G4.1-K06 | K | Evaluación Organizacional | misma unidad |
| G4.1-K07 | K | Enfoque en Negocio | misma unidad |
| G4.1-K08 | K | Roles y Responsabilidades | misma unidad |
| G4.1-K09 | K | Supervisión | misma unidad |
| G4.1-K10 | K | Reporte a Dirección | misma unidad |
| AMP-16 | AMP | Homeostasis y fuerzas de cambio | misma unidad |
| HC-009 | HC | Gobierno de identidades no humanas | misma unidad |
| HC-014 | HC | Arquitectura de riesgo empresarial | misma unidad |
| HC-022 | HC | Gobierno de crisis multidisciplinario | misma unidad |
| G4.1-PA01 | PA | Tres líneas de defensa para la flota de agentes | misma unidad |
| G4.1-PA02 | PA | Taxonomía y registro de riesgos de agentes | misma unidad |

**Pregunta generadora:** Si su proveedor de identidad fallara una hora, ¿cuántos de sus agentes y controles seguirían funcionando?

---

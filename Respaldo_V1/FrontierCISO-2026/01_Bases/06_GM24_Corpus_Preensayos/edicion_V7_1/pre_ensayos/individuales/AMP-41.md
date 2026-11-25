# Pre-ensayo · AMP-41

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 083. AMP-41 — Prompt injection

**Unidad:** M4.2 Gestión de Amenazas, Vulnerabilidades y Riesgos Emergentes · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Referencias por ID (V7-C09):** OWASP LLM01 (2025), ASI01/ASI06 (2026 v2.01); MITRE ATLAS AML.T0051 · **Extensión:** 203 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La inyección de instrucciones convierte contenido en órdenes: un correo, un adjunto o una página que el agente lee puede contener texto diseñado para desviar su objetivo.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La inyección de instrucciones convierte contenido en órdenes: un correo, un adjunto o una página que el agente lee puede contener texto diseñado para desviar su objetivo. La defensa combina aislamiento de datos (el contenido es dato, nunca instrucción), límites de herramientas (aunque se desvíe, no puede hacer daño), filtros (Prompt Shields) y detección en ejecución (comportamiento anómalo). La tesis es que la inyección no se elimina —un agente de SOC lee correo hostil por diseño— sino que se contiene limitando lo que el agente puede hacer con ella.

**Tensión y límites.** La tensión es que la mitigación más efectiva (limitar herramientas) es la que más reduce utilidad. Otra tensión es la detección: la inyección exitosa parece una decisión normal del agente. El ensayo debe argumentar defensa en profundidad y pruebas periódicas.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: OWASP LLM01/ASI01, MITRE ATLAS, defensa en profundidad. Implementación: skill SK-01 (contenido nunca es instrucción), Prompt Shields/Content Safety, allowlist de tools, Approvals para escritura, pruebas de inyección indirecta por correo sobre AG-01/AG-02, detección de desvíos en Sentinel.

**Evidencia y evaluación.** Evidencia: pruebas de inyección con tasa de éxito y mitigaciones verificadas. Se evalúa la defensa en profundidad y no la confianza en un solo filtro.

**Puentes.** Extiende M6.2-K04; se relaciona con AMP-36, AMP-37 y M4.2-PA02; sostiene AGC-08.

**Recomendaciones de práctica y ejercitación.**
1. Diseñar cinco correos de inyección indirecta y probarlos contra AG-01 y AG-02.
2. Verificar las cuatro capas de defensa en la flota.
3. Escribir la detección de desvío de objetivo en Sentinel.

**Próximos pasos.**
- Incluir en el red teaming periódico (AMP-37).
- Actualizar skill SK-01 con los hallazgos.
- Registrar el riesgo (G4.1-PA02).

**Relación con los conceptos de la(s) unidad(es) M4.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M4.2-K01 | K | Gestión Vulnerabilidades | misma unidad |
| M4.2-K02 | K | Modelado de Amenazas | misma unidad |
| M4.2-K03 | K | Amenaza Interna | misma unidad |
| M4.2-K04 | K | RaaS (Ransomware) | misma unidad |
| M4.2-K05 | K | Priorización por Riesgo | misma unidad |
| M4.2-K06 | K | Superficie de Ataque | misma unidad |
| M4.2-K07 | K | Riesgos Emergentes | misma unidad |
| M4.2-K08 | K | Economía del Cibercrimen | misma unidad |
| M4.2-K09 | K | STRIDE | misma unidad |
| M4.2-K10 | K | IoC (Indicadores) | misma unidad |
| AMP-42 | AMP | Envenenamiento de datos y modelos | misma unidad |
| HC-016 | HC | Superficie de ataque contextualizada | misma unidad |
| HC-026 | HC | Ética, cultura y controles internos | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| M4.2-K11 | K | Escalamiento de privilegios en identidades humanas y no humanas como táctica adversaria | misma unidad |
| M4.2-PA01 | PA | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | misma unidad |
| M4.2-PA02 | PA | Catálogos de amenazas a sistemas agénticos aplicados a la flota | misma unidad |

**Pregunta generadora:** ¿Qué haría su agente de triaje si un correo malicioso le pidiera, en texto, que lo clasificara como legítimo y cerrara el incidente?

---

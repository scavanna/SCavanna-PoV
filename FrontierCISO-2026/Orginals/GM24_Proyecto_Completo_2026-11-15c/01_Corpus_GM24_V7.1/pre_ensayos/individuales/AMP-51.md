# Pre-ensayo · AMP-51

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 093. AMP-51 — Postura de IA en nube

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 179 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** La postura de IA en la nube descubre modelos, endpoints, datos y configuraciones riesgosas en servicios como Foundry u OpenAI —endpoints públicos, claves expuestas, modelos sin filtros, recursos sin dueño— y prioriza su corrección.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** La postura de IA en la nube descubre modelos, endpoints, datos y configuraciones riesgosas en servicios como Foundry u OpenAI —endpoints públicos, claves expuestas, modelos sin filtros, recursos sin dueño— y prioriza su corrección. La tesis es que los recursos de IA son recursos de nube con riesgos adicionales y que la gestión de postura (AI-SPM) debe incluirlos con la misma cadencia que el resto.

**Tensión y límites.** La tensión es la proliferación de recursos de IA fuera del control del SOC (equipos de datos, desarrollo). Otra tensión es la novedad de los hallazgos: el equipo de postura puede no saber interpretarlos. El ensayo debe conectar la postura de IA con el inventario de agentes.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: CSPM/AI-SPM, CIS Benchmarks, configuración segura. Implementación: Defender for Cloud (postura de IA) sobre los recursos de Foundry del alcance, informe AI-SPM, conexión con el inventario de agentes y con Secure Score.

**Evidencia y evaluación.** Evidencia: informe AI-SPM del alcance con hallazgos priorizados y corregidos. Se evalúa la cobertura de todos los recursos que usa la flota.

**Puentes.** Extiende M6.2-K02 (seguridad nube); se relaciona con AMP-50 y M2.1-PA01; sostiene AGC-14.

**Recomendaciones de práctica y ejercitación.**
1. Ejecutar la evaluación de postura de IA sobre los recursos de Foundry del alcance.
2. Reconciliar los recursos con el inventario de agentes.
3. Corregir los tres hallazgos de mayor severidad.

**Próximos pasos.**
- Incorporar a la cadencia de postura (MDO-W05).
- Alimentar el registro de agentes (M2.1-PA01).
- Revisar al crear recursos nuevos.

**Relación con los conceptos de la(s) unidad(es) M6.2.**

| ID | Tipo | Concepto | Relación |
|---|---|---|---|
| M6.2-K01 | K | C-SCRM (Cadena Suministro) | misma unidad |
| M6.2-K02 | K | Seguridad Nube | misma unidad |
| M6.2-K03 | K | DevSecOps | misma unidad |
| M6.2-K04 | K | Seguridad IA | misma unidad |
| M6.2-K05 | K | IoT/OT Security | misma unidad |
| M6.2-K06 | K | Shadow AI | misma unidad |
| M6.2-K07 | K | Responsabilidad Compartida | misma unidad |
| M6.2-K08 | K | Riesgo Terceros (TPRM) | misma unidad |
| M6.2-K09 | K | SDLC Seguro | misma unidad |
| M6.2-K10 | K | SBOM | misma unidad |
| AMP-49 | AMP | Supply chain de modelos | misma unidad |
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| HC-008 | HC | Cadena de confianza en terceros | misma unidad |
| HC-011 | HC | Seguridad de datos en la IA empresarial | misma unidad |
| HC-023 | HC | Riesgo de concentración tecnológica | misma unidad |
| HC-024 | HC | Cumplimiento y privacidad por diseño | misma unidad |
| HC-029 | HC | Aseguramiento de terceros y cadena de suministro | misma unidad |
| HC-030 | HC | Seguridad industrial y continuidad de negocio | misma unidad |
| HC-031 | HC | Seguridad del software y confianza en componentes | misma unidad |
| HC-032 | HC | Evaluación adversarial de sistemas autónomos | misma unidad |
| HC-033 | HC | Seguridad y soberanía de datos distribuidos | misma unidad |
| M6.2-PA01 | PA | Plataformas y rutas de construcción de agentes y responsabilidad compartida en IA | misma unidad |
| M6.2-PA02 | PA | AgentOps / ALM de agentes | misma unidad |
| M6.2-PA03 | PA | Bases multiplataforma, multicloud y multimodelo | misma unidad |

**Pregunta generadora:** ¿Cuántos endpoints de modelos existen hoy en su suscripción de Azure, y cuántos sabe quién los creó?

---

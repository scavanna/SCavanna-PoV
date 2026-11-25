# Pre-ensayo · AMP-49

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

### 091. AMP-49 — Supply chain de modelos

**Unidad:** M6.2 Seguridad en Redes, Nube, Tecnologías Emergentes y SCRM · **Tipo:** AMP · **Horas (sub-plan):** — · **Competencias:** — · **Origen:** V6 (AMP, título) → V7 (pre-ensayo) · **Extensión:** 188 palabras · **Estado:** Idea central desarrollada (lotes AMP-01/02/03, V7); ID curricular, no ESS.

**Definición / idea central.** Modelos y componentes de IA tienen cadena de suministro: procedencia (quién lo entrenó y con qué), licencias (qué uso permiten), integridad (que el artefacto no fue alterado) y evaluación (que se comporta como se declara) antes de su uso.

**Origen.** V6 (AMP, título) → V7 (pre-ensayo)

**Tesis y sentido para el rol.** Modelos y componentes de IA tienen cadena de suministro: procedencia (quién lo entrenó y con qué), licencias (qué uso permiten), integridad (que el artefacto no fue alterado) y evaluación (que se comporta como se declara) antes de su uso. La tesis es que el owner necesita un AI BOM —inventario de modelos, conectores, servidores MCP, bibliotecas y fuentes— equivalente al SBOM, y criterios de aceptación por componente.

**Tensión y límites.** La tensión es la opacidad de los proveedores (datos de entrenamiento no divulgados) y la velocidad de cambio (versiones frecuentes). Otra tensión es la cadena indirecta: un conector de un tercero que llama a otro modelo. El ensayo debe proponer qué exigir y qué aceptar como no verificable.

**Aplicación formativa (base agnóstica → implementación Microsoft).** Base agnóstica: C-SCRM (SP 800-161), SBOM/AI BOM, OWASP LLM03/ASI04. Implementación: AI BOM de la flota (modelos del catálogo de Foundry con sus fichas, conectores certificados, servidores MCP aprobados, bibliotecas), criterios de aceptación y revisión ante cambios.

**Evidencia y evaluación.** Evidencia: AI BOM completo con procedencia, licencia, integridad y evaluación por componente. Se evalúa la cobertura de componentes indirectos.

**Puentes.** Se apoya en HC-031 (cadena de suministro de software); se relaciona con AMP-20, AMP-42 y AMP-50; sostiene AGC-20.

**Recomendaciones de práctica y ejercitación.**
1. Construir el AI BOM de la flota (modelos, conectores, MCP, bibliotecas, fuentes).
2. Definir criterios de aceptación por tipo de componente.
3. Identificar componentes indirectos y su riesgo.

**Próximos pasos.**
- Registrar como AGC-20.
- Revisar ante cambios de versión.
- Conectar con el anexo contractual (M1.2-PA02).

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
| AMP-50 | AMP | Seguridad de herramientas y conectores | misma unidad |
| AMP-51 | AMP | Postura de IA en nube | misma unidad |
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

**Pregunta generadora:** ¿De cuántos componentes de terceros depende su agente más crítico, y de cuántos conoce la procedencia?

---

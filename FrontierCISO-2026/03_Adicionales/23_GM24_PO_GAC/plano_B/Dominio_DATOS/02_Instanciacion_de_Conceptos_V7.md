# 02 · Cómo el dominio Datos instancia los conceptos V7 (sin modificarlos)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Concepto V7 | Tipo | Unidad(es) | Concepto | Instancia |
|---|---|---|---|---|
| G2.2-PA03 | PA | G2.2 | Baseline, excepciones y overrides de un control técnico | Baseline = taxonomía de etiquetas + DLP en bloqueo para SITs críticos + etiquetas por defecto; excepciones = overrides con vencimiento. |
| G3.2-PA01 | PA | G3.2 | Aseguramiento continuo de la configuración del control (deriva) | Deriva: políticas en simulación que debían pasar a producción; etiquetas por defecto removidas. |
| G3.1-PA01 | PA | G3.1 | Panorama regulatorio de IA y agentes | Exposición regulatoria: datos personales, Insider Risk y privacidad. |
| M2.1-PA01 | PA | M2.1 | Registro de agentes como clase de activo | Inventario de repositorios y fuentes de conocimiento; DSPM como descubrimiento. |
| M2.2-PA01 | PA | M2.2 | Permisos de humanos y agentes en el control: RBAC unificado, roles y conectores | Roles de Purview (IRM solo humanos) y Graph scopes de agentes. |
| M3.1-PA02 | PA | M3.1 | Arquitectura de protección del dominio Zero Trust (instancias: correo y colaboración · detección y respuesta unificada · endpoints · identidades · datos) | Instancia Datos: arquitectura de protección (clasificación → etiquetado → encriptación → DLP → DSPM → IRM). |
| M4.1-PA01 | PA | M4.1 | Modelo operativo del producto-control por cadencias (instancias: Defender for Office 365 · Defender XDR · Defender for Endpoint · Defender for Identity/Entra · Purview · Sentinel · Defender for Cloud) | Instancia Datos del modelo operativo (25 tareas). |
| M4.1-PA03 | PA | M4.1 | Gestión de la calidad de detección del dominio: FP/FN, tuning, listas, indicadores y supresiones (instancias: MDO · XDR · MDE · MDI/ID Protection · Purview DLP · Sentinel) | Instancia Datos: FP de DLP, confianza de SIT, excepciones, simulación. |
| M4.2-PA01 | PA | M4.2 | Amenazas del dominio Zero Trust (instancias: correo y colaboración · cross-domain · endpoints · identidades · datos) | Instancia Datos: exfiltración, sobrecompartición, insider, fuga por IA. |
| M3.2-PA01 | PA | M3.2 | El control como producto: objetivo → configuración → evidencia | Cadena objetivo → configuración → evidencia para 5 controles de Purview. |
| AMP-31 | AMP | M2.1 | DSPM | DSPM for AI: instancia directa. |
| AMP-32 | AMP | M2.1 | Gobierno de datos para RAG | Gobierno de datos para RAG: owner de las fuentes aprobadas de todas las flotas (AGC-07). |
| AMP-11 | AMP | G3.1 | Soberanía de datos | Soberanía: residencia y claves de datos etiquetados. |
| HC-011 | HC | G3.1 · M2.1 · M6.2 | Seguridad de datos en la IA empresarial | Flujo de información sensible en aplicaciones de IA: instancia directa. |
| HC-033 | HC | G3.1 · M2.1 · M6.2 | Seguridad y soberanía de datos distribuidos | Soberanía y transferencias: etiquetas y DLP como instrumento. |
| AMP-52 | AMP | G6.2 · M3.2 | Content safety y riesgos de contenido generado | Content safety: DLP para IA complementa guardrails de salida. |
| M4.1-K11 | K | M4.1 | Deception y señuelos como control detectivo | Señuelos: documentos cebo etiquetados como detección de exfiltración. |
| AMP-25 | AMP | G6.2 | Ética de autonomía | Ética: bloquear comunicación legítima e investigar insider exigen proporcionalidad. |

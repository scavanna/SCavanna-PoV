# Matriz de gobierno: escenario, técnica, privacidad y evidencia

## Propósito

Conectar tres vistas sin mezclar sus objetos:

- **Ejecutiva**: activo/proceso, evento, consecuencias, tolerancia y riesgo residual.
- **Técnica**: comportamientos, controles, detecciones, pruebas y cobertura.
- **Privacidad**: titulares, tratamiento, amenaza, obligaciones y mitigaciones.

Los mapeos siguientes son hipótesis de trabajo; deben validarse contra arquitectura, datos, controles y versión de cada base. La guía didáctica de ransomware muestra cómo convertir estas relaciones en escenarios, valoración, controles, pruebas y playbooks específicos por tecnología y sector.

## Matriz de escenarios

| ID | Escenario ejecutivo | Comportamientos orientativos | Controles/detecciones propuestos | Privacidad/LINDDUN | Evidencia/KRI |
|---|---|---|---|---|---|
| RS-001 | Interrupción prolongada de ERP/servicio y divulgación por cifrado/exfiltración | ATT&CK: `T1566`, `T1078`, `T1003`, `T1021`, `T1567`, `T1486` como candidatos; validar cadena | MFA resistente a phishing, privilegio mínimo, segmentación, EDR/XDR, backup aislado/probado, runbook | Data Disclosure; posible Link/Identify; obligaciones de notificación según jurisdicción | RTO real, cobertura Tier-0, MTTC, backup restore, alcance de datos |
| RS-002 | Fraude/toma de cuenta ejecutiva y compromiso de colaboración | `T1566.002`, `T1539`, `T1111`, `T1098`, `T1114` como candidatos | CA fuerte y dispositivos, protección/rotación de tokens, ITDR, bloqueo de auto-forward, doble aprobación | Disclosure y Linking; retención/minimización | sesiones anómalas, controles de pago, reportes phishing, revocación |
| RS-003 | Exfiltración masiva por aplicación/API y pérdida de confianza | `T1190`, `T1213`, `T1046`, `T1020` según evidencia de diseño | autorización robusta, gateway/WAF, SAST/DAST, EASM, logging y rate limits | Identifying, Detecting, Data Disclosure; DPIA y minimización | MTTR de exposición, API inventariadas, hallazgos y alcance de datos |
| RS-004 | Acceso o fuga indirecta por proveedor/tercero | `T1195`, `T1199`, `T1078` si corresponde | Zero Trust, PAM/JIT, mínimo privilegio, SBOM/firma, monitoreo, offboarding | Unawareness/unintervenability, Non-compliance; subencargados y transferencias | evaluaciones vigentes, SLA/notificación, accesos, borrado certificado |
| RS-005 | Fuga o sabotaje interno con abuso de privilegio | `T1005`, `T1530`, `T1052`, `T1562` como candidatos | RBAC/ABAC, PIM/PAM, DLP, UEBA, sesiones, separación de funciones | Data Disclosure, Non-repudiation como equilibrio de accountability/privacidad | cuentas JIT, tiempo de revocación, alertas DLP, calidad de auditoría |
| RS-006 | Acción indebida o fuga por IA/agente | validar MAESTRO/ATLAS; no asumir IDs aquí | identidad propia, mínimo privilegio, aprobación humana, sandboxes, validación de tool calls, guardrails y RAG seguro | Detecting, Unawareness/unintervenability, Linking; base legal, minimización | inventario de agentes, pruebas adversariales, fugas bloqueadas, cobertura de permisos |

## Cadencias y decisiones

### Diseño / cambio

1. Crear/revisar caso ejecutivo y modelo técnico.
2. Asignar activos, datos, fronteras, titulares y dueño.
3. Derivar requisitos de controles y privacidad.
4. Definir evidencia y umbral de aceptación antes de producción.

### Validación

1. Probar diseño y despliegue.
2. Ejecutar threat emulation/purple team/BAS y pruebas de privacidad cuando proceda.
3. Registrar cobertura, falsos negativos, supuestos y límites.
4. Recalcular riesgo residual bajo reglas aprobadas; no de forma “automática” sin contexto.

### Operación

1. Monitorizar KRIs y señales de exposición.
2. Correlacionar incidentes y hallazgos con escenarios.
3. Revisar excepciones y tratamientos vencidos.
4. Ejecutar continuidad/DPIA/control testing con cadencia definida.

### Gobierno y comité

Presentar exposición, tolerancia, tendencia, incertidumbre, decisiones requeridas y evidencia. Evitar métricas como “ataques bloqueados” sin relación al escenario. Para cada excepción registrar: riesgo, duración, compensación, propietario, aprobador y fecha de expiración.

## Modelo RACI mínimo

| Actividad | Aprobador | Responsable | Consultados |
|---|---|---|---|
| Riesgo y apetito | dueño negocio/comité | risk owner/CISO | finanzas, legal |
| Arquitectura/amenaza | CTO/CISO según alcance | arquitectura/AppSec | producto, SOC |
| Privacidad | DPO/Legal | privacy engineering | seguridad, producto |
| Controles | control owner | ingeniería/operación | riesgo, arquitectura |
| Prueba independiente | CISO/Auditoría | assurance/red team | propietarios |
| Riesgo residual | dueño negocio | risk owner | CISO, DPO |
| Incidente | ejecutivo designado | SOC/IR/resiliencia | legal, DPO, comunicación |

## Métrica de trazabilidad

- % de riesgos ejecutivos con técnica/abuso y fuente documentados.
- % de técnicas mapeadas a control y evidencia verificable.
- % de escenarios críticos probados dentro de ventana.
- % de hallazgos con tratamiento, dueño y fecha.
- % de tratamientos de privacidad con titular/tratamiento/documentación.
- Edad de la última revisión por escenario y cobertura de activos.

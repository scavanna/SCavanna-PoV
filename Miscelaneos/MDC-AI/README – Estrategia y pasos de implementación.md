# Enriquecer alertas de Defender for Cloud – AI services con MITRE ATLAS / OWASP LLM en Microsoft Sentinel

**Versión:** 1.0 · 18-nov-2026 · Para: Santiago Cavanna (CSU Security)
**Premisa:** Microsoft solo publica tácticas ATT&CK por alerta; el mapeo ATLAS/OWASP es *propuesto* y vive en una watchlist versionada que el cliente controla.

---

## 1. Dónde puede ocurrir el enriquecimiento (y qué conviene)

| Capa | Mecanismo | Qué permite | Limitación | Veredicto |
|---|---|---|---|---|
| **A. Ingesta** | DCR *workspace transformation* sobre `SecurityAlert` | Modificar la fila al entrar | `SecurityAlert` soporta DCR workspace transformation, pero las transformaciones **no pueden hacer lookup a watchlists**; solo lógica estática (`case()`); mantener el mapeo en código KQL es frágil. Riesgo de romper la tabla que usan XDR/incidentes. | ❌ No recomendado como vía principal (válido para tags simples). |
| **B. Consulta (query-time)** | **Watchlist + función KQL guardada `MDCAI_Enriched()`** | Vista enriquecida sin tocar datos; base para hunting, workbooks, reglas, Security Copilot | No se ve en el incidente por sí sola | ✅ **Base obligatoria**. |
| **C. Detección** | **Analytics rule** que consume `MDCAI_Enriched()` y re-emite alerta con *custom details*, título/descr dinámicos y entity mapping | ATLAS/OWASP **dentro** de la alerta/incidente, consultables (`SecurityAlert.ExtendedProperties.Custom Details`), accionables por automation rules | Duplicación de incidentes si no se gestiona (ver §4) | ✅ Recomendado para analistas. |
| **D. Respuesta** | **Automation rule + Playbook** `Enrich-MDCAI-ATLAS` | Tags `ATLAS:`/`OWASP:`, comentario con links, *incident tasks*, severidad | Costo Logic App, latencia 1–2 min | ✅ Recomendado; complementa C o sustituye C si no se quiere duplicar. |
| **E. Reporting** | **Summary rule** → `MDCAI_ATLAS_Daily_CL` + **Workbook** heatmap + export *ATLAS Navigator layer* | Cobertura y tendencia por táctica/técnica ATLAS y OWASP; retención larga barata | Agregado, no forense | ✅ Recomendado. |
| **F. Asistente** | **Plugin Security Copilot (KQL)** sobre `MDCAI_Enriched()` + skill "explica la alerta en ATLAS/OWASP" | Lenguaje natural para analista | Requiere SCU | ◐ Opcional / diferenciador. |
| **G. Fuente** | Enviar `SecurityContext` (UserSecurityContext) desde la app a Azure OpenAI | La alerta llega con `End user ID`, `Application name`, IP → correlación con Entra | Requiere cambio en la app del cliente | ✅ Pedirlo siempre: mejora toda la cadena. |

**Estrategia recomendada = B + C (o D) + E, con G como prerequisito de calidad.**

---

## 2. Paquete entregado

```
mdcai_atlas/
├─ watchlist/MDCAI_ATLAS_OWASP.csv      # SearchKey=AlertType → ATLAS tácticas/técnicas, OWASP, confianza, guía analista
├─ watchlist/ATLAS_Techniques.csv       # Diccionario técnicas ATLAS usadas (id, nombre, táctica, URL)
├─ kql/01_fn_MDCAI_Enriched.kql         # Función guardada (vista enriquecida)
├─ kql/02_analytics_rule_enrich_MDCAI.kql  # Regla programada con custom details / alert details
├─ kql/03_correlation_and_reporting.kql # Heatmap, Navigator layer, OWASP por app, kill-chain, Jailbreak→Leak, Entra, QA, tags
├─ kql/04_summary_rule_MDCAI_ATLAS_Daily.kql
└─ automation/playbook_Enrich-MDCAI-ATLAS.md  # Diseño del Logic App + automation rule + validación
```

---

## 3. Pasos de implementación

1. **Conectores:** Defender XDR (incidentes) **y** Microsoft Defender for Cloud *tenant-based* (alertas en `SecurityAlert`). Sin el segundo, los joins sobre `SecurityAlert` quedan incompletos.
2. **Watchlists:** importar `MDCAI_ATLAS_OWASP.csv` (alias `MDCAI_ATLAS_OWASP`, SearchKey `AlertType`) y `ATLAS_Techniques.csv` (alias `ATLAS_Techniques`, SearchKey `TechniqueId`). Versionar los CSV en Git; opcional: auto-update desde blob (`WatchlistAutoUpdateFromNetworkRestrictedBlob` en Azure-Sentinel repo).
3. **Función:** guardar `01` como función `MDCAI_Enriched`. Probar: `MDCAI_Enriched() | take 10`.
4. **Analytics rule (opcional, patrón C):** crear regla programada con `02`; configurar *Alert details* (título/descr/severidad), *Custom details* (ver cabecera del archivo) y *Entity mapping*. Decidir estrategia anti-duplicado (§4).
5. **Automation rule + Playbook (patrón D):** desplegar según `automation/playbook_Enrich-MDCAI-ATLAS.md`.
6. **Summary rule:** crear con `04` → tabla `MDCAI_ATLAS_Daily_CL`.
7. **Workbook:** paneles con 3.1 (heatmap táctica×técnica), 3.3 (OWASP por app), 3.4 (kill-chain), 3.7 (UNMAPPED = deuda de mapeo). Exportar 3.2 a ATLAS Navigator.
8. **Validar** con *Sample alerts* del plan AI Services (Defender for Cloud) y revisar que `UNMAPPED` = 0.

---

## 4. Decisión clave: cómo evitar duplicar incidentes (patrón C)

- **Opción 1 (recomendada):** no crear la analytics rule; usar solo **automation rule + playbook** sobre el incidente MDC original → sin duplicados, ATLAS/OWASP como tags, comentario y tareas. Para KQL/reporting se usa `MDCAI_Enriched()`/summary rule.
- **Opción 2:** crear la regla 02 **y** una automation rule que cierre el incidente MDC original (`Undetermined`, tag `superseded-by-enriched`). Ventaja: custom details nativos y título con ATLAS en la cola. Riesgo: métricas de MTTR distorsionadas si no se excluye el tag.
- **Opción 3:** regla 02 con *Alert grouping* que agrupe la alerta enriquecida con la original en el mismo incidente (grouping por entidad `AzureResource` + ventana). Funciona cuando la original llega vía XDR al mismo incidente; validar en el tenant.

---

## 5. Qué ve el analista al final

- **Título:** `[ATLAS AML.T0054 | OWASP LLM01] A Jailbreak attempt on an Azure AI model deployment was blocked…`
- **Tags:** `AI-Threat`, `ATLAS:AML.T0054`, `ATLAS:AML.T0051.000`, `OWASP:LLM01`, `ATLAS-Tactic:Execution`, `Mapping-Confidence:High`
- **Comentario:** tabla con links a atlas.mitre.org / genai.owasp.org + guía de investigación + aviso "mapeo propuesto".
- **Tareas:** pasos concretos (rotar credenciales, revisar índice RAG, revisar filtros del deployment…).
- **Custom details** (si patrón C): `ATLAS_Techniques`, `OWASP_LLM`, `Original_AlertType`, `ATTACK_Tactics`.

## 6. Qué habilita para correlación y reporting

- Kill-chain ATLAS por recurso (3.4) y secuencia Jailbreak → Leak/Credential (3.5) como **detecciones de segundo nivel**.
- Correlación con identidad (3.6) usando `End user ID`/IP → exige `SecurityContext` en la app.
- Heatmap/Navigator ATLAS (3.1/3.2) para **mostrar cobertura y gaps** (sustituye la página MITRE de Sentinel, que solo soporta ATT&CK).
- OWASP por aplicación (3.3) para conversaciones con dueños de producto/AppSec.
- Tabla diaria (summary rule) para reportes mensuales/anuales y tendencia por táctica.

## 7. Gobierno del mapeo

- La watchlist es la **única fuente de verdad**; cambios por PR en Git con columna `Confidence` y fecha.
- Revisar al publicarse nuevas alertas MDC-AI (query 3.7 detecta `UNMAPPED`) y nuevas versiones de ATLAS/OWASP (OWASP 2026 ya cambia posiciones: Excessive Agency #3, Unbounded Consumption #6).
- Etiquetar siempre como "mapeo propuesto" hasta validación con PG (Shay Amar / Liran Levy) o publicación oficial.

## 8. Limitaciones conocidas

- Nombres de claves en `ExtendedProperties` (`Caller IP address`, `Prompt evidence`, `End user ID`, `Application name`) pueden variar por alerta; ajustar la función tras inspeccionar `ExtendedProperties` reales del tenant.
- Las DCR transformations sobre `SecurityAlert` no pueden consultar watchlists; por eso el enriquecimiento se hace en query/detección/respuesta.
- Las consultas no fueron ejecutadas contra un tenant en esta sesión; validar sintaxis con datos reales (en especial 3.6 por columnas opcionales de SigninLogs).

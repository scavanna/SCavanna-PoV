# Defender for Cloud for AI Services × Sentinel × MITRE ATLAS — V3

**Versión del mapeo: 3.0.0 · Fuentes verificadas al 18 de noviembre de 2026.** Paquete autocontenido para piloto: no requiere abrir los entregables v1/v2. El código y la matriz son una implementación propuesta, no contenido soportado por Microsoft ni un despliegue ya validado en un tenant.

## Qué instalar, y para qué

| Si necesitás… | Usá… |
|---|---|
| Una matriz para defender el mapeo y discutir gaps | [Excel V3](MDC_AI_ATLAS_OWASP_Mapping_v3.xlsx) y [análisis de fuentes](docs/Investigacion_y_mapeo.md). |
| Contexto de CAAT, ATLAS y OWASP en Logs/Workbook, sin mutar alertas | [01_Core.arm.json](deploy/01_Core.arm.json): cuatro watchlists, tres funciones KQL y workbook. |
| Mostrar contexto en el **incidente original** | [02_Playbook.arm.json](deploy/02_Playbook.arm.json) + una automation rule configurada en Sentinel. Logic Apps está deshabilitado y en modo sin escritura por defecto. |
| Una serie diaria por `AlertType` | [03_Resumen_Diario.arm.json](deploy/03_Resumen_Diario.arm.json), opcional. |
| Saber qué clasificación estaba aplicada en una fecha | [04_Historial_DCR.arm.json](deploy/04_Historial_DCR.arm.json) + [Save-Snapshot.ps1](scripts/Save-Snapshot.ps1), opcional. |
| Exportar actividad a ATLAS Navigator | KQL `12` → CSV → `scripts\export_navigator.py`. No reemplaza la matriz nativa ATT&CK. |

El inventario y los SHA-256 quedan en `MANIFEST.sha256`. **No compartas externamente el ZIP completo:** el anexo `uso-interno\` conserva enlaces de Teams autorizados para el usuario, separados del Excel y de todos los artefactos de despliegue.

## 1. Antes de instalar

- Usá un workspace de prueba en **Azure comercial**, en la misma suscripción y grupo de recursos que los despliegues ilustrados. Registrá los proveedores `Microsoft.OperationalInsights`, `Microsoft.SecurityInsights`, `Microsoft.Insights`, `Microsoft.Logic` y `Microsoft.Web` según los componentes seleccionados. Usá un nombre de deployment propio.
- **Portal Defender con XDR:** la integración de alertas de Defender for Cloud se realiza en Defender XDR; no des por obligatorio el conector clásico tenant-based ni esperes verlo en ese portal. Comprobá que las alertas estén en el **Log Analytics workspace elegido**, no solo visibles en Advanced Hunting de Defender. En la modalidad **Azure portal con integración de incidentes de XDR**, habilitá la ruta MDC que corresponda; en esa modalidad Microsoft recomienda el conector tenant-based (preview) y evitar el conector legacy en paralelo. Fuente: [MDC a Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) y [flujo clásico de incidentes](https://learn.microsoft.com/en-us/azure/sentinel/ingest-defender-for-cloud-incidents).
- En Logs ejecutá `kql\00_Inspeccionar_origen.kql`. Compará `ProductName`, `ProviderName`, tipos y volumen con una alerta conocida en el portal. El filtro desplegable admite `Azure Security Center` (valor de ejemplo oficial) y el nombre alternativo `Microsoft Defender for Cloud`; este segundo no se presupone. Si tu ruta muestra otro valor, corroboralo antes de editar `product_names` en `data\policy.json` y reconstruir. **No filtres por el título ni uses `ProviderName` como único identificador.**
- `SystemAlertId` identifica una instancia de alerta en el workspace. `AlertType` es una **clase** de alerta y se usa para consultar el mapeo. Si hay fuentes duplicadas que generan IDs distintos, cotejá `VendorOriginalId` y la ruta de ingesta; las consultas no unen automáticamente identidades de diferentes conectores o workspaces.
- No habilites captura de prompts para instalar este paquete. [`UserSecurityContext`](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai) es opcional, solo para rutas y SDK compatibles. Las consultas de hunting necesitan un identificador de usuario Entra confiable emitido por la aplicación; no usan IP como sustituto. Si la app no lo adjunta o el workspace mezcla tenants de identidad, no actives esa correlación.

## 2. Capa de consulta y workbook

Abrí PowerShell en la carpeta extraída. Los comandos muestran un piloto; **no los ejecutes sobre producción** hasta terminar la sección 5. Sustituí los valores entre comillas.

```powershell
az account set --subscription '<ID de la suscripción de piloto>'
$rg = '<grupo de recursos del workspace>'
$ws = '<nombre del workspace Sentinel>'
$region = '<región del workspace>'

az deployment group validate -g $rg --template-file .\deploy\01_Core.arm.json --parameters "workspaceName=$ws" "workbookLocation=$region"
az deployment group create   -g $rg --name mdcai-v3-core --mode Incremental --template-file .\deploy\01_Core.arm.json --parameters "workspaceName=$ws" "workbookLocation=$region"
```

Si preferís configuración manual **en vez de** ARM, importá los CSV de `watchlists\` con los alias exactos y respetá sus claves:

| Alias | `SearchKey` | Uso |
|---|---|---|
| `MDCAI_V3_Profiles` | `AlertType` | Una fila por alerta documentada; campos directos y disposición. |
| `MDCAI_V3_Relations` | `AlertType` | Varias filas por tipo por diseño; clave completa framework + edición + ID. Hipótesis en modo de consulta. |
| `MDCAI_V3_CAAT` | `CAAT_Id` | Los 14 escenarios; fuentes y notas, sin herencia automática de etiquetas. |
| `MDCAI_V3_ATLAS` | `TechniqueId` | Diccionario de la versión MITRE fijada; no mide cobertura. |

Guardá `kql\01`, `02` y `03` como funciones con alias del nombre de archivo (`MDCAI_V3_Base`, `MDCAI_V3_Enriched`, `MDCAI_V3_Escenarios`) y parámetro `Lookback:timespan`, en ese orden. En el editor avanzado de Workbooks, pegá `workbook\MDCAI_V3_Workbook.json`, seleccioná el workspace correspondiente en el origen de las consultas y guardá. Si la watchlist está en estado `InProgress`, esperá antes de validar.

Probá `MDCAI_V3_Enriched(7d) | take 20` y `MDCAI_V3_Escenarios(30d)` (14 filas incluso sin actividad). Ejecutá `kql\15_QA_watchlists.kql` (esperado: cero filas, incluye controles de cantidad) y `06` (puede haber candidatos no clasificados; investigalos en vez de asignarles un ID por obligación). El workbook no usa tablas o componentes opcionales.

## 3. Automatización del incidente original

```powershell
az deployment group validate -g $rg --template-file .\deploy\02_Playbook.arm.json --parameters "workspaceName=$ws" "location=$region"
az deployment group create -g $rg --name mdcai-v3-playbook --mode Incremental --template-file .\deploy\02_Playbook.arm.json --parameters "workspaceName=$ws" "location=$region"
```

1. En la Logic App Consumption `Enrich-MDCAI-ATLAS-v3`, verificá identidad administrada y conexión Sentinel creada. Otorgá **Microsoft Sentinel Responder** sobre el workspace a esa identidad. Al servicio de Sentinel, no a la identidad del playbook, otorgale **Microsoft Sentinel Automation Contributor** en el grupo de recursos del playbook desde *Manage playbook permissions*. Para ejecutar a mano y configurar reglas, usá roles de operador/contribuidor apropiados. [Permisos y ejecución](https://learn.microsoft.com/en-us/azure/sentinel/automate-responses-with-playbooks).
2. Poné `workflowState=Enabled`, manteniendo `writeToIncident=false`. Ejecutalo **manualmente** en un incidente de prueba; `Plan` muestra el contexto y los tags que se aplicarían, sin escribir. El flujo usa la [API de alertas del incidente](https://learn.microsoft.com/en-us/rest/api/securityinsights/incidents/list-alerts?view=rest-securityinsights-2025-09-01), no el título, ni una consulta con IDs interpolados. Si el `productName` del payload ARM difiere de Logs, validá ambos valores en `data\policy.json`.
3. Solo después de validar el plan, redeplegá `02` con `workflowState=Enabled writeToIncident=true`. En Sentinel > *Automation*, creá `MDCAI-V3-Enrich-OnCreate`: **When incident is created** → **Run playbook** → V3. Si la condición *Alert product names* se ofrece y se corroboró en el tenant, usala para acotar. El flujo siempre revalida el tipo y el producto alerta por alerta. No sobreescribas incidentes no IA. Para alertas que se agregan más tarde, ejecutá el playbook manualmente o evaluá una segunda regla restringida inequívocamente a **adición de alertas**, si la condición está disponible. No lo conectes a actualizaciones genéricas (tags/comentarios disparan actualizaciones).
4. Esperá un comentario por **incidente + versión** y tags aditivos `MDCAI:` solo a partir de vínculos directos (OWASP 2026, versiones en Excel/Logs; condicionales no se etiquetan). El comentario usa un identificador determinista y se vuelve a escribir solo si cambian los tipos incluidos. No se toca estado, propietario, severidad ni el título. Los tags agregados no se retiran automáticamente; son un índice de triage, no la evidencia ni un registro histórico autoritativo. Las alertas no IA no se incluyen en el comentario. `includeModelScan=false` por defecto: aprobalo aparte como señal de escaneo en preview.

El playbook trae **la misma versión compilada de la política** que las watchlists; no necesita esperar la ingesta a Logs. Redeplegá `01` y `02` juntos al cambiar la política. Si el conector regional difiere, abrí la Logic App y creá/asociá la conexión Sentinel con identidad administrada; volvé a probar antes de activar escrituras. Revisión de 403: verificar RBAC y autorización de ejecución; 429/5xx: revisar ejecuciones, consumo y reintentar el incidente sin duplicar el comentario. No exponer cuerpos de alertas en diagnósticos; el flujo no copia secretos, contenido de prompt/respuesta ni URLs detectadas. Solo incluye texto y enlaces revisados del paquete.

## 4. Hunting y reporting

| Consulta | Resultado e interpretación |
|---|---|
| `04` / `05` | Alertas distintas por técnica/riesgo, solo vínculos directos. No sumes los valores entre categorías o ediciones. |
| `07` | Matriz larga: aplicá un filtro `AlertType` exacto para ver los requisitos de evidencia de los vínculos condicionales. |
| `08` | Intento detectado no bloqueado → credencial en respuesta, con identidad y recurso no vacíos, dos alertas distintas y secuencia temporal de hasta 2 h. **Hipótesis**, no prueba de causalidad o exfiltración. |
| `09` | Pivote de usuario con `SigninLogs` en un workspace de un único tenant de identidad. Sin fuente de usuario confiable no retorna vínculos atribuibles. Entra service principals son una fuente separada: no los correlaciones con `UserId`. |
| `11` | Incidentes distintos por tag. Cuenta la última versión de incidentes con al menos una actualización en el rango. |
| `12` | Exportá `TechniqueId,Alerts` a CSV. Ejecutá `python .\scripts\export_navigator.py .\conteos.csv .\actividad-atlas.json` e importá el JSON en [ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/). Compartí conteos según la política de tu organización. |

**Reglas analíticas:** no instales una regla que reemita cada alerta de MDC ni cierres el incidente original. Si querés alertar sobre la hipótesis `08`, aprobala primero como hunting. Medí falsos positivos con evidencia propia; después configurá una regla programada para la **correlación nueva**, con una ventana por tiempo de actividad, una ventana disjunta de elegibilidad por ingesta de la segunda alerta y deduplicación persistente por pareja o segundo ID. Probá reenvíos y eventos fuera de orden antes de habilitarla. Conservá los dos IDs en *Custom details*, no copies evidencia sensible ni uses `AML.*` como técnicas ATT&CK nativas. La agrupación de una regla no garantiza una fusión con un incidente XDR preexistente.

**Volumen diario:** desplegá `03` con `workspaceName` y `firstBinStartUtc` en medianoche UTC (vigente o siguiente, ISO 8601). Por ejemplo:

```powershell
$bin = [DateTime]::UtcNow.Date.AddDays(1).ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")
az deployment group create -g $rg --name mdcai-v3-daily --mode Incremental --template-file .\deploy\03_Resumen_Diario.arm.json --parameters "workspaceName=$ws" "firstBinStartUtc=$bin"
```

Alternativa manual: Log Analytics > *Summary rules* → `kql\10`, bin 1440 min, destino `MDCAI_V3_Daily_CL`, ajustar el retraso a la latencia observada. `10` no llama funciones guardadas ni impone un segundo rango temporal. `16` lee el resultado. Una alerta actualizada en dos días puede aparecer en ambos bins; el total es **alertas distintas por día**, no alertas únicas mensuales. No se infiere ATLAS a partir de la suma de dimensiones. [Summary rules](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/summary-rules).

**Histórico del mapeo:** desplegá `04` solo si lo necesitás. La identidad escritora debe tener acceso de lectura al workspace y **Monitoring Metrics Publisher** en el DCR. En Azure CLI, consumí `properties.endpoints.logsIngestion` e `immutableId` de ese DCR y el `customerId` del workspace (GUID). En PowerShell 7 ejecutá `.\scripts\Save-Snapshot.ps1 -WorkspaceId <GUID>` primero: informa la cantidad sin escribir. Para persistir, repetí con `-DcrEndpoint <URL> -DcrImmutableId <dcr-ID> -CommitSnapshot`. La consulta `13` deduplica por `AlertKey` + `MappingVersion`; la escritura es append-only y puede duplicar filas físicas ante un reintento. `TimeGenerated` es la captura, `SourceAlertTime` es el tiempo de alerta. Esto conserva la **clasificación calculada**, no demuestra qué leyó efectivamente el analista. Revisá costos/retención, soporte de Private Link (el script es solo para endpoint directo comercial) y RBAC antes de automatizar. No almacena prompts ni entidades de usuario.

## 5. Validación y migración segura

| Prueba | Criterio de aceptación |
|---|---|
| Ingesta | Comparar metadatos de un caso real autorizado o [Sample alerts](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alert-validation) del plan si aparecen en tu tenant. Que fluya una muestra valida transporte, no cobertura de cada detector. |
| Taxonomía | `15` sin diferencias, cuatro watchlists completas; todo vínculo automático está documentado como **propuesta directa** y sin IDs retirados; alerta con tipo desconocido queda para revisión. |
| Cómputo | Dos filas del mismo ID no se cuentan dos veces en el workbook dentro del mismo workspace. Dos alertas de identidad vacía no se emparejan. Una única alerta no satisface `08`. |
| Incidente | Ejecución sin escritura correcta; luego comprobá repetición, incidente compuesto/mixto, nuevo tipo, 403/429 controlados y `includeModelScan=false`. No se pierde ningún tag ajeno ni se cierra ni crea otro incidente por enriquecimiento. |
| Reportes | Los 14 escenarios aparecen aun sin actividad. Dos ediciones OWASP separadas. Snapshot/summary solo si habilitados; revisar volumen y latencia. Cargar el JSON de Navigator y confirmar que las técnicas se ubican en la matriz. |

V3 no utiliza los alias, reglas, playbooks ni tablas v1/v2. Si ya desplegaste versiones anteriores, inventarialas; validá V3 de forma paralela **sin escritura**; desactivá primero la automatización anterior y cualquier regla que reemita alertas antes de activar escrituras de V3. Conservá historial y notas que todavía utilices. Para rollback, deshabilitá la automation rule V3 o redeplegá `02` sin escritura; las alertas siguen llegando sin enriquecimiento. No hace falta cerrar incidentes ni eliminar la configuración anterior para dar de baja este flujo.

Para reemplazar los **archivos** antiguos, conservá el ZIP y/o la carpeta V3. Reemplazo detallado en [Migración de entregables](docs/Migracion_de_entregables.md). No descartes evidencia o notas que hayas agregado por tu cuenta en los originales.

## Mantenimiento y verificación local

- `data\policy.json`: única fuente editable de decisiones; `data\reference.json`: snapshot de fuentes. No edites watchlists, Excel ni ARM generados para cambios durables. Actualizá fuentes, revisá cambios semánticos, incrementá `release` y aprobá en Git. En un redepliegue, confirmá que las watchlists hayan quedado con una sola versión antes de reactivar el playbook; si el servicio no reemplaza ítems importados por ARM, recreá los alias V3 en ventana controlada siguiendo el orden anterior. No mezcles filas viejas y nuevas.
- Para reconstruir: `python -m pip install -r .\requirements.txt` si faltan dependencias; `python -B .\scripts\build_release.py`; `python -B -m unittest discover -s .\tests`. Para crear un ZIP con manifest actualizado: `python -B .\scripts\pack_release.py`. Esta operación no se comunica con Azure.
- Para contrastar de nuevo el snapshot con las fuentes públicas, instalá las dependencias de `scripts\requirements-refresh.txt` y ejecutá `python -B .\scripts\refresh_reference.py --check`. Este paso requiere Internet y no cambia `reference.json`. La construcción normal y el playbook no consultan GitHub, MITRE ni OWASP en tiempo de ejecución.
- Pasos y evidencia de automatización: [pruebas locales y criterios de piloto](docs/Validacion.md). Las pruebas locales no sustituyen `az deployment group validate`, los prerrequisitos de red/RBAC ni la ejecución KQL en tu workspace.

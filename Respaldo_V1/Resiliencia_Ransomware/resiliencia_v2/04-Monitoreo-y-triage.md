# 04. Guía de control, monitoreo y triage (v2.0 · DE-01 a DE-13 sobre Full Microsoft)

**Operadores:** SOC y guardia designada. **Objetivo:** detectar actividad adversaria antes de que dañe servicios y preservar un hilo de decisión verificable. Las señales abajo son **casos de uso de detección**, no reglas ya desplegadas ni umbrales universales. Cada regla necesita cobertura, línea base, validación y autorización de respuesta [MS-03, MS-05].

## 1. Precondiciones y salud de la vigilancia

Inventariar fuentes y población esperada: endpoints/servidores, identidad local y nube, aplicaciones SaaS, DNS, VPN, red/egress, almacenamiento, respaldos y auditoría de datos. Para cada flujo registrar propietario, cobertura, último evento UTC, retraso de ingestión, retención aprobada, zona horaria, acceso de emergencia y fuente alternativa. No colocar datos sensibles ni eventos reales en los HTML de esta carpeta. Comprobar al comienzo de cada turno la ingesta y la capacidad de recibir alertas; por cada fuente crítica caída abrir incidencia propia y aplicar vigilancia compensatoria [CT-11].

**Establecer umbrales por entorno:** usar tasas normales de cambios, volúmenes y picos autorizados; para acciones críticas (p. ej., borrado de copias o alta de privilegios) alertar por evento aunque la tasa sea baja. Probar sensibilidad y falsos positivos antes de automatizar bloqueos. El dueño de negocio aprueba tiempo objetivo de detección/triage según RTO, no a la inversa.

## 2. Casos de uso `DE-*`

| ID y cadena | Señal que inicia revisión | Datos para confirmar / discriminar | Escalamiento |
|---|---|---|---|
| `DE-01` Acceso inicial | Autenticación de riesgo, intentos repetidos o acceso remoto fuera de patrón. | Identidad, MFA, IP/dispositivo, hora, sesión, cambio de geografía y acceso aprobado. | Privilegio afectado o uso desde dispositivo no confiable → IR/identidad. |
| `DE-02` Toma de control | Alta de privilegios, cambio de MFA/CA, consentimiento de aplicación, nueva credencial o acceso de emergencia. | Operador, cambio autorizado, alcance, sign-ins posteriores, auditoría independiente. | Cambio no aprobado en plano de identidad → incidente mayor. |
| `DE-03` Supresión | EDR/antimalware deshabilitado, exclusión nueva, borrado de logs o dispositivo fuera de línea anómalo. | Comando o evento, precedentes, ticket, telemetría alternativa. | Si coincide con acceso/lateral o activos críticos → contención urgente. |
| `DE-04` Movimiento lateral | Inicio remoto administrativo o ejecución/propagación en varios equipos. | Grafo usuario-origen-destino, proceso, autenticación, ventana de mantenimiento. | Más de un segmento o credenciales privilegiadas → IR/red. |
| `DE-05` Ataque a copias | Desactivación, borrado, cambio de retención/immutabilidad o fallos nuevos en respaldos. | Identidad, cambio, repositorio, punto recuperable previo, ticket autorizado. | Cualquier cambio no autorizado en copias críticas → proteger repositorios y escalar. |
| `DE-06` Cifrado | Cambios masivos de archivos, notas de rescate, procesos de cifrado o I/O anómala. | Host, ruta, tasa vs base, usuario, tareas legítimas de migración, archivos de muestra. | Señal creíble de cifrado/destrucción → aislamiento autorizado inmediato. |
| `DE-07` Sincronización/borrado | Borrado masivo, versionado alterado o sincronización inusual en datos críticos. | Usuario/app, biblioteca, volumen, origen, ventanas de cambio y preservación de versiones. | Alcance multisitio o repositorio crítico → detener propagación según plan. |
| `DE-08` Exfiltración | Transferencia/compartición de datos sensible fuera de patrón. | Cantidad, clasificación, destinatario, dispositivo, ruta y autorización del negocio. | Datos regulados o transferencia sostenida no autorizada → IR/Legal. |
| `DE-09` Control remoto | Destino de red o tráfico saliente sospechoso asociado con otra señal. | Dominio/IP, proceso, DNS, proxy, reputación y uso legítimo del destino. | Correlación con `DE-01/04/06` → bloquear indicador tras verificación. |
| `DE-10` Disponibilidad | Pérdida de servicio crítico, caída de identidad o acumulación de errores de acceso. | Estado del negocio, dependencias, cambios y confirmación de plataforma. | RTO amenazado → CI y continuidad, aun sin prueba de malware. |
| `DE-11` Ceguera | Falta de logs/heartbeats, caída de sensor o desfase de reloj. | Universo, última hora válida, cambio aprobado, monitoreo alternativo. | Si coincide con otras señales o afecta control crítico → tratar como incidente. |
| `DE-12` Aviso humano | Usuario, proveedor o tercero reporta nota de rescate, archivos inaccesibles o exigencia de extorsión. | Canal seguro, prueba mínima, hora y sistemas afectados; preservar mensaje original. | Abrir caso de inmediato; no esperar confirmación técnica para avisar al CI. |
| `DE-13` IA y agentes | Prompt injection indirecto, invocación anómala de herramientas/MCP, acceso masivo por agente o fuga hacia Shadow AI. | Identidad del agente/usuario, origen del prompt/archivo, alcance Graph/RBAC y alertas DLP/DSPM. | Suspender agente/conector (`PB-07`), preservar trazas y pasar proceso crítico a operación sin IA (`K56`). |

Cada `DE-*` tiene registro de regla/fuente y prueba en `02-Operacion-y-pruebas.xlsx` / `Detecciones`. El uso de `DE-07` es independiente de `DE-06`: un incidente de extorsión puede no cifrar nada. Ajustar el nombre de campos/eventos a los productos instalados; no crear falsos “silencios” porque una fuente no existe.

## 3. Triage reproducible: abrir, verificar, decidir

1. **Abrir y asegurar canal.** Dar ID, conservar alerta original, UTC de evento/ingesta/recepción, identidad, host, volumen, origen y operador. Verificar salud de sensor para no tratar ausencia de eventos como ausencia de ataque.
2. **Comprobar contexto permitido.** Contrastar mantenimiento y cambio aprobado, proceso de negocio, criticidad y dueño; buscar al menos otra evidencia independiente cuando el tiempo lo permita. Una única coincidencia de nombre/IP no prueba ransomware.
3. **Delimitar hipótesis.** Enumerar sistemas confirmados, posiblemente afectados y aún no revisados; privilegiados/respaldos/datos; posible exfiltración; y ruta de propagación. Marcar lo desconocido en vez de clasificarlo “limpio”.
4. **Escalar con criterio de negocio.** Cifrado en curso, borrado de copias, credencial de alta autoridad, exfiltración creíble o función crítica degradada activan al CI, aun si el vector inicial no se conoce. Registrar a quién se avisó, UTC y respuesta.
5. **Solicitar intervención:** proponer aislamiento/acceso/egress según [05-Respuesta-y-repudio.md](05-Respuesta-y-repudio.md), indicando objetivo, radio de impacto, prerrequisitos, autorizador, plan de reversión y cómo verificar cese de actividad. Preservar evidencia en paralelo.
6. **Revisar el resultado:** confirmar en dos vías (acción completada en la plataforma **y** telemetría de no propagación) con ventana de observación aprobada. Si no se puede verificar, mantener incidente abierto y escalar.

Cerrar como falso positivo solo si se identifica actividad legítima con evidencia, responsable y motivo de ajuste; conservar la alerta para auditoría. **No** suprimir permanentemente un caso de uso para cerrar el ticket. Un hallazgo legítimo residual abre acción del plan aunque no sea ransomware.

## 4. Operación por cadencia

| Frecuencia | Acción y evidencia |
|---|---|
| Cada turno o diariamente, según guardia | Salud de fuentes críticas, cola de alertas de alta severidad, acceso al canal fuera de banda y suplentes. |
| Semanalmente | Cambios de reglas, falsos positivos/negativos, nuevas fuentes y cuentas privilegiadas, fallos de respaldo y excepciones vigentes. |
| Trimestralmente | Simulaciones benignas de `DE-*`, denominadores de cobertura, latencia desde evento a alerta, prueba de escalamiento y actualización de escenarios. |
| Tras incidente/ejercicio | Cronología de detección → triage → contención, huecos de logs, eficacia de indicadores y lecciones con propietario. |

El SOC reporta **mediana y percentiles**, además de casos que superaron el objetivo acordado; una media favorable puede ocultar un retraso crítico. Para fórmulas, denominadores y pruebas véase [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md). Sin datos medidos, mostrar `Sin datos`, nunca “0 minutos” o “100 %”.

## 5. Correlación con tablas Full Microsoft, KPIs y módulos Ninja

| Detección | Fuentes y tablas de referencia | Motor Full Microsoft | KPIs y rituales | Playbook | Módulos `PKG-NINJA` |
|---|---|---|---|---|---|
| `DE-01` | `SRC-01;SRC-03` · `SigninLogs, AADUserRiskEvents, IdentityLogonEvents` | Entra ID Protection + Defender for Identity + Sentinel UEBA | `K33;K42;K43` · `R03;R04` | `PB-02` | NT-03 03_Entra_Identidad_y_Agentes [M1,M2,A2] (28h) · NT-02 02_Defender_XDR [I6,M5] (13h) · NT-01 01_Sentinel [M7,M11] (14h) |
| `DE-02` | `SRC-01;SRC-06` · `AuditLogs, IdentityDirectoryEvents, CloudAppEvents` | Entra PIM Alerts + Defender XDR + Sentinel NRT | `K34;K42;K45;K50` · `R04;R16` | `PB-02;PB-05` | NT-03 03_Entra_Identidad_y_Agentes [M3,M5,A1,A5] (34h) · NT-02 02_Defender_XDR [M4,A8] (22h) · NT-01 01_Sentinel [M7] (10h) |
| `DE-03` | `SRC-02;SRC-07` · `DeviceEvents, DeviceRegistryEvents, SecurityEvent (1102), Heartbeat` | Defender for Endpoint Tamper Protection + Sentinel Health | `K41;K42;K43` · `R04` | `PB-01` | NT-02 02_Defender_XDR [M3,M10,A3] (26h) · NT-01 01_Sentinel [M12] (4h) |
| `DE-04` | `SRC-01;SRC-02;SRC-03` · `DeviceLogonEvents, DeviceProcessEvents, IdentityLogonEvents` | Defender for Identity + Defender XDR Attack Disruption | `K36;K42;K45;K55` · `R03;R04` | `PB-01;PB-02` | NT-02 02_Defender_XDR [M4,M7,M9,A8] (36h) · NT-03 03_Entra_Identidad_y_Agentes [A2] (12h) · NT-14 14_Defender_for_Cloud [M3,A7] (13h) |
| `DE-05` | `SRC-02;SRC-04;SRC-06` · `AddonAzureBackupAlerts, AzureActivity, DeviceProcessEvents (vssadmin/wbadmin)` | Azure Backup Alerts + Resource Guard + Defender for Endpoint + Sentinel NRT | `K28;K42;K45` · `R04;R17` | `PB-03` | NT-14 14_Defender_for_Cloud [M6,M7,A3,A4] (26h) · NT-02 02_Defender_XDR [M3,M10] (18h) · NT-01 01_Sentinel [M7,M13] (16h) |
| `DE-06` | `SRC-02;SRC-04;SRC-05` · `DeviceFileEvents, DeviceProcessEvents, SecurityAlert, StorageBlobLogs` | Defender XDR Automatic Attack Disruption + MDE Controlled Folder Access + Defender for Storage | `K42;K45;K55` · `R04;R22` | `PB-01` | NT-02 02_Defender_XDR [M1,M3,M7,A1,A8] (44h) · NT-14 14_Defender_for_Cloud [W2,A3] (14h) |
| `DE-07` | `SRC-05` · `OfficeActivity, CloudAppEvents` | Defender for Cloud Apps + SharePoint/OneDrive Ransomware Detection + Purview Audit | `K28;K37;K42;K45` · `R04;R17` | `PB-04` | NT-10 10_Purview_eDiscovery_y_Audit [I2,M3,A3] (16h) · NT-09 09_Purview_Ciclo_de_vida_y_Registros [I2,A4] (7h) · NT-02 02_Defender_XDR [M1] (6h) |
| `DE-08` | `SRC-03;SRC-05` · `CloudAppEvents, DeviceNetworkEvents, Purview DLP/IRM Alerts, OfficeActivity` | Purview DLP + Purview Insider Risk Management + Defender for Cloud Apps | `K37;K42;K45;K61;K64` · `R03;R04;R20` | `PB-04` | NT-06 06_Purview_DLP [I3,M2,M4,A2] (25h) · NT-07 07_Purview_Insider_Risk [M1,M2,A2] (20h) · NT-05 05_Purview_Information_Protection [A4] (5h) |
| `DE-09` | `SRC-02;SRC-03` · `DeviceNetworkEvents, DeviceProcessEvents, CommonSecurityLog, DnsEvents` | Defender for Endpoint Network Protection + Defender TI + Sentinel Analytics | `K42;K43;K45` · `R03;R04` | `PB-01;PB-05` | NT-02 02_Defender_XDR [M3,M9,A3] (24h) · NT-01 01_Sentinel [M4,M7,M10] (23h) · NT-04 04_Security_Copilot [M2] (4h) |
| `DE-10` | `SRC-01;SRC-06;SRC-07` · `AzureActivity, SigninLogs, Heartbeat, alertas de monitoreo/servicio` | Sentinel + Azure Monitor + tablero operativo del SOC/plataforma | `K05;K21;K29;K47` · `R04;R32;R34` | `PB-03` | NT-01 01_Sentinel [M8,M9] (10h) · NT-02 02_Defender_XDR [S2] (6h) · NT-14 14_Defender_for_Cloud [B6,A3] (12h) |
| `DE-11` | `SRC-07` · `Heartbeat, SentinelHealth, Usage, AzureActivity (DiagnosticSettings)` | Sentinel Health & Audit + Defender XDR Sensor Health | `K41;K42` · `R04;R06` | `PB-01` | NT-01 01_Sentinel [M3,M12] (10h) · NT-02 02_Defender_XDR [I4,S3] (12h) · NT-03 03_Entra_Identidad_y_Agentes [M6] (8h) |
| `DE-12` | `SRC-08` · `Tickets SOC, reporte de usuario, notificaciones de proveedor en Sentinel` | Flujo de escalamiento SOC + canal fuera de banda + Purview eDiscovery hold | `K05;K11;K61;K62` · `R04;R07;R33` | `PB-01;PB-04` | NT-02 02_Defender_XDR [S2] (6h) · NT-10 10_Purview_eDiscovery_y_Audit [M1,A3] (11h) · NT-08 08_Purview_Communication_Compliance [I3] (4h) |
| `DE-13` | `SRC-09;SRC-05;SRC-01` · `CopilotInteraction, CloudAppEvents, Alertas Defender for AI, SigninLogs (Agent)` | Defender for Cloud AI Threat Protection + Defender XDR for Copilot + Purview DSPM/DLP for AI | `K49;K50;K52;K53;K54;K56` · `R03;R04;R16;R37` | `PB-07` | NT-12 12_Purview_DSPM_y_Seguridad_de_datos_para_IA [M1,M2,M3,A1,A4] (34h) · NT-13 13_Seguridad_de_Copilot_y_Copilot_Studio [A1,A4,A5,A8] (28h) · NT-15 15_Seguridad_de_agentes_de_IA_en_Foundry [M3,A2,A3,A5] (27h) |

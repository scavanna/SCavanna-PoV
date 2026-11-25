# 05. Respuesta temprana, contención e invalidación del acceso adversario (v2.0 · PB-01 a PB-07)

**“Repudio” en este paquete significa impedir y verificar la pérdida del acceso adversario**, no negar hechos ni garantizar invalidación criptográfica inmediata. Este runbook se activa ante una **sospecha creíble**; el CI autoriza el perímetro y el dueño técnico ejecuta. Registrar cada cambio en `02-Operacion-y-pruebas.xlsx` / `Decisiones` y `Incidentes`. No ejecutar acciones desde el HTML: su función es recordar pasos y exportar notas locales.

## 1. Invariantes de intervención

- **Personas y seguridad primero.** Identificar sistemas físicos, médicos, industriales y servicios esenciales antes de cortar comunicaciones; coordinar alternativas con el dueño de la función.
- **Contención e investigación en paralelo.** Cuando hay propagación activa, ejecutar el mínimo aislamiento autorizado sin esperar imagen forense completa; preservar lo que no retrase esa decisión [MS-05].
- **No apagar de forma rutinaria.** Un apagado puede perder memoria, claves y conexiones; aislar un equipo afectado suele preservar mejor evidencia, salvo criterio técnico/seguridad que exija otra cosa [MS-05, MS-06].
- **Perímetro preciso.** Describir activo, identidad, segmento, aplicación, respaldo y terceros tocados, junto con dependencias. Evitar bloqueos de todo el tenant o dominio sin valorar continuidad.
- **Confirmación independiente.** “Comando aceptado” no significa “acceso terminado”. Revisar acción, nuevos inicios de sesión, actividad de datos, tráfico y alertas hasta el punto de decisión fijado.

## 2. Bucle común de cada playbook

1. Abrir ID de incidente y recopilar fuente, UTC, confianza, afectados confirmados/posibles, criticidad y alternativa operativa. Informar al CI y custodio.
2. Elegir **acción mínima eficaz**, daño potencial si no se actúa, impacto colateral y ámbito autorizado. Registrar quién decidió, quién operó y cuándo.
3. Preservar registros ya disponibles y la configuración previa cuando sea seguro; si hay cifrado en curso, actuar y documentar por qué la captura previa no era viable.
4. Ejecutar mediante consola/herramienta corporativa autorizada, nunca con ejemplos genéricos sin comprobar permisos y alcance. Registrar identificador de tarea y resultado.
5. Verificar efecto con telemetría y negocio; ampliar o corregir alcance si persisten accesos. Mantener vigilancia de nuevos tokens, cuentas, agentes, claves y sesiones.
6. Documentar criterio de reversión: dueño, estado previo, orden seguro para reactivar, prueba de limpieza, impacto y aprobación del CI/negocio. No reactivar solo porque desapareció una alerta.

## 3. Tarjetas de contención

| Playbook, disparador | Acción inicial autorizada | Verificación, evidencia y límite |
|---|---|---|
| `PB-01` Equipo con cifrado, proceso de propagación o telemetría convergente (`DE-03/04/06`). | Identificar origen y equipos de propagación; aislar por EDR o red en el alcance permitido. Conservar respuesta del agente y coordinar acceso forense alternativo. | Confirmar estado real de aislamiento y ausencia de nueva comunicación lateral; conservar alertas, árbol de procesos y eventos. No apagar por defecto ni aislar un servicio esencial sin ruta de continuidad [MS-05, MS-06]. |
| `PB-02` Usuario privilegiado o sesión sospechosa (`DE-01/02`). | Proteger primero un acceso administrativo **limpio**; bloquear nuevos accesos, revocar sesiones/refresh tokens cuando aplique, reestablecer credenciales desde dispositivo confiable y revisar grupos, métodos MFA y delegaciones. | Intentos posteriores, tokens válidos, auditoría de privilegios y aplicaciones; sincronizar revocación en AD/Entra y SaaS según arquitectura. Un token de acceso existente o cookie de la aplicación puede seguir activo [MS-10]. |
| `PB-03` Repositorio/administración de respaldos atacado (`DE-05`). | Restringir acceso administrativo y borrado en perímetro definido, inmovilizar copias sanas y proteger claves/documentación de recuperación. Evaluar desconexión de sistemas online antes de cualquier interrupción. | Puntos recuperables anteriores al compromiso, integridad, acceso del adversario y disponibilidad del servicio. No borrar logs de backup ni desconectar sin evaluar replicación, monitoreo y RTO [MS-05, MS-07]. |
| `PB-04` Datos/sincronización o exfiltración (`DE-07/08`). | Congelar cambios peligrosos al repositorio, compartición o sincronización de dispositivos afectados según producto y política; bloquear destinos confirmados, preservar auditoría y versiones. | Delimitar archivos, identidades, enlaces, apps y destino; confirmar que cesa el flujo y que hay copia íntegra. Legal evalúa exposición sin anticipar obligaciones ni afirmar “sin robo” [MS-05, MS-08]. |
| `PB-05` Claves, aplicaciones o terceros abusados (`DE-02/09`). | Suspender privilegio o integración comprometida, rotar secretos/certificados bajo control dual, revocar sesiones en el proveedor y limitar egress sin interrumpir servicios esenciales. | Confirmar tareas/servicios aún funcionales, credenciales nuevas propagadas, accesos antiguos fallidos y sesiones propias de apps invalidadas; coordinar con propietario/tercero [MS-10]. |
| `PB-06` Medida ya aplicada con alcance erróneo o falso positivo. | Conservar estado y evidencia, obtener aprobación de CI/negocio, corregir alcance mínimo y recuperar mediante procedimiento de reversión. | Volver a medir salud y riesgo adversario; no descartar el incidente si persiste una hipótesis plausible. |
| `PB-07` Copiloto, agente autónomo o conector MCP comprometido (`DE-13`). | Bloquear identidad en Entra Agent ID / Agent 365, desactivar agente/herramienta en Copilot Studio o Foundry, cortar fuentes contaminadas y activar operación sin IA (`DD18`). | Preservar `CopilotInteraction` y trazas en Purview Audit; verificar que no queden credenciales OBO/service principals activos y confirmar continuidad del proceso (`K50, K55, K56`). |

Si el EDR no puede aislar, disponer de rutas alternativas **preaprobadas** (red, hipervisor, acceso remoto, proveedor). Registrar cuál funcionó; no presumir equivalencia entre controles.

## 4. Revocación: matriz de superficies

| Superficie | Verificar al responder | Riesgo residual |
|---|---|---|
| Usuario AD/híbrido | Estado de cuenta, replicación, contraseñas, sesiones remotas y roles. | Equipos o dominios no sincronizados y tickets ya emitidos. |
| Microsoft Entra | Bloqueo de cuenta, revocación de refresh/sesiones y roles/permisos. | Access tokens vigentes hasta expiración o evaluación continua compatible [MS-10]. |
| SaaS/aplicación | Sesiones/cookies propias, sesiones locales y cuentas sin SSO; soporte del proveedor. | Entra no puede revocar por sí sola la cookie emitida por otra aplicación [MS-10]. |
| Servicio/API | Secretos, certificados, identidades administradas, integraciones y permisos delegados. | Rotación incompleta interrumpe negocio o deja credenciales aceptadas. |
| Dispositivo | Acceso local/caché, EDR, conexión, contenido sincronizado. | Equipo desconectado conserva datos locales; borrado remoto puede destruir evidencia y requiere autorización específica. |
| Agente de IA / conector MCP | Estado en Entra Agent ID / Agent 365, permisos Graph/RBAC, conectores Copilot Studio/Foundry y credenciales delegadas (OBO). | Desactivar la interfaz del chat no revoca tokens de un service principal subyacente ni limpia documentos envenenados en el índice RAG. |

No usar “cuenta bloqueada” como cierre: probar desde un cliente controlado que los nuevos accesos fallan y revisar eventos de la sesión anterior hasta el plazo acordado. Mantener acceso de emergencia legal y trazable durante la recuperación.

## 5. Paso a erradicación, recuperación y cierre

IR define hipótesis de entrada, persistencia, alcance y potencial exfiltración; forense preserva fuentes; ingeniería construye imagen/configuración confiable; identidad rota credenciales afectadas; respaldos validan punto limpio. Una vez comprobado, el CI aprueba pasar a [07-Continuidad-y-recuperacion.md](07-Continuidad-y-recuperacion.md). En caso de alcance incierto, activar operación degradada y registrar riesgo, no reconectar por presión de tiempo sin aceptar formalmente el residuo.

**Criterio de contención:** no se observa nueva propagación dentro del alcance razonablemente vigilado, se restringieron las rutas conocidas, se preservó evidencia crítica y queda vigilancia de persistencia. **No equivale a declarar el entorno libre de atacantes.** [06-Evidencia-y-forense.md](06-Evidencia-y-forense.md) detalla custodia; [08-Comunicaciones.md](08-Comunicaciones.md) controla cualquier mensaje externo.

## 6. Mapeo de playbooks con derechos de decisión CISO 365, Full Microsoft y Ninja Training

| Playbook | Disparadores | Decisiones `DD##` | Ejecución en stack Full Microsoft | KPIs impactados | Entrenamiento `PKG-NINJA` |
|---|---|---|---|---|---|
| `PB-01` | `DE-03;DE-04;DE-06;DE-09;DE-11;DE-12` | `DD10;DD11` | MDE Device Isolation (Full/Selective), Live Response, bloqueo de indicadores en MDE/Firewall y Automatic Attack Disruption en Defender XDR; preservar memoria/paquete forense sin apagar por defecto. | `K05;K32;K45;K55` | NT-02 02_Defender_XDR [M3,M7,A1,A2,A8] (48h) · NT-14 14_Defender_for_Cloud [A3,A5] (15h) |
| `PB-02` | `DE-01;DE-02;DE-04;DE-11` | `DD10;DD11` | Asegurar canal admin limpio (break-glass), deshabilitar usuario en AD/Entra, doble reset de contraseña AD (KRBTGT según alcance), Revoke-MgUserSignInSession, CAE, revisión de MFA/PIM/reglas de buzón y sesiones de apps no federadas. | `K05;K32;K33;K34;K45` | NT-03 03_Entra_Identidad_y_Agentes [M1,M2,M3,A2,A5] (46h) · NT-02 02_Defender_XDR [M4,M5,A8] (30h) |
| `PB-03` | `DE-05;DE-10` | `DD11;DD14` | Bloquear cambios destructivos con Multi-User Authorization / Resource Guard, aislar red de gestión de backup si persiste amenaza activa, verificar inmutabilidad WORM y preservar último punto limpio e inventario de claves. | `K28;K30;K45;K47` | NT-14 14_Defender_for_Cloud [M6,M7,A3,W2,W4] (32h) · NT-09 09_Purview_Ciclo_de_vida_y_Registros [A4] (3h) |
| `PB-04` | `DE-07;DE-08;DE-12` | `DD11;DD12` | Pausar/bloquear clientes OneDrive comprometidos, cortar sesiones de descarga en Defender for Cloud Apps, aplicar bloqueo DLP/Adaptive Protection, preservar Audit/eDiscovery hold y evaluar Microsoft 365 Backup / Files Restore tras erradicar. | `K37;K45;K57;K61;K64` | NT-06 06_Purview_DLP [I3,M2,M4,A2] (25h) · NT-07 07_Purview_Insider_Risk [M2,M3] (11h) · NT-10 10_Purview_eDiscovery_y_Audit [M1,M3,M4,A3] (21h) |
| `PB-05` | `DE-02;DE-09` | `DD11;DD15;DD16` | Deshabilitar Enterprise App / Service Principal, revocar consentimientos OAuth y tokens, rotar secretos/certificados en Key Vault bajo control dual, suspender acceso Entra B2B/Private Access del proveedor afectado. | `K27;K31;K34;K45;K62` | NT-03 03_Entra_Identidad_y_Agentes [M4,M5,M8,A1,A5] (48h) · NT-14 14_Defender_for_Cloud [M7,W4] (12h) |
| `PB-06` | `Falso positivo o impacto desproporcionado` | `DD11;DD14` | Preservar evidencia del estado previo, validar con CI y dueño de negocio, revertir por tramos verificando telemetría limpia y actualizar regla/exclusión temporal con vencimiento. | `K03;K06;K45;K63` | NT-02 02_Defender_XDR [M10,S2] (16h) · NT-01 01_Sentinel [M13] (6h) |
| `PB-07` | `DE-13` | `DD11;DD17;DD18` | Deshabilitar identidad en Entra Agent ID / Agent 365, desactivar agente o conector MCP en Copilot Studio / Foundry, bloquear ingesta de fuentes contaminadas, preservar prompts/trazas en Purview Audit y activar procedimiento operativo sin IA. | `K50;K52;K53;K55;K56` | NT-03 03_Entra_Identidad_y_Agentes [X2,X3,X4] (17h) · NT-13 13_Seguridad_de_Copilot_y_Copilot_Studio [M5,A1,A4,A8] (28h) · NT-15 15_Seguridad_de_agentes_de_IA_en_Foundry [M1,M4,A4,A5] (28h) |

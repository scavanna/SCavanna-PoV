# 07. Contingencia, continuidad y recuperación confiable (v2.0 · Azure Backup/ASR, M365 Backup y modo sin IA)

**Objetivo:** sostener o restablecer funciones críticas dentro de los objetivos aprobados, sin reintroducir al atacante. El dueño de negocio decide la prioridad y acepta el retorno; el CI coordina con identidad, respaldo, plataforma y forense. Un respaldo exitoso no demuestra por sí solo que el servicio o sus dependencias son recuperables [MS-02, MS-07].

## 1. Preparación anterior al incidente

Para cada proceso de `01-Evaluacion-y-controles.xlsx` / `BIA` documentar dueño y suplente, función mínima viable, **RTO** (desde interrupción hasta servicio aceptado), **RPO** (máxima antigüedad de datos tolerada), punto a partir del cual se activa contingencia, dependencia de identidad/DNS/red/proveedor, prioridad relativa, secuencia de restauración y plan de reconciliación de transacciones. El dueño firma objetivos y excepción si la capacidad ensayada no los cumple.

Conservar fuera de la zona comprometida: procedimientos, configuración de infraestructura como código cuando aplique, diagramas, inventarios, medios de instalación confiables, copias aisladas/inmutables, instrucciones de acceso de emergencia y canal para contactar a los equipos. Segregar credenciales y llaves conforme a la política de custodia. Probar restauraciones de extremo a extremo, no solo “job de backup completado”. OneDrive/SharePoint, versionado y papelera son rutas acotadas para determinados datos, **no** reemplazos de la recuperación de identidad, aplicaciones y dependencias [MS-02, MS-08].

## 2. Activar modo contingencia

El CI y el dueño de negocio comparan hora de interrupción, RTO restante, contagio potencial, confianza en identidad y disponibilidad de rutas manuales. Activan cuando continuar conectado amplifica daño o la restauración ordinaria probablemente superará el umbral acordado. Registrar: alcance, equipos/canales alternativos, trabajos que **se suspenden** por seguridad, controles compensatorios, integridad de datos en modo manual, duración estimada, comunicación aprobada y condiciones de retorno. Aplicar principio de mínima exposición: no usar un repositorio/manual compartido que haya sido comprometido.

Ejemplos de capacidades alternativas a decidir localmente: recepción manual con numeración de transacciones, plataforma de reserva aislada, proveedor de contingencia con credenciales limpias o suspensión controlada de operaciones. **No asumir** que un procedimiento manual conserva requisitos de privacidad, seguridad física o regulación; validar con Legal y los dueños.

## 3. Recuperar en una zona confiable

1. **Fijar límite de confianza:** IR define equipos y planos de control sospechosos, última actividad conocida y condiciones para admitir un nuevo entorno. Validar que el adversario no administra el mecanismo de backup o la zona de recuperación.
2. **Elegir punto de restauración:** comparar hora del posible compromiso, última copia íntegra y RPO aprobado. Si el punto limpio excede RPO, pedir al negocio decisión sobre reconstrucción/reconciliación y riesgo residual; nunca inventar datos.
3. **Restituir cimientos:** acceso de emergencia verificado, identidad, DNS, red segmentada, controles de seguridad/telemetría, repositorio de secretos y plataformas base en el orden que marque el mapa real de dependencias. Evitar ciclos de restauración; usar procedimiento aislado y firmado si el directorio original no es confiable.
4. **Reconstruir servicios:** imágenes y configuraciones confiables; parches, EDR, cuentas mínimas y rotación de credenciales antes de conexión. Restaurar datos, validar hashes/consistencia y escanear según el riesgo. Mantener servicios restaurados aislados hasta autorizar entrada.
5. **Probar funcionalmente:** negocio ejecuta transacciones críticas, verifica permisos, integridad, reconciliación de datos recibidos en modo contingencia, rutas de salida y telemetría. Medir RTO real desde interrupción y RPO real desde último dato confirmado. Registrar fallas y excepciones.
6. **Reconectar gradualmente:** CI autoriza segmento/servicio y punto de observación; IR verifica que no reaparecen controles adversarios, detecciones ni acceso no autorizado; negocio acepta disponibilidad. Mantener opción de volver a modo degradado.
7. **Cerrar y aprender:** conciliar operaciones manuales, confirmar que no quedan datos o procesos por recuperar, entregar evidencia a Legal y abrir mejoras de BIA, arquitectura y pruebas.

Si forense no puede excluir persistencia o extracción, eso limita el grado de certeza del retorno; documentar riesgo y protecciones adicionales antes de reconectar. No restablecer cuentas y relaciones de confianza antiguas solo por conveniencia.

## 4. Ficha por servicio

| Dato a completar por el dueño | Evidencia exigida |
|---|---|
| Función, prioridad, dueño/suplente, dependencias y proveedor | BIA y mapa de dependencias versionados. |
| RTO/RPO aprobados y punto de inicio/fin de medición | Firma de negocio, calendario de pruebas y tiempos medidos. |
| Copias: datos, configuraciones, credenciales protegidas y manuales | Inventario, punto íntegro, prueba de restauración y acceso separado. |
| Modo degradado: inicio, capacidad, seguridad y reconciliación | Ejercicio con transacciones de muestra y aceptación. |
| Reingreso: pruebas de negocio y seguridad, monitorización y reversión | Acta de aceptación y observación post-retorno. |

Una recuperación que funciona solo con personas, contraseñas o documentos del entorno cifrado **no** es una ruta independiente. La prueba anual en [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md) debe revelar estas dependencias; los registros viven en `02-Operacion-y-pruebas.xlsx` / `Pruebas`.

## 5. Arquitectura de recuperación Full Microsoft y alineación con CISO 365 / KPIs

| Ámbito a recuperar | Capacidad Full Microsoft de referencia | Qué NO sustituye / condición crítica | Indicadores y rituales |
|---|---|---|---|
| Infraestructura, VMs, SQL y archivos Azure/híbridos | **Azure Backup** con bóvedas inmutables bloqueadas, *Soft Delete*, *Cross-Region Restore* y **Multi-User Authorization (Resource Guard)** en suscripción/tenant separado + **Azure Site Recovery** hacia Landing Zone limpia. | No reconectar redes restauradas al dominio comprometido antes de contener y rotar secretos (`CT-02`, `CT-07`). | `K28`, `K30`, `K47` · `R17` (trimestral), `R34` (anual), `ACT-109`, `DD14`. |
| Colaboración a escala empresarial (SharePoint, OneDrive, Exchange) | **Microsoft 365 Backup** para restauración masiva rápida a punto en el tiempo; **Files Restore** (30 días) y papelera/retención **Purview** para incidentes acotados. | Ni OneDrive Sync ni Files Restore reconstruyen Active Directory, bases de datos LOB ni configuraciones SaaS (`CT-20`). | `K28`, `K30` · `NT-09 (I2, M4, A4)`, `NT-10 (M1)`. |
| Plano de identidad (AD DS y Microsoft Entra) | Procedimiento aislado de **AD Forest Recovery**, cuentas *break-glass* en Entra ID con FIDO2 y exportación como código de políticas de Acceso Condicional/grupos críticos (`NT-03 A3, A4, A5`). | No restaurar controladores desde imágenes con persistencia previa ni reutilizar KRBTGT/secretos comprometidos (`CT-03`). | `K33`, `K34`, `K30` · `R16`, `R34`. |
| Procesos críticos asistidos por IA y agentes | Desactivación selectiva en **Entra Agent ID / Agent 365 / Copilot Studio / Foundry** y paso a procedimiento manual o determinista (`PB-07`, `CT-21`). | Prohibido depender de un agente de IA sin ruta degradada probada (`K56`, E3 ≥ 50 %, E4 ≥ 75 %; `ACT-114`, `EV46`). | `K29`, `K56` · `R34`, `R37`, `NT-03 (X4)`, `NT-15 (O2)`. |

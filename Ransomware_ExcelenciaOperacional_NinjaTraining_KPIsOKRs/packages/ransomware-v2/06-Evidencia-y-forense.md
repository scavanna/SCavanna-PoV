# 06. Preservación de evidencia y trabajo forense (v2.0 · Purview Audit/eDiscovery y cadena de custodia)

**Fin:** conservar integridad, contexto y cadena de custodia para responder qué ocurrió, qué se afectó y qué puede volver a ocurrir. El custodio designado y Legal definen alcance, jurisdicción, retención y transferencias. Este documento no sustituye un protocolo forense local ni faculta a entrar en sistemas sin autorización.

## 1. Decisión inmediata de preservación

Al activar IR, clasificar fuentes de mayor volatilidad y plazo de expiración: eventos y alertas del SOC, auditorías de identidad y nube, EDR/árbol de procesos, procesos/conexiones en memoria, logs de proxy/VPN/DNS, cambios de privilegios, archivos y metadatos de respaldo, notas de rescate y comunicaciones con terceros. Poner bajo conservación el caso y las evidencias disponibles; solicitar retención legal cuando corresponda. Si aislar o revocar evita daño en curso, hacerlo sin esperar una adquisición completa, **anotando lo no preservado y por qué** [MS-05].

No ejecutar herramientas de terceros no aprobadas sobre evidencia, no abrir muestras de malware en equipos de operación y no alterar el original para facilitar lectura. Para memoria volátil o adquisición de discos, usar personal entrenado, procedimientos del entorno y análisis del impacto operativo. El EDR puede recoger un paquete de investigación, pero su éxito y alcance deben verificarse [MS-06].

## 2. Registro mínimo por objeto

| Campo | Qué consignar |
|---|---|
| `EV-ID` y `INC-ID` | Identificadores estables, caso/pedido de retención asociado. |
| Fuente y alcance | Sistema, tenant, repositorio, dispositivo o proveedor, intervalo UTC y filtros exactos. |
| Origen y método | Herramienta/versión aprobada, operador, autorización, estado original, formato y ruta aprobada de extracción. |
| Marcas de tiempo | Evento, captura, recepción y transferencia en UTC; origen horario y desajuste conocido. |
| Integridad | Hash SHA-256 cuando aplica, tamaño y nombre de archivo; si una API genera evidencia no descargable, identificador y constancia de integridad del proveedor. |
| Custodia | Quién tuvo acceso, cuándo, propósito, a quién se entregó, canal y comprobación de recepción. |
| Protección | Clasificación, cifrado, permisos mínimos, retención/hold y fecha de revisión por Legal. |
| Limitaciones | Datos ausentes, sensor apagado, expiración, muestreo, error de sincronización, pérdida de volatilidad. |

Crear **un registro por copia o transformación** y conservar la relación con el original. Un hash prueba igualdad de bytes de la copia hasheada, **no** que la fuente haya sido genuina ni que la captura sea completa. No reutilizar la hoja de cálculo compartida para adjuntar bytes de evidencia; guardar archivos en repositorio forense aprobado y referenciarlos por ID/ruta restringida en `02-Operacion-y-pruebas.xlsx` / `Evidencia`.

## 3. Cadena de custodia en operación

1. Capturar identificación del activo, UTC, estado (encendido/aislado), relación con el incidente, responsable y permiso. Documentar cambios ya hechos por contención.
2. Preservar logs con filtros y ventanas suficientes para investigación de acceso inicial, escalamiento, propagación, borrado de copias y salida de datos; incluir fuentes que **no** entregaron eventos y su razón.
3. Calcular integridad de exportaciones cuando es posible y depositarlas en almacenamiento aprobado, con control de acceso, cifrado, auditoría y copia de conservación. No confiar solo en una URL de descarga temporal.
4. Antes de cada transferencia, registrar origen, destino, fecha UTC, canal, remitente, receptor, propósito e integridad verificada. Si falla hash o falta un objeto, detener uso probatorio de esa copia, preservar el error y recapturar sin sobrescribir.
5. Analizar **copias de trabajo** en un entorno segregado; notas de hallazgo enlazan `EV-ID`, herramienta, versión, criterios, confianza y contraejemplos. No convertir una correlación temporal en prueba de causalidad o atribución.
6. Al terminar la necesidad operativa, Legal define conservación, acceso y disposición según jurisdicción, contratos y solicitudes regulatorias/penales. No eliminar respaldos o logs bajo hold para liberar espacio.

## 4. Preguntas de investigación y resultado

El informe forense separa (a) hechos observados, (b) inferencias con soporte, (c) hipótesis abiertas y (d) lagunas por falta de telemetría. Responde, con fechas UTC y `EV-ID`: acceso inicial posible; identidades, endpoints y aplicaciones usadas; modificaciones en defensas y copias; persistencia y acceso residual; sistemas y datos efectivamente afectados; límites de posible extracción; hora de primera/última actividad observada; y confianza. **No afirmar ausencia de exfiltración solo porque no se encontró una alerta.**

Compartir resultados con el CI y Legal mediante repositorio autorizado; Comunicaciones recibe hechos aprobados para la audiencia, no muestras, credenciales ni datos de víctimas. Consultar [08-Comunicaciones.md](08-Comunicaciones.md). Las pruebas anuales deben incluir al menos un objeto con captura, hash, transferencia y recuperación de la copia por otra persona [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md).

## 5. Instrumentación forense sobre un cliente Full Microsoft y referencias canónicas

- **Configuración previa indispensable (`CT-14`, `F2/H60` → `F4/H180`):** la evidencia en nube no se improvisa durante el ataque. Verificar en `ACT-033` y `ACT-091` que **Microsoft Purview Audit (Standard y Premium)** esté activo, con retención de al menos 1 año para usuarios/sistemas críticos, eventos de alta importancia (`MailItemsAccessed`, `FileAccessed`, `CopilotInteraction`) y exportación a **Microsoft Sentinel** / almacenamiento inmutable (**Azure Blob WORM**).
- **Custodia y preservación legal:** usar **Purview eDiscovery (Premium)** (`NT-10 M1, M2, M4`) para colocar custodios, buzones, sitios SharePoint, OneDrive y Teams bajo *Legal Hold* sin avisar al adversario, combinándolo con **Purview Data Lifecycle & Records** (`NT-09 A3, A4`) para impedir purgas. En endpoints y servidores usar **MDE Investigation Package** y biblioteca controlada de **Live Response** (`NT-02 M3, A1`).
- **Trazabilidad con `PKG-CISO365` y `PKG-KPI-OKR`:** alimenta `K03` (reconstrucción de decisiones), `K57` (obligaciones con evidencia vigente, E3 ≥ 70 %, E4 ≥ 85 %), `K60` (controles probados) y prácticas `EV09`, `EV11`, `EV41` y `EV43` (revisión posincidente `R51`).

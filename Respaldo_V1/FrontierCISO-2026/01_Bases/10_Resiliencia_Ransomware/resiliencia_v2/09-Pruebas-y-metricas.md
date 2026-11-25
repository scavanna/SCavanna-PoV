# 09. Ensayos mínimos, evaluaciones periódicas y métricas (v2.0 · conectado a H270, KPIs/OKRs y Ninja Training)

**Objetivo verificable:** el personal comprende **y puede ejecutar** detección, escalamiento, autorización, contención, preservación, continuidad, restauración y comunicación bajo una falla realista. Una sesión informativa o un quiz no sustituyen una prueba de ejecución. Los resultados se registran en `02-Operacion-y-pruebas.xlsx` / `Pruebas`, con datos de `01-Evaluacion-y-controles.xlsx`.

## 1. Programa mínimo por frecuencia

| Cadencia | Prueba/entregable obligatorio | Evidencia y criterio de resultado |
|---|---|---|
| **Al inicio del programa** | Assessment de BIA, `CT-01` a `CT-20`, universo/lagunas, autoridades, canales y plan de brechas. | Informe firmado, controles sin evidencia como `No evaluado`, propietarios y fechas [02-Evaluaciones.md](02-Evaluaciones.md). |
| **Cada trimestre** | Revisión completa de deriva; comprobar salud/cobertura de telemetría y respaldos, al menos una señal por dominio crítico, contacto de suplente, una decisión de aislamiento/revocación simulada y una restauración de muestra o prueba incremental segura. | Fecha, operador, universo, log/alerta, resultado, riesgo residual; una falla abre remediación. No interrumpir producción fuera de ventana autorizada. |
| **Al menos una vez cada 12 meses** | **E1: ejercicio integrado** con mando, SOC, identidad, plataformas, backup, negocio, forense, Legal y Comunicaciones; usar inyecciones de exfiltración y cifrado, respaldo amenazado, pérdida de correo, propagación y consulta externa. | Cronología de activación, hechos vs hipótesis, aprobaciones, checklist ejecutada, borradores sin envío y decisiones de continuidad. Cada titular y suplente crítico demuestra su tarea sin pistas; una ausencia se registra y se ensaya aparte dentro del ciclo anual. |
| **Al menos una vez cada 12 meses por función crítica** | **E2: restauración técnica representativa de extremo a extremo** en entorno autorizado: identidad/red, configuración, aplicación, datos y transacción de negocio; medir RTO/RPO. Repetir para cada función `crítica/tier 0` del BIA, o registrar explícitamente la excepción aceptada y su fecha de cierre. | Punto limpio e integridad, tiempo real <= RTO aprobado, pérdida real <= RPO aprobado, comprobación de negocio y seguridad, y prueba de retorno o de reversión. Un backup job exitoso no basta. |
| **En E1 y E2, o ensayo aparte dentro del año** | **E3: aislamiento y repudio + evidencia + comunicación.** Aislar objetivo benigno, revocar sesión de laboratorio, verificar cese efectivo, hacer adquisición/hash/transferencia y redactar mensajes para públicos distintos con reloj legal simulado. | Preaprobación, efecto y reversión observados, cadena de custodia recuperable, destinatarios/formatos simulados y aprobaciones; cero comunicaciones reales a terceros. |
| **Tras cambio material o incidente** | Repetir el tramo afectado sin esperar el trimestre/año. | Falla original vinculada con prueba de regresión y aprobación de cierre. |

El programa anual puede unir **E1, E2 y E3 en una secuencia** si la restauración es técnica, representativa y medible, no un relato sobre cómo se haría. Si falta uno de los componentes, la afirmación “respuesta ensayada de punta a punta” no es válida. No se declaran universales tiempos como “15 minutos”: cada objetivo se fija antes de la prueba, según BIA, capacidad y requisitos locales.

## 2. Guion de ejercicio integrado E1

**Preparación (planificar y autorizar):** escenario, alcance benigno, participantes/suplentes, observadores independientes, permisos, ventana, reglas de parada, datos de prueba, métricas objetivo y medio para inyectar eventos sin dañar producción. Separar mensajes simulados de canales reales. Elegir un proceso crítico con dependencia de identidad y proveedor para descubrir cadenas incompletas.

**Inyecciones, en orden variable para no enseñar una secuencia falsa:**

1. Cuenta privilegiada anómala y pérdida parcial de logs: SOC decide si existe evidencia suficiente para abrir incidente aun con ceguera.
2. Intento de manipular respaldos y movimiento lateral: CI decide autoridad y acciones mínimas, red/backup ejecutan simulación o lab con comprobación.
3. Posible exfiltración antes del cifrado: Legal pide preservar datos, separar hipótesis y evaluar disparadores de notificación.
4. Cifrado en un sistema de prueba y caída del correo: guardia convoca por canal alternativo; negocio valora contingencia.
5. Solicitud de cliente, prensa y fuerzas de la ley/regulador: Comunicaciones redacta versiones distintas y Legal valida reloj/jurisdicción simulados.
6. Copia limpia disponible pero identidad original sospechosa: equipo reconstruye entorno de prueba, mide RTO/RPO y negocio acepta o rechaza retorno.

Observar **quién** tomó cada decisión y con qué evidencia, no solo “qué botón se oprimió”. Registrar detección, triage, declaración, contención confirmada, captura, transición a contingencia, inicio/fin de restauración y aprobación de mensajes en UTC.

### Rúbrica individual para comprobar comprensión

El observador entrega a **cada titular y suplente** una inyección adecuada a su función sin anunciar la respuesta. Registra por persona/rol en `Competencias` del segundo Excel si puede **explicar el disparador, actuar dentro de autoridad, demostrar la tarea o una simulación técnica equivalente, reconocer cuándo detenerse, mostrar evidencia y realizar el relevo**. Exigir actuación **sin indicaciones del facilitador** para aprobar; una decisión que ponga en riesgo personas, destruya evidencia sin necesidad o divulgue datos sin autorización es un fallo crítico aunque el resto del equipo complete el escenario.

| Rol | Demostración mínima observable |
|---|---|
| SOC | Abrir caso ante señal ambigua y sensor degradado, distinguir hecho de hipótesis y escalar con UTC. |
| CI | Confirmar suplente y canal alternativo, resolver impacto/autoridad y ordenar pistas paralelas. |
| Identidad y red/endpoint | Invalidar acceso o aislar objetivo de laboratorio por ámbito, medir efecto y planear reversión; reconocer límites de tokens/cookies. |
| Backup/plataforma y negocio | Elegir punto limpio, recuperar transacción, medir RTO/RPO, activar contingencia y aceptar/rechazar retorno. |
| Forense | Registrar fuente, integridad o limitación, transferencia y ubicación protegida sin alterar original. |
| Legal/privacidad y Comunicaciones | Separar públicos, validar reloj/jurisdicción, aprobar borradores y verificar canal sin avisos reales. |

Si un rol o suplente no supera el criterio, el componente anual se registra `Incompleta` o `Fallida`; impartir corrección específica y repetir la demostración. La asistencia, lectura del manual o el puntaje de otro miembro no sustituyen esa evidencia.

## 3. Criterios de aprobación y repetición

Una prueba está `Aprobada` solo si el alcance/objetivos se fijaron antes, los titulares y suplentes críticos demostraron su rol sin pistas, las acciones disruptivas se autorizaron, se respetó la seguridad física, hubo ruta alternativa funcional, se detectó/escaló la actividad conforme a objetivos aprobados, se verificó **el efecto** de contención y su reversión, se preservó un objeto con integridad y custodio, el servicio de prueba cumplió RTO/RPO y fue aceptado por negocio, y los mensajes simulados tuvieron aprobación legal/portavoz sin envío real. Para un componente no aplicable se exige **justificación** y aprobación, no una celda vacía.

Si un criterio esencial falla: estado `Fallida` o `Incompleta`, riesgo/compensación, responsable, fecha de corrección y **retest**. No aceptar una “aprobación con reservas” como equivalente a capacidad demostrada. El comité puede aceptar temporalmente el riesgo, pero mantiene visible el fallo y su fecha.

## 4. Métricas que no esconden incertidumbre

| Métrica | Fórmula o medición y alcance | Regla de interpretación |
|---|---|---|
| BIA completo | Procesos críticos con dueño y RTO/RPO aprobados ÷ procesos críticos inventariados. | Denominador cero o inventario incompleto → `Sin datos`/brecha, no 100 %. |
| Cobertura de copia recuperable | Procesos críticos con copia independiente protegida **y** restauración E2 vigente ÷ procesos críticos inventariados. | No usar archivos sincronizados como sustituto de E2. |
| Sensor saludable | Activos que requieren señal con agente/fuente sana ÷ activos inventariados que la requieren. | Reportar exclusiones y caídas separadas. |
| Detección → alerta | UTC de emisión de alerta - UTC del primer evento conocido de la señal. | Indicar fuentes investigadas y sesgo por logs faltantes; mediana, p90 y peor caso. |
| Alerta → triage / triage → contención | UTC inicio triage - UTC alerta; UTC efecto **verificado** - UTC decisión autorizada. | No usar UTC del clic como contención efectiva. |
| Cumplimiento RTO/RPO | Por servicio: tiempo desde interrupción hasta aceptación; antigüedad de últimos datos válidos al retomar. | Comparar objetivos aprobados para el mismo servicio; sin objetivo, `No evaluable`. |
| Cadena de evidencia | Objetos con origen, UTC, integridad, acceso y transferencias trazables ÷ objetos de muestra adquiridos. | Si falla una transferencia, corregir y retestar. |
| Calidad de comunicaciones | Mensajes simulados con hechos verificados, aprobación, audiencia, reloj validado y canal seguro ÷ mensajes simulados previstos. | No cuenta un borrador no autorizado como envío o cumplimiento legal. |

Establecer denominadores y ventana de observación en la primera línea base; tendencias trimestrales comparan **el mismo perímetro**, o explican altas y bajas. El panel HTML muestra recuentos del catálogo/importación, **no** una garantía de resiliencia ni métricas temporales sin registros reales. Publicar métricas con limitaciones, fecha, fuentes y hallazgos vencidos.

## 5. Informe posprueba

El observador independiente produce: alcance y autorizaciones, cronología UTC, objetivos vs resultados, controles que funcionaron/no funcionaron, daño evitable, restricciones de la simulación, aprendizaje de roles, acciones con dueño/fecha, y fecha de repetición. El CI y el dueño de negocio firman el resultado; Legal revisa cualquier referencia a información protegida. Los ejercicios y sus exportaciones se almacenan en repositorio aprobado, no en los HTML de prueba.

## 6. Correspondencia exacta entre métricas operativas, KPIs/OKRs y rituales CISO 365

| Métrica operativa del paquete | Indicadores canónicos (`PKG-KPI-OKR`) | Meta Año 1 (`E3`) / Año 2 (`E4`) | Actividades y rituales (`PKG-CISO365`) | Validación formativa (`PKG-NINJA`) |
|---|---|---|---|---|
| BIA completo y con dueños | `K21` · `K09` · `K39` | `K21` ≥ 60 % / ≥ 80 % · `K09` ≥ 60 % / ≥ 80 % | `ACT-018, 032, 076, 112` · `R12, R23, R32` (`A1-O2-KR2`) | `NT-14 (B6, M2)` · `NT-11 (I3)` |
| Cobertura de copia inmutable y prueba `E2` | `K28` · `K30` · `K47` | `K28` ≥ 70 % / ≥ 85 % · `K30` ≥ 60 % / ≥ 80 % · `K47` ≤ 100 % RTO | `ACT-041, 055, 109` · `R17, R34` (`A1-O3-KR2`) | `NT-14 (M6, A3, W2)` · `NT-09 (A4)` |
| Operación degradada (sin TI y sin IA) | `K29` · `K56` | `K29` ≥ 50 % / ≥ 75 % · `K56` ≥ 50 % / ≥ 75 % | `ACT-109, 114` · `R34, R37` (`EV46`) | `NT-03 (X4)` · `NT-13 (O3)` · `NT-15 (O2)` |
| Salud de telemetría y cobertura crítica | `K41` · `K53` | `K41` ≥ 75 % / ≥ 90 % · `K53` ≥ 40 % / ≥ 70 % | `ACT-037, 097, 114` · `R04` (`EV37`) | `NT-01 (M2, M12)` · `NT-02 (I4, M8)` |
| Detección, hunting y contención (`DE-*`, `PB-*`) | `K42` (MTTD) · `K43` · `K44` · `K45` (MTTC) · `K55` | `K42` ≤ 24 h / ≤ 8 h · `K45` ≤ 12 h / ≤ 4 h | `ACT-037, 094, 097` · `R03, R04, R15, R22` | `NT-01` · `NT-02` · `NT-04` (certificación ≥ 80 % + `[LAB]`) |
| Ejercicio ejecutivo/integral `E1` y decisión | `K15` · `K05` · `K32` · `K06` · `K48` | `K15` ≥ 50 % / ≥ 75 % · `K05` ≤ 120 min / ≤ 60 min | `ACT-062, 099, 105, 111` · `R22, R33, R51` (`A1-O3-KR1`) | `NT-02 (A1, A8, S2, S4)` |
| Competencias de titulares y suplentes | `K12` · `K16` · `K07` | `K12` ≥ 70 % / ≥ 85 % · `K16` ≥ 60 % / ≥ 80 % | `ACT-014, 034, 081, 089` · `R02, R40, R49` (`EV28`) | Rutas `ROL-01..09` en [15-Plan-de-entrenamiento-y-recursos.md](15-Plan-de-entrenamiento-y-recursos.md) |
| Cadena de evidencia, controles y avisos | `K60` · `K57` · `K61` · `KSG01..KSG06` | `K60` ≥ 60 % / ≥ 80 % · `K61` ≥ 80 % / ≥ 95 % · `KSG01` ≥ 70 % / ≥ 85 % | `ACT-045, 107, 110, 116, 119, 126` · `R14, R20, R31, R35, R42, R43` | `NT-10 (M1..M4)` · `NT-11 (I3, A3)` |

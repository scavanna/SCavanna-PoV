# 10. Tarjetas breves para usar durante la crisis (v2.0 · con derechos DD## y control de IA PB-07)

**Cómo usarlas:** imprimir o conservar copia fuera de banda. No son autorización para modificar producción; cada rol sigue el mandato de [01-Gobierno.md](01-Gobierno.md). Marcar hora UTC, ID y operador en el registro oficial. La seguridad humana prevalece sobre la preservación de equipos.

## SOC / primera persona que recibe la alerta

- [ ] Abrir `INC-ID`; guardar alerta original y UTC (evento, recepción e ingesta).
- [ ] Confirmar fuente viva; delimitar equipos, identidades, copias, datos y función de negocio **confirmados / posibles / no revisados**.
- [ ] Ante cifrado activo, privilegios o copias atacados, exfiltración creíble o servicio crítico, avisar al CI y guardia por canal alternativo; no esperar atribución.
- [ ] Pedir acción mínima eficaz y custodio de evidencia; registrar falso positivo solo con causa verificable.
- [ ] Seguir `DE-*` en [04-Monitoreo-y-triage.md](04-Monitoreo-y-triage.md).

## Comandante de incidente

- [ ] Confirmar autoridad, suplentes, seguridad física y canal fuera de banda.
- [ ] Abrir sala de crisis y acta de hechos, hipótesis, lagunas, decisiones, riesgos y próximo informe.
- [ ] Aprobar perímetro y reversión de contención; impulsar forense, negocio y Legal **en paralelo**.
- [ ] Activar contingencia si el RTO o la integridad están amenazados; escalar al patrocinador si supera mandato.
- [ ] No declarar “resuelto” antes de verificar cese de actividad y aceptación de negocio.

## Identidad / endpoints / red

- [ ] Proteger primero un canal administrativo confiable; confirmar dependencias críticas antes de aislar.
- [ ] Aislar equipo/origen afectado por control aprobado; guardar tarea y resultado, verificar ausencia de propagación.
- [ ] Bloquear nuevos accesos y revocar sesiones donde aplique; revisar apps/cookies, secretos y credenciales de servicio por separado.
- [ ] Confirmar impacto en negocio, efectos posteriores y reversión autorizada [05-Respuesta-y-repudio.md](05-Respuesta-y-repudio.md).

## Respaldos / continuidad

- [ ] Proteger copias, repositorio, claves y procedimientos contra borrado; conservar logs de cambios.
- [ ] Elegir punto anterior al compromiso y **zona de recuperación limpia**; validar dependencias de identidad/red.
- [ ] Aplicar modo degradado aprobado y numerar las transacciones a reconciliar.
- [ ] Medir RTO/RPO desde interrupción hasta aceptación y registrar aprobación del negocio [07-Continuidad-y-recuperacion.md](07-Continuidad-y-recuperacion.md).

## Custodio forense / Legal

- [ ] Declarar hold si procede; registrar fuentes volátiles y fechas de vencimiento.
- [ ] Adquirir copia íntegra por método aprobado, SHA-256 cuando aplique, guardar en repositorio seguro.
- [ ] Registrar operador, UTC, origen, transferencias, pérdida de logs y limitaciones.
- [ ] Verificar jurisdicción, contratos, materialidad y destinatarios antes de cualquier mensaje [06-Evidencia-y-forense.md](06-Evidencia-y-forense.md), [08-Comunicaciones.md](08-Comunicaciones.md).

## Comunicaciones / portavoz

- [ ] Trabajar desde la ficha factual versionada del CI.
- [ ] Separar empleados, junta/accionistas, prensa, ley, reguladores, socios y clientes.
- [ ] Obtener aprobación Legal y corporativa pertinente; verificar destinatario y canal por vía independiente.
- [ ] Registrar mensaje exacto, hora UTC y acuse; no prometer ausencia de robo ni plazos sin base.

**Al terminar cada turno:** relevo firmado con ID, hechos, pendientes urgentes, riesgos aceptados, ubicación restringida de evidencia, próximo punto de decisión y contacto seguro. Si falta un responsable o canal, escalar antes de cerrar el relevo. En la prueba anual, cada titular y suplente demuestra su tarjeta **sin pistas** y el observador registra el resultado individual en `Competencias` [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md).

## Gobierno de IA, Copilot y agentes autónomos (`PB-07` · `DD18`)

- [ ] Identificar si el incidente involucra un agente, conector MCP, índice RAG contaminado o cuenta usada por Copilot (`DE-13`).
- [ ] Suspender identidad en **Entra Agent ID / Agent 365** o desactivar el agente en **Copilot Studio / Foundry** (`DD18`).
- [ ] Preservar `CopilotInteraction` y trazas en **Purview Audit** antes de purgar configuraciones.
- [ ] Activar procedimiento operativo **sin IA** con el dueño del proceso (`K56`) y verificar revocación de credenciales delegadas (`CT-21`).

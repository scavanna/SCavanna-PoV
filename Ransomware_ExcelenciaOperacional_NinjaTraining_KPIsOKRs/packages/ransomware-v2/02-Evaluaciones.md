# 02. Assessment inicial y revisión trimestral (v2.0 · alineado a H30/H60, EV01–EV51 y estadios E1–E5)

**Propósito:** medir preparación demostrada y convertir las brechas en decisiones verificables, sin confundir licencia, configuración, despliegue, cobertura y prueba. Se usa junto a `01-Evaluacion-y-controles.xlsx`. No se asigna un porcentaje de madurez si faltan denominadores o evidencia.

## 1. Unidad de análisis y estados

Evaluar cada proceso de negocio crítico **y** sus dependencias: identidad, DNS/red, infraestructura de virtualización/nube, aplicaciones, datos, respaldos, proveedores y canal de comunicación. Registrar alcance, propietario y sensibilidad aprobada. Un control puede estar `Probado` para un servicio y `Parcial` para el resto; no extrapolar. La hoja `BIA` recoge RTO/RPO objetivo aprobados por negocio y tiempos observados en una prueba; sin prueba, dejar observados vacíos.

| Estado | Condición verificable |
|---|---|
| `No evaluado` | No existe evidencia suficiente para concluir; es el estado inicial de todos los controles. |
| `No implementado` | El responsable confirma ausencia dentro del alcance definido. |
| `Parcial` | Hay despliegue o cobertura limitada, o falta evidencia de operación sostenida. |
| `Implementado` | Configuración, cobertura y operador comprobados, sin prueba funcional completa. |
| `Probado` | Criterio de aceptación reproducido en ensayo autorizado, con fecha, alcance, evidencia y resultado. |

Si un resultado `Probado` deja de representar la realidad por cambio de arquitectura, pérdida de sensor o vencimiento de ensayo, degradar el estado y abrir seguimiento. La evidencia puede ser política aprobada, export de configuración, inventario contra universo, alerta con UTC, ticket, hash de restauración, acta de ejercicio o aprobación; una captura aislada nunca prueba cobertura sostenida.

## 2. Assessment inicial: ejecutar una vez al activar el programa

1. **Fijar corte:** fecha UTC, patrocinador, perímetro, sedes/tenants, procesos, terceros, fuentes disponibles, excepciones y restricciones de acceso. Registrar quién evalúa y quién valida para evitar autoevaluación no revisada.
2. **Hacer BIA:** pedir al dueño de cada proceso el máximo tiempo tolerable, RTO, RPO, pérdidas por indisponibilidad y datos, dependencias técnicas y externas, ruta manual y punto de decisión de contingencia. El negocio valida los objetivos; el operador valida si son alcanzables.
3. **Recorrer cadena adversaria:** acceso inicial (correo, acceso remoto, vulnerabilidades, terceros), privilegio e identidad, movimiento lateral, desactivación de defensas, borrado de respaldos, exfiltración, cifrado, abuso de sincronización y persistencia. No convertir ejemplos en atribución de un incidente real.
4. **Verificar `CT-01` a `CT-21`:** por control revisar diseño, implementación, cobertura contra un universo conocido, telemetría, permisos, responsable, caducidad de secretos, prueba funcional y evidencia. Copias deben incluir datos **y** configuración/documentación; comprobar independencia y restauración en entorno confiable [MS-02, MS-07].
5. **Comprobar respuesta humana:** guardia, suplentes, canales alternativos, autoridad para aislamiento/revocación, forense, continuidad y aprobadores de mensajes. Simular una convocatoria sin divulgar datos a destinatarios reales [MS-05, EXT-01].
6. **Registrar brecha y remediación:** impacto sobre función crítica, probabilidad/escenario, dependencia, acción, control compensatorio, propietario, fecha y prueba de cierre en `Plan`. El estado inicial es desconocido hasta obtener evidencia; no rellenar celdas vacías con `Sí`.
7. **Emitir decisión:** patrocinador aprueba prioridades y acepta por escrito riesgos residuales con vencimiento. Publicar solo un resumen sin secretos ni datos del incidente, con vínculo al repositorio de evidencias autorizado.

Preguntas mínimas de salida: ¿se puede recuperar identidad y restaurar al menos un proceso crítico sin que el atacante controle el plano de recuperación? ¿se detectan y contienen cambios en cuentas, respaldos y datos? ¿las decisiones, evidencia y comunicaciones siguen funcionando sin correo corporativo?

## 3. Assessment trimestral: verificar deriva, no solo completar formulario

En cada trimestre calendario o fiscal acordado, conservar un **nuevo registro fechado** en `Evaluaciones`; no sobrescribir la línea base. Repetir al menos:

- Inventario/BIA: altas y bajas de servicios, nuevas dependencias, cambios de RTO/RPO, cambios en dueño y ruta de continuidad.
- Respaldo: cobertura de activos críticos, inmutabilidad/aislamiento, alertas por borrado y resultados de restauración seleccionados; verificar que la copia de los procedimientos sigue accesible fuera de banda.
- Identidad: cuentas privilegiadas y de servicio, MFA/estaciones de administración, cambios de federación/sincronización, eficacia y límites de revocación en aplicaciones.
- SOC: sensores vivos versus inventario, latencia/retención de logs, detecciones `DE-01` a `DE-13`, falsos negativos y prueba acotada de una señal por dominio.
- Respuesta: llamada a suplentes, autoridad de aislamiento y reversión, cadena de custodia, puntos de activación de continuidad y matriz legal/regulatoria actualizada.
- Hallazgos: vencidos, excepciones, incidentes, pruebas fallidas, controles degradados y controles compensatorios que hayan expirado.

Registrar **antes/después** para cada control cambiado, adjuntar evidencia nueva y reabrir el plan si su criterio de aceptación ya no se cumple. Un cambio relevante de proveedor, tenant, región, régimen legal o arquitectura gatilla evaluación extraordinaria sin esperar al próximo trimestre.

## 4. Priorización sin inventar una puntuación

Priorizar primero un fallo que impida recuperar funciones críticas (respaldos, identidad, documentación), luego acceso privilegiado y propagación, y después puntos de entrada y visibilidad, adaptando a impacto y factibilidad [MS-01]. Usar `Crítica` / `Alta` / `Media` / `Baja` en `Controles` y `Plan` **solo tras justificar** impacto en BIA y exposición. Si no se conoce, dejar `Por definir`; no promediar `No evaluado` con `Probado`.

Para cada brecha: `riesgo -> control -> criterio de aceptación -> prueba -> evidencia -> aprobación -> próxima revisión`. Una fecha sin propietario o una acción sin prueba no cuenta como plan. El HTML `Panel-de-resiliencia.html` calcula recuentos **solo** de las filas que se importan o de las plantillas iniciales; no certifica preparación.

## 5. Informe de cierre por corte

Entregar al patrocinador: perímetro y vacíos, procesos con RTO/RPO aprobados, controles por estado, evidencia caducada, hallazgos críticos abiertos, medidas temporales, fecha del siguiente ejercicio y decisiones a aprobar. Incluir expresamente **qué no se pudo comprobar** y quién aceptó ese riesgo. Los formularios de [12-Formularios.md](12-Formularios.md) permiten realizar entrevistas o imprimir una copia controlada.

**Criterio de finalización:** todas las funciones críticas conocidas tienen dueño y BIA, cada `CT-*` tiene estado con alcance y evidencia o una laguna explícita, los riesgos de recuperación tienen dueño/plazo, y la dirección aprueba el plan. Esto no equivale a certificar que una organización está protegida.

## 6. Equivalencia con las escalas de CISO 365 y del Catálogo de KPIs/OKRs

Para evitar evaluaciones paralelas o contradictorias, los cinco estados operativos de este paquete se articulan directamente con la escala de evidencia `0–4` de `AI_CISO_Atlas_CISO365_Evaluacion_y_Entrevistas_v1.0.xlsx` (`EV01`–`EV51`, indicador `KSG05`) y con los estadios `E1`–`E5` de `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx`:

| Estado en este paquete (`CT-*`) | Nivel de evidencia CISO 365 (`EV##`) | Lectura frente a estadios KPI (`E1`–`E5`) | Hito natural en el primer año |
|---|---|---|---|
| `No evaluado` | Sin puntuar (brecha de visibilidad) | Sin línea base válida (`KSG04` pendiente) | Antes de `H30` / `H60` |
| `No implementado` | `0 · Inexistente` | `E1` (ad hoc, reactivo o sin control) | Recepción `F1/H30` (`RC01..RC32`) |
| `Parcial` | `1 · Inicial / informal` | `E2` (cobertura incompleta o sin estándar) | Diagnóstico `F2/H60` (`ACT-031..051`) |
| `Implementado` | `2 · Definido e implementado` | Elegible a `E3` en métricas de implementación (no en pruebas) | Gobierno operando `F4/H180` |
| `Probado` | `3 · Probado con evidencia` / `4 · Optimizado y auditado` | Habilita `E3` (meta Año 1) y `E4` (meta Año 2) en efectividad/resiliencia | Capacidades probadas `F5/H270` y cierre `F6/H365` |

- **Preguntas de descubrimiento e intervención (`PKG-CISO365`):** usar `EN05` (*evidencia de recuperación del servicio más crítico*), `EN09` (*anticipación de alertas*), `EN11` (*primera hora de incidente mayor*) y `EN14` (*tres escenarios materiales*) durante las entrevistas iniciales. Cuando un control crítico permanezca en `No implementado` o `Parcial`, vincular la brecha con los servicios canónicos `S02` (Diagnóstico base), `S10` (Ejercicios de crisis), `S13` (Gobierno de IA y agentes), `S14` (Arquitectura Zero Trust), `S15` (Operaciones SOC), `S16` (Resiliencia y recuperación) o `S17` (Terceros).
- **Fuentes de evidencia en un cliente Full Microsoft:** contrastar inventario y denominadores con **Microsoft Security Exposure Management**, **Defender for Endpoint/Cloud/IoT**, **Entra ID (Authentication Methods / PIM)** y **Purview Compliance Manager** (`NT-11 I1..I3, M1..M4, A2, A3`). Nunca trasladar el puntaje bruto de un portal como si fuera `Probado` sin acta de ensayo funcional.

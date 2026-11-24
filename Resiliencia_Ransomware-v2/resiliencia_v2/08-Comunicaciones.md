# 08. Comunicaciones de crisis y relaciones externas (v2.0 · DD12/DD13, Q1–Q6 y K58/K61/K62)

**Regla de oro:** primero hechos verificados, audiencia/propósito, aprobación legal y dueño del mensaje; luego un canal que no dependa de la infraestructura sospechosa. La comunicación no espera una certeza imposible cuando hay un deber confirmado de actuar, pero tampoco inventa alcance, atribución, ausencia de robo ni plazos. Este documento es plantilla, **no asesoría legal** [EXT-01, EXT-02].

## 1. Flujo de control de cualquier mensaje

1. El CI crea una ficha de situación con UTC, ID, hechos confirmados, hipótesis separadas, incertidumbres, impactos, medidas y hora de próxima actualización; forense/negocio verifican hechos de su ámbito.
2. Legal y privacidad determinan jurisdicciones, autoridad regulatoria, contratos, materialidad, preservación de pruebas, restricciones de divulgación y plazos **específicos**; llenar la matriz siguiente antes de prometer un plazo. El reporte a fuerzas de la ley puede tener coordinación propia.
3. Comunicaciones prepara versión exacta por audiencia; Legal revisa lenguaje, identidad de afectados, datos personales y riesgo de obstaculizar investigación; el CI/negocio comprueban precisión operativa. Para mercado/inversionistas se suma aprobación corporativa conforme a normas aplicables.
4. Verificar destinatario y canal por un medio independiente para evitar suplantación. El emisor autorizado envía manualmente; registrar versión, aprobadores, UTC, canal, destinatarios y acuse en la hoja `Comunicaciones`. **Ni el HTML ni este paquete envían mensajes.**
5. Corregir errores con versión nueva y hora, sin borrar la anterior; anunciar hora/canal de próxima actualización solo si se puede cumplir. Registrar consultas, compromisos y solicitudes de evidencia/hold.

**Matriz legal a completar por Legal (no hay plazos por defecto):**

| Jurisdicción / contrato | Hecho disparador y criterio | Reloj que aplica | Destinatario y canal | Responsable / suplente | Evidencia de envío y revisión |
|---|---|---|---|---|---|
| `[completar]` | `[completar]` | `[completar]` | `[completar]` | `[completar]` | `[completar]` |

Un “plazo de 72 horas” o “cuatro días” sin ley, entidad, hecho disparador y asesoramiento local es una suposición peligrosa. Mantener la matriz en repositorio restringido, revisada trimestralmente y ante cada incidente.

## 2. Público, objetivo y aprobaciones

| Audiencia | Qué necesita saber / canal | Gate de aprobación |
|---|---|---|
| Equipo de respuesta y empleados | Medidas seguras, rutas alternativas, qué reportar, a quién y cuándo; canal fuera de banda si correo afectado. | CI + seguridad + RR. HH. cuando aplica; evitar indicadores internos que faciliten acceso no autorizado. |
| Dirección y junta/accionistas internos | Riesgo para funciones, escenarios y confianza, costo/continuidad, decisiones requeridas; separar estimaciones de cifras verificadas. | CI, negocio, Legal y gobierno corporativo. |
| Inversionistas/accionistas externos y mercado | Solo información material y exigida según emisor/jurisdicción, con consistencia frente a otros avisos. | Legal, relaciones con inversionistas, autoridad corporativa. |
| Prensa / público | Portavoz único, hechos publicables, medidas de protección y próxima revisión; sin especular sobre autor, pago o exfiltración. | Legal + Comunicaciones + ejecutivo autorizado. |
| Fuerzas de la ley / CERT | Reporte por canal oficial, datos y evidencia pertinentes, contacto para seguimiento, integridad y permisos de entrega. | Legal + custodio forense + CI; registrar número de caso. |
| Reguladores / autoridades de datos | Clasificación del incidente y sujetos, categorías de datos y servicios, medidas, contacto; lo desconocido se etiqueta. | Legal/privacidad confirma disparadores, forma y reloj. |
| Socios/proveedores | Interfaces afectadas, suspensión/restablecimiento de integraciones, medidas de coordinación y obligaciones contractuales. | CI + dueño del tercero + Legal. |
| Clientes / titulares | Hechos aplicables a sus servicios/datos, impacto conocido, medidas para protegerse si procede, canal de soporte y siguiente actualización. | Negocio + Legal/privacidad + Comunicaciones. |

**No** reenviar una misma nota a todas las audiencias: la base factual es común, pero los destinatarios, obligaciones y datos permitidos son distintos. Verificar identidad y confidencialidad de la lista de contactos; un canal comprometido invalida la supuesta entrega.

## 3. Bloques de texto para adaptar, no enviar sin aprobación

**Aviso interno inicial:**

> Estamos investigando una posible interrupción de seguridad que afecta a `[función confirmada]` desde `[hora UTC conocida]`. Por seguridad, utilicen `[canal alternativo aprobado]` y sigan `[instrucción segura verificada]`. No compartan archivos, capturas ni especulaciones fuera del canal del incidente. Próxima actualización `[hora o condición aprobada]`. Contacto verificado: `[registro restringido]`.

**Mensaje a clientes/socios afectados:**

> Estamos investigando un incidente de seguridad relacionado con `[servicio/relación efectivamente afectada]`. Hasta ahora hemos confirmado `[hechos mínimos]`; todavía estamos determinando `[alcance abierto]`. Hemos tomado `[medidas confirmadas que pueden divulgarse]`. Si corresponde, realicen `[acción útil y aprobada]`. Para consultas, utilicen `[canal verificado]`. Compartiremos nueva información `[cadencia aprobada]`.

**Declaración pública/prensa:**

> Detectamos un incidente de ciberseguridad y activamos nuestro plan de respuesta. Estamos investigando el alcance con especialistas y trabajando para mantener o restablecer los servicios afectados. Comunicaremos información adicional cuando esté verificada y sea apropiado hacerlo. Contacto de prensa: `[portavoz autorizado]`.

**Nota para junta/accionistas:** situación y nivel de confianza; afectación/RTO/RPO medidos frente a objetivo; acciones ejecutadas y riesgos de continuidad; categorías de información posiblemente afectada **sin datos personales innecesarios**; decisiones requeridas; asesoramiento legal sobre divulgación y próxima hora de informe. No trasladar estimaciones financieras sin fuente y periodo.

**Solicitud a fuerzas de la ley / regulador:** Legal completa identificación, fundamento y disparador, alcance conocido y desconocido, cronología UTC, medidas de preservación, punto de contacto y adjuntos autorizados; enviar solo por canal oficial y conservar acuse. Un mismo formulario no sustituye requisitos específicos de cada autoridad.

## 4. Gestión de rumores, extorsión y corrección

Centralizar comunicaciones con el atacante y verificar con Legal/IR si su contenido es evidencia; no negociar ni divulgar prueba de vida de datos por iniciativa de un operador. Responder a rumores solo con hechos aprobados y no confirmar públicamente información no verificada. Si surge nueva evidencia de exfiltración o cambia materialidad, Legal reevalúa avisos ya enviados y relojes aplicables; publicar corrección versionada.

**Ensayo:** en el ejercicio anual simular al menos una consulta de prensa, una demanda de cliente/socio y una decisión regulatoria/junta; documentar borrador, reloj confirmado, aprobadores y canal **sin enviarlo a destinatarios reales** [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md).

## 5. Gobierno ejecutivo, regulatorio y técnico de comunicaciones en el ecosistema integrado

- **Derechos de decisión y rituales (`PKG-CISO365`):** `DD12` asigna a **Legal, cumplimiento y privacidad** la autoridad (`A`) para notificar a reguladores y afectados (`R`: CISO), apoyándose en el inventario de obligaciones levantado en `ACT-033` (`RC11`, `RC12`, `RC32`) y actualizado en `R20` y `R30`. `DD13` asigna al **CEO / comité ejecutivo** la aprobación (`A`) de comunicación pública y a **Comunicaciones** la ejecución (`R`). La preparación ejecutiva se instala en `ACT-065` (`R18`) y se somete a prueba con el comité ejecutivo en `ACT-111` (`R33`, `EV22`, `EV44`).
- **Indicadores (`PKG-KPI-OKR`):** `K05` (minutos hasta decisión ejecutiva), `K14` (supervisión activa del Directorio), `K23` (compromisos con clientes), `K58` (calidad del reporte al Directorio, `Q5`), `K61` (notificaciones obligatorias emitidas en plazo: E3 ≥ 80 %, E4 ≥ 95 %), `K62` (incidentes de terceros notificados en plazo contractual, `R07`) y `K64` (evaluación de impacto en datos personales de alto riesgo).
- **Controles Full Microsoft y entrenamiento (`PKG-NINJA`):** proteger borradores y evidencias compartidas con etiquetas cifradas y control de derechos en **Purview Information Protection** (`NT-05 M2, M3`), segmentar acceso interno sensible cuando corresponda mediante **Information Barriers** (`NT-08 M2`) y mantener el mapa de normativas regionales MCSA en **Purview Compliance Manager** (`NT-11 I2, A4, O3`).

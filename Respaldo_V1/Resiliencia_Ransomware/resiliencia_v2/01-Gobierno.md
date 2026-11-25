# 01. Gobierno, autoridad y activación (v2.0 · integrado a CISO 365 y KPIs/OKRs)

**Estado:** plantilla para aprobación local. **Responsable de mantenimiento:** designar. **Revisión:** al inicio, tras cada incidente o ejercicio material y al menos una vez al año. La prioridad es proteger a las personas, limitar el daño y sostener las funciones esenciales; ningún paso de esta guía autoriza por sí solo cambios en producción.

## 1. Mandato y límites

El patrocinador designa por escrito un **comandante de incidente (CI)**, un suplente, un responsable de seguridad (SOC/IR), un responsable de identidad, uno de infraestructura y respaldos, un responsable de continuidad, un custodio de evidencia y representantes de Legal y Comunicaciones. Cada suplente debe poder operar aunque el correo corporativo, el directorio o el proveedor principal no estén disponibles. Conservar directorio, aprobaciones y copia de este plan en un medio **fuera de banda** protegido y probado; no escribir credenciales ni números personales en este paquete.

El CI dirige decisiones operativas y mantiene un único registro de hechos, hipótesis, autorizaciones y próximos hitos. El dueño del proceso de negocio aprueba el impacto tolerable, el orden de recuperación y la aceptación del servicio. Legal determina jurisdicciones, contratos, preservación, notificaciones y contacto con fuerzas de la ley; no se presumen plazos ni obligaciones universales. Comunicaciones redacta y coordina las versiones autorizadas. Separar la decisión de pagar o negociar, si surgiera, en un proceso ejecutivo/legal especializado; no inferir que el pago recuperará datos [MS-02].

| Rol | Tiene que estar disponible para | Autoriza o valida | Registro mínimo |
|---|---|---|---|
| CI y suplente | Declaración, coordinación, cadencia y cierre | Alcance de contención y activación de contingencia dentro del mandato aprobado | ID, hora UTC, razón, alternativas, aprobador |
| SOC/IR | Triage, correlación, hunting y verificación | Recomendación técnica, no mensaje externo | Indicadores, fuentes, confianza, acciones |
| Identidad / plataformas / respaldos | Acciones acotadas y recuperación | Ejecución con aprobación y criterio de reversión | Sistema, operador, resultado y evidencia |
| Forense / custodio | Preservación y transferencias | Método, integridad, acceso y retención con Legal | Cadena de custodia y hashes |
| Negocio / continuidad | BIA y modo degradado | Prioridad de procesos, RTO/RPO, aceptación | Función, dependencia, tiempo, excepción |
| Legal / privacidad | Reglas aplicables y hechos notificables | Avisos, reservas legales y divulgación de datos | Fundamento, jurisdicción, plazo confirmado |
| Comunicaciones | Mensaje y canales alternativos | Publicación tras aprobación | Versión exacta, audiencia, remitente, hora |

Una misma persona puede asumir varios roles solo si se documenta la concentración de riesgo y existe suplente. Completar la matriz nominal y el canal de contacto en un registro restringido aprobado, **no** en los HTML portables [CT-01, CT-16].

## 2. Criterios de activación

| Nivel de trabajo | Indicadores suficientes para abrirlo | Decisión inmediata |
|---|---|---|
| **Sospecha** | Señal creíble de cifrado, borrado de copias, cuenta privilegiada anómala, exfiltración o desactivación de defensas, aun sin confirmación. | Abrir caso, conservar datos volátiles que sea seguro preservar, activar SOC/IR y verificar alcance. |
| **Incidente mayor** | Cifrado/destrucción en curso, propagación, privilegios o respaldos comprometidos, datos críticos posiblemente extraídos o indisponibilidad de función esencial. | CI dirige sala de crisis fuera de banda, solicita contención urgente y llama a continuidad, Legal y forense. |
| **Crisis de negocio** | La continuidad, seguridad física, obligaciones externas o recuperación de procesos críticos supera la autoridad normal. | Patrocinador/gestión de crisis asume decisiones extraordinarias; CI mantiene coordinación técnica. |

La clasificación es provisional y puede subir o bajar con nueva evidencia. **La ausencia de un aviso de rescate no descarta robo de datos.** No esperar una atribución del actor para actuar ante propagación activa. Usar [04-Monitoreo-y-triage.md](04-Monitoreo-y-triage.md) para confirmar señales y [05-Respuesta-y-repudio.md](05-Respuesta-y-repudio.md) para contener [MS-05].

## 3. Autoridad de emergencia y controles de cambio

Antes de una crisis, el patrocinador aprueba por activo o clase de activo: quién puede aislar un equipo, bloquear un usuario, retirar conectividad, suspender sincronización, inmovilizar respaldos o pasar a modo manual; impacto permitido; canales alternativos; duración; y procedimiento de reversión. Un operador ejecuta **solo** en el perímetro autorizado y registra la respuesta del sistema. Para acciones que puedan afectar identidad raíz, controladores de dominio, infraestructura clínica/industrial o servicios de seguridad física, exigir autorización del CI más el dueño técnico y de negocio según la política local. Si un riesgo inminente no permite esperar, actuar conforme al mandato de emergencia ya aprobado, registrar por qué no fue posible el segundo visto bueno y obtener revisión posterior.

Las decisiones son explícitas: **actuar**, **esperar con mitigación temporal** o **rechazar con aceptación del riesgo**. Cada una consigna alcance, evidencia, riesgo de no actuar, efectos colaterales, responsable, UTC, observación posterior y condición de reversión en `02-Operacion-y-pruebas.xlsx` / hoja `Decisiones`. Prohibido automatizar aislamientos masivos o destrucción de sistemas desde los HTML; son guías locales, no integraciones.

## 4. Secuencia de coordinación

1. **Apertura:** registrar el primer indicio y su hora UTC, fuente, activos/usuarios, contacto seguro y nivel provisional. No escribir material sensible en un canal que el adversario pueda leer.
2. **Sala de crisis:** confirmar CI y suplentes, pasar a comunicaciones fuera de banda verificadas y designar escribiente. Revisar quién puede aprobar restricciones sobre identidad, red, respaldos y datos.
3. **Dos pistas simultáneas:** SOC/IR delimita origen, extensión y exfiltración; los operadores detienen la propagación y protegen sistemas todavía sanos. Forense preserva lo factible antes de modificar, sin demorar la contención urgente [MS-05].
4. **Ritmo de decisiones:** fijar hora de siguiente informe según severidad y capacidades; cada informe distingue *confirmado*, *probable*, *desconocido*, acciones realizadas, riesgos y próximo punto de decisión.
5. **Negocio y terceros:** dueño de negocio decide si pasa a proceso alternativo; Legal/Comunicaciones activan la matriz de interesados en [08-Comunicaciones.md](08-Comunicaciones.md). Nadie anuncia “sin exfiltración” si la investigación no lo demuestra.
6. **Salida:** el CI solo desactiva la crisis cuando no hay señales de acceso activo dentro del alcance razonablemente investigado, las credenciales/planes de control han sido saneados, las funciones esenciales son aceptadas por el negocio y quedan brechas y seguimiento asignados.

## 5. Gobierno sostenido

El comité del programa revisa el assessment inicial, el informe trimestral, los resultados de ejercicios y excepciones. Todo hallazgo tiene propietario, fecha comprometida y evidencia de cierre; un riesgo aceptado lleva vencimiento y compensaciones. Si una fuente de telemetría o respaldo deja de funcionar, se abre riesgo operativo en vez de contarla como cobertura. Las cifras de RTO, RPO, tiempos de triage y notificación se aprueban **por proceso y jurisdicción**; las referencias públicas no sustituyen esa decisión [02-Evaluaciones.md](02-Evaluaciones.md), [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md).

**Entregable de aprobación:** mandato firmado, roles y suplentes, alcance de acciones de emergencia, lista protegida de contactos fuera de banda, BIA de funciones críticas, y convocatoria/reporte de la primera prueba.

## 6. Vinculación canónica con CISO 365, KPIs/OKRs, Full Microsoft y Ninja Training

- **Instalación en `PKG-CISO365` (`AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx`):**
  - **F0/H0 (Mandato):** `ACT-002` acuerda alcance, reporte y derechos de decisión; `ACT-009` inicia el diario de decisiones (`R01`).
  - **F1/H30 (Recepción):** `ACT-011` verifica preparación mínima ante incidentes (`RC15` matriz de severidad/contactos, `RC16` retención IR/forense, `RC17` cuentas de emergencia y custodia de secretos); `ACT-023` revisa quién tiene las llaves.
  - **F3/H100 y F4/H180 (Gobierno operando):** `ACT-057` diseña el modelo de gobierno; `ACT-062` actualiza el plan de respuesta con matriz de decisión; `ACT-070` constituye el comité de ciberriesgo (`R12`); `ACT-075` instala aceptación/excepciones (`R09`, `R54`); `ACT-076` designa dueños de riesgo (`EV14`).
- **Derechos de decisión aplicables (`Hoja Derechos de decisión` en CISO 365):**
  - `DD01` Mandato y carta (`A`: CEO/comité ejecutivo; `R`: CISO).
  - `DD03` Apetito y tolerancias (`A`: Directorio; `R`: Comité de ciberriesgo / CISO / CRO).
  - `DD05` / `DD06` / `DD07` Aceptación de riesgo fuera/dentro de tolerancia y excepciones a políticas.
  - `DD10` Declarar un incidente mayor (`A`: CISO; **nunca la declara un proveedor**).
  - `DD11` Aislar o desconectar un servicio crítico (`A`: CEO/comité ejecutivo con umbrales preautorizados; `R`: CISO y CIO/CTO; `C`: dueño de negocio y Legal).
  - `DD12` Notificar a reguladores y afectados (`A`: Legal, cumplimiento y privacidad; `R`: CISO).
  - `DD13` Comunicación pública en crisis (`A`: CEO; `R`: Comunicaciones; `C`: Legal y CISO).
  - `DD14` Activar continuidad o DR (`A`: CEO; `R`: CIO/CTO; `C`: CISO y dueño de negocio).
  - `DD18` Autoridad delegada y límites/desconexión de un agente de IA (`A`: dueño de negocio; `R`: CIO/CTO; `C`: CISO y Legal).
- **Indicadores y OKR (`PKG-KPI-OKR` · `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx`):**
  - `K03` Decisiones materiales registradas y revisadas (E3 ≥ 50 %, E4 ≥ 75 %); `K04` Aceptaciones con alternativas, pre-mortem y vencimiento (E3 ≥ 50 %, E4 ≥ 80 %); `K05` Tiempo hasta la decisión ejecutiva en crisis (E3 ≤ 120 min, E4 ≤ 60 min); `K09` Procesos críticos con dueño de riesgo (`A1-O2-KR2`, E3 ≥ 60 %); `K14` Supervisión activa del Directorio; `K15` Ejercicios ejecutivos (`A1-O3-KR1`); `K16` Roles críticos con suplente entrenado (E3 ≥ 60 %, E4 ≥ 80 %); `KSG02` Rituales realizados (`A1-O2-KR1`); `KSG03` Decisiones tomadas por el rol con autoridad (`A1-O2-KR3`).
- **Operación Full Microsoft y formación (`PKG-NINJA`):** proteger actas, matriz de contactos y sala de crisis con etiquetas cifradas de **Purview Information Protection** (`NT-05 M2/M3`), registrar decisiones/compromisos en listas controladas con retención **Purview** (`NT-09`), gestionar paquetes de suplencia en **Entra ID Governance** (`NT-03 M4`) y entrenar mando de crisis con `NT-02` (`S1, S2, S7`). Véanse [13-Mapeo-canonico-y-prioridades.md](13-Mapeo-canonico-y-prioridades.md) y [14-Operacion-Full-Microsoft.md](14-Operacion-Full-Microsoft.md).

# Ransomware: preparar, contener y recuperar

[Modelado de amenazas](README.md) · [Biblioteca](../README.md)

Guía de trabajo basada en **Resiliencia v2.0 integrada** (12 de noviembre de 2026). Validá autoridades, procedimientos y plazos locales antes de usarla. La seguridad humana prevalece sobre la preservación de equipos.

## Libros y formularios de trabajo

| Artefacto local | Cuándo y cómo usarlo |
| --- | --- |
| [01 · Evaluación y controles](artefactos/ransomware/01-Evaluacion-y-controles.xlsx) | Empezá en `BIA`: proceso, responsable, servicio mínimo, dependencias, RTO y RPO. Completá `Controles` y `Evaluaciones`; trasladá las brechas priorizadas a `Plan` con dueño, plazo y prueba. |
| [02 · Operación y pruebas](artefactos/ransomware/02-Operacion-y-pruebas.xlsx) | Prepará `Fuentes` y `Detecciones`. Registrá cada caso en `Incidentes`, la autorización en `Decisiones` y su evidencia o comunicación en la hoja correspondiente. Usá `Pruebas` para comprobar recuperación y `Competencias` para comprobar titular y suplente. |
| [03 · Correlación, prioridades, Microsoft y Ninja](artefactos/ransomware/03-Correlacion-Prioridades-FullMS-Ninja.xlsx) | Contrastá `Prioridades_Sector_365` y `Matriz_Controles_360` con la BIA. Usá `Operacion_Full_MS` y `Rutas_Ninja_Roles` para encontrar capacidades y práctica, no para declarar controles probados. |
| [Formularios portables v2.0](artefactos/ransomware/12-Formularios.md) | Apertura, BIA, contención, custodia, comunicaciones, ejercicio y relevo; mantené una copia fuera de banda. Guardá los registros reales en un espacio autorizado, no en esta biblioteca. |

El libro 03 conserva el **cruce con el Plan CISO 365 v1.0 y KPI/OKR v1.2**. Para una iniciativa nueva, contrastá los IDs con [el catálogo y los libros de gobierno](../01_Gobierno-CISO/README.md), y registrá los que no tengan equivalencia verificada. La matriz orienta prioridades; no recalcula un cruce con el Plan Frontier v2.0.

[Derechos de decisión](#derechos-de-decisión) · [Playbooks de respuesta](#playbooks-de-respuesta) · [Códigos de pruebas y formación](#códigos-de-pruebas-y-formación)

## Antes de un incidente

- El dueño de negocio aprueba el **servicio mínimo**, el tiempo objetivo de recuperación (**RTO**), la pérdida de datos tolerable (**RPO**) y la opción de operar de forma degradada.
- El comandante de incidente y su suplente tienen mandato de decisión, canal fuera de banda, umbrales de escalamiento y acceso a los procedimientos sin depender del entorno que podría quedar comprometido.
- Probá la independencia de identidades, copias, claves, red y procedimientos de recuperación. Un respaldo exitoso no demuestra que la aplicación, la identidad y sus dependencias puedan recuperarse.
- Ejercitá un escenario con indisponibilidad de identidad, un proveedor que no responde y un proceso asistido por IA que deba continuar sin el agente. Medí capacidad real, no solo ejecución del simulacro.

## Durante la respuesta

| Paso | Responsable propuesto | Acción y evidencia |
| --- | --- | --- |
| Declarar y delimitar | SOC y comandante | Abrir incidente con hora UTC; distinguir sistemas, identidades y datos confirmados, posibles y no revisados. No esperar atribución para escalar un servicio crítico comprometido. |
| Contener con autorización | Comandante y responsables técnicos | Mantener administración confiable; elegir el perímetro mínimo eficaz, considerar el efecto en negocio y dejar registrada la reversión. Custodiar la evidencia. |
| Mantener el servicio | Dueño de negocio y continuidad | Activar contingencia si el RTO o la integridad están en riesgo. Registrar tareas suspendidas, canal alternativo y transacciones que se deberán reconciliar. Si se suspende un agente, ejecutar la ruta sin IA. |
| Preservar y comunicar | Forense, Legal y portavoz | Proteger integridad, acceso e historial de custodia. Revisar obligaciones y plazos aplicables. Comunicar hechos confirmados, incertidumbres y momento de la próxima actualización. |
| Recuperar en una zona confiable | Continuidad, plataforma, identidad y negocio | Seleccionar un punto limpio, recuperar dependencias en orden y validar integridad, permisos, telemetría y transacciones. Si el punto limpio excede el RPO, no ocultar la brecha: pedir una decisión. |

## Códigos de respuesta

### Derechos de decisión

El `DD-ID` identifica **qué se autoriza**, no quién detectó el incidente ni qué playbook se eligió. Estos códigos conservan el sentido del programa de resiliencia v2.0 sobre el Plan CISO 365 v1.0. Usá el rol aprobado en el mandato local y registrá a la persona que autorizó y la hora UTC. Los códigos de referencia no otorgan autoridad.

| Código | Decisión | Autoridad de referencia |
| --- | --- | --- |
| `DD10` | Declarar un incidente mayor. | CISO. Un proveedor puede informar y recomendar, no declarar por la organización. |
| `DD11` | Aislar o desconectar un servicio crítico. | CEO o comité ejecutivo, según los umbrales preautorizados. CISO y CIO/CTO coordinan la ejecución; se consulta al dueño de negocio y a Legal. |
| `DD12` | Notificar a reguladores o personas afectadas. | Legal, Cumplimiento y Privacidad determinan la obligación y el plazo; CISO aporta los hechos. |
| `DD13` | Autorizar la comunicación pública de crisis. | CEO; Comunicaciones prepara y emite, con revisión de Legal y CISO. |
| `DD14` | Activar continuidad o recuperación ante desastres (DR). | CEO; CIO/CTO coordina con CISO y el dueño de negocio. |
| `DD18` | Definir o suspender la autoridad delegada de un agente de IA. | Dueño de negocio; CIO/CTO ejecuta con intervención de CISO y Legal según el mandato local. |

Si una medida exige más de una decisión, registralas por separado. Por ejemplo, suspender un agente (`DD18`) no autoriza a desconectar el servicio crítico que lo usa (`DD11`), ni a activar por sí solo el plan de continuidad (`DD14`).

### Playbooks de respuesta

El `PB-ID` identifica el procedimiento aplicable al escenario. Elegí el perímetro mínimo, preservá la evidencia y verificá el efecto antes de cerrar. La [matriz de correlación](artefactos/ransomware/03-Correlacion-Prioridades-FullMS-Ninja.xlsx), hoja `Matriz_SOC_IR_360`, permite consultar detecciones, derechos de decisión y métricas asociados; la hoja `Decisiones` del [libro de operación](artefactos/ransomware/02-Operacion-y-pruebas.xlsx) conserva la autorización real.

| Código | Cuándo usarlo | Qué verificar |
| --- | --- | --- |
| `PB-01` | Equipo con indicios de cifrado o propagación respaldados por señales convergentes: contención del equipo o segmento autorizado. | Aislamiento efectivo, ausencia de nueva propagación dentro del alcance y evidencia preservada. |
| `PB-02` | Usuario privilegiado o sesión sospechosa: limitar accesos y revocar sesiones según el alcance. | Acceso administrativo confiable, accesos afectados invalidados y aplicaciones aún operativas. |
| `PB-03` | Repositorio o administración de respaldos bajo amenaza: proteger copias, claves y operación de recuperación. | Punto íntegro recuperable y acceso restringido sin perder monitoreo ni continuidad. |
| `PB-04` | Datos o sincronización comprometidos, o posible exfiltración: limitar el flujo y preservar registros. | Cese observado del flujo, datos en alcance y evidencia para la evaluación de Legal. |
| `PB-05` | Clave, aplicación o acceso de tercero comprometido: suspender o sustituir el acceso afectado. | El acceso anterior dejó de funcionar y las integraciones autorizadas conservan su servicio. |
| `PB-06` | Medida aplicada con alcance erróneo o falso positivo: corregir o revertir de forma controlada. | Servicio restituido, salud y riesgo reevaluados, y evidencia del estado previo conservada. |
| `PB-07` | Agente, copiloto o conector comprometido: suspenderlo y pasar al proceso alternativo. | Nuevas acciones bloqueadas, trazas preservadas y operación sin IA comprobada. |

**Ejemplo de F3, solo simulación:** `INC-EJ-01 / PB-07 / DD18`. La evidencia `EV-EJ-01` muestra un agente de prueba fuera de alcance. Se propone suspender solo ese agente y seguir por la vía manual para evitar nuevos efectos sin interrumpir el servicio. El dueño de negocio autoriza a las `14:10 UTC`; plataforma registra la tarea simulada a las `14:12 UTC`. A las `14:15 UTC`, un verificador confirma que no salen nuevas acciones y que la vía manual funciona. El agente permanece suspendido hasta revisar permisos y obtener autorización de retorno.

### Códigos de pruebas y formación

- `CT-##`: control, en la hoja `Controles` del [libro de evaluación](artefactos/ransomware/01-Evaluacion-y-controles.xlsx). `DE-##`: detección, en la hoja `Detecciones` del [libro de operación](artefactos/ransomware/02-Operacion-y-pruebas.xlsx).
- `E1`: ejercicio integrado de mando y respuesta; `E2`: restauración técnica con RTO/RPO medidos y aceptación de negocio; `E3`: aislamiento y revocación simulados, con evidencia y comunicación. Registrá tipo y resultado en `Pruebas`.
- `ACT-###`, `R##` y `K##`/`KSG##`: buscá las referencias en `Plan365_Integracion`, `Catalogo_KPI` y `KPI_Sistema_Gestion` del [catálogo KPI/OKR v1.2](../01_Gobierno-CISO/artefactos/AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.2_2026-11-10.xlsx). Contrastá los KPI específicos en `Catalogo_KPI_Ransom` del libro 03. Si se trabaja con el Plan Frontier v2.0 y la equivalencia no está verificada, registrá el ID de la edición elegida y «sin equivalencia confirmada».
- Para `ROL-01` a `ROL-09`, consultá `Rutas_Ninja_Roles` del [libro 03](artefactos/ransomware/03-Correlacion-Prioridades-FullMS-Ninja.xlsx). Usá el índice [Ninja Training](../03_Operacion-y-formacion-Microsoft/Rutas-Ninja.md) para abrir el programa `NT-##` y localizar el módulo. Registrá el resultado en `Competencias` del libro 02.

## Criterios para reconectar

1. IR y plataforma establecen qué identidades, configuraciones y datos son confiables. Se valida en un entorno aislado que no depende de la administración comprometida.
2. Negocio verifica transacciones críticas y reconcilia datos del modo degradado. Medí el tiempo real de recuperación desde la interrupción hasta la aceptación del servicio y la pérdida de datos desde el último punto íntegro restaurado hasta la interrupción. Compará ambos resultados con el RTO y el RPO acordados.
3. Comandante autoriza reincorporación gradual con monitoreo reforzado, criterio de reversión y dueño para cada segmento.
4. Negocio acepta el retorno y registra el riesgo residual. Si siguen abiertas dudas de alcance, persistencia o extracción, esas dudas quedan explícitas.

### Acta de retorno para copiar

| Incidente / servicio | Punto de restauración y zona | RTO/RPO objetivo y real | Pruebas que pasaron / fallaron | Aceptación, restricciones y reversión |
| --- | --- | --- | --- | --- |
| | | | | |

Para preparar la práctica de cada rol y suplente, ver [Rutas Ninja por rol](../03_Operacion-y-formacion-Microsoft/Rutas-Ninja.md).

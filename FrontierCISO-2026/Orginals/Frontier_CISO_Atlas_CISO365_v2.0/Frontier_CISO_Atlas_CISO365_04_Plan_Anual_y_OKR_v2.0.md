# Plan anual y cuatro ciclos de OKR

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 04 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Estructura

El año tiene cuatro ciclos trimestrales. El primero empieza con el diagnóstico, que ocupa sus primeros 60 días. Cada ciclo tiene seis frentes, un objetivo por frente y tres resultados clave por objetivo: 24 objetivos y 72 resultados clave. Cada etapa se cierra con criterios de salida.

| Etapa | Días | Objetivo |
|---|:--:|---|
| Diagnóstico y entendimiento (primer tramo del ciclo 1) | 1 a 60 | Saber, con evidencia, qué se recibe y dónde está la organización: funciones, quién las opera, servicios externalizados, entornos, postura Zero Trust e indicadores de base. |
| Ciclo 1 · Conocer, estabilizar y ordenar | 1 a 90 | Conocer con evidencia lo que se recibe, cerrar lo que no puede esperar y ordenar la propiedad: cada función con dueño, cada servicio externalizado con responsable interno y cada riesgo prioritario con quien decide. Son los primeros 90 días del cargo: ocupan el lugar de los 100 días del plan anterior. |
| Ciclo 2 · Adecuar | 91 a 180 | Llevar las funciones al nivel que el riesgo exige en todos los entornos: apetito, políticas, estructura, contratos y controles con la misma regla en cada nube y con cada proveedor. |
| Ciclo 3 · Evolucionar y probar | 181 a 270 | Probar lo que se afirma y avanzar hacia la política dinámica, el mínimo privilegio y la automatización, con agentes y proveedores bajo las mismas reglas. |
| Ciclo 4 · Demostrar y sostener | 271 a 365 | Rendir cuentas con evidencia, decidir con los datos del año qué se opera, qué se contrata y qué se cambia, y dejar instalado el ciclo que se repite cada año. |

Las fechas se calculan desde el día 1 en el cargo, en el libro `Frontier_CISO_Atlas_CISO365_Plan_Anual_y_OKR_v2.0.xlsx`. Las duraciones son parámetros.

Los hitos de la versión 1.0 coinciden ahora con el cierre de cada ciclo, salvo los dos del diagnóstico:

| Hito | Día | Qué se entrega | Ciclo |
|:--:|:--:|---|:--:|
| H30 | 30 | Acta de recepción | Ciclo 1 |
| H60 | 60 | Diagnóstico base | Ciclo 1 |
| H90 | 90 | Informe de los 90 días | Ciclo 1 |
| H180 | 180 | Sistema de gobierno operando | Ciclo 2 |
| H270 | 270 | Capacidades probadas | Ciclo 3 |
| H365 | 365 | Rendición de cuentas anual | Ciclo 4 |

## 2. Seis frentes

| Frente | Nombre | Alcance |
|:--:|---|---|
| F1 | Gobierno y rendición de cuentas | Mandato, apetito, políticas, cumplimiento y reporte. |
| F2 | Programa, personas y presupuesto | Portafolio de controles, estructura, dotación, cadencias y finanzas. |
| F3 | Identificar y proteger | Inventario, exposición y protección sobre la arquitectura Zero Trust. |
| F4 | Detectar, responder y recuperar | Vigilancia, respuesta, recuperación y aprendizaje. |
| F5 | Ecosistema | Servicios externalizados, entornos multinube, herramientas de varios proveedores y terceros. |
| F6 | IA y agentes | Inventario, identidad, límites, evaluación y supervisión de la IA y de los agentes. |

## 3. Cómo se mide un resultado clave

- Cada resultado clave usa **un** indicador del catálogo, o es un hito que se mide de 0 a 1.
- **Versión aplicable.** Si la función está externalizada, se aplica la versión externalizada. Si está co-gestionada, se mide con el indicador propio y el compromiso del proveedor se sigue aparte.
- De los 72 resultados clave, 39 usan un indicador distinto cuando la función está externalizada y 3 son hitos.
- **Avance.** Si el valor al cierre alcanza la meta, 100%. Si no, (valor − línea base) ÷ (meta − línea base), entre 0% y 100%. Si la línea base ya cumplía la meta y el valor dejó de cumplirla, el avance es 0%.
- **Estado.** En camino con 70% o más; en riesgo entre 40% y 70%; fuera de curso por debajo.
- **Metas.** Son propuestas para calibrar con la línea base del diagnóstico. Una meta que la línea base ya cumple se reemplaza por una más exigente.

## Diagnóstico y entendimiento (primer tramo del ciclo 1) · días 1 a 60

**Objetivo.** Saber, con evidencia, qué se recibe y dónde está la organización: funciones, quién las opera, servicios externalizados, entornos, postura Zero Trust e indicadores de base.

**Pregunta que responde.** ¿Qué tenemos, quién lo opera, qué evidencia lo respalda y qué puede dañar al negocio?

**Trampa habitual.** El diagnóstico sin fecha de cierre, o el plan escrito antes de medir.

**Resultado.** Diagnóstico base, línea base de indicadores, metas del ciclo 1 confirmadas y propuesta de plan anual con presupuesto y decisiones requeridas.

**En la versión 1.0.** F1 Recibir y escuchar · F2 Diagnosticar · H30 Acta de recepción · H60 Diagnóstico base · 42 actividades del plan anterior.

### Criterios de salida de la etapa (8)

1. Acta de recepción firmada: personas, presupuesto, contratos, compromisos y riesgos abiertos.
2. Diagnóstico por función completo: nivel de evidencia y modelo de provisión de las 59 funciones.
3. Registro de servicios externalizados con dueño interno, alcance y fecha de fin de contrato.
4. Mapa de entornos y cobertura de control medida en cada uno.
5. Postura Zero Trust evaluada en los ocho dominios.
6. Línea base medida para los indicadores principales de las tres audiencias.
7. Escenarios de riesgo prioritarios acordados con los dueños del negocio.
8. Propuesta de cuatro ciclos, presupuesto y decisiones requeridas presentada al sponsor.

## Ciclo 1 · Conocer, estabilizar y ordenar · días 1 a 90

**Objetivo.** Conocer con evidencia lo que se recibe, cerrar lo que no puede esperar y ordenar la propiedad: cada función con dueño, cada servicio externalizado con responsable interno y cada riesgo prioritario con quien decide. Son los primeros 90 días del cargo: ocupan el lugar de los 100 días del plan anterior.

**Pregunta que responde.** ¿Qué puede dañarnos hoy, quién responde por cada función y qué necesito que la dirección decida?

**Trampa habitual.** Prometer sin pedir: un plan ambicioso sin dueños, sin recursos y sin decisiones explícitas.

**Resultado.** Diagnóstico cerrado en el día 60; mandato, plan y presupuesto aprobados; dueños designados; exposiciones críticas cerradas; informe de los 90 días a las tres audiencias.

**En la versión 1.0.** F1 Recibir y escuchar · F2 Diagnosticar · F3 Priorizar y comprometer · H30 Acta de recepción · H60 Diagnóstico base · H90 Informe de los 90 días (H100 en la versión 1.0) · 21 actividades del plan anterior.

### F1 · Gobierno y rendición de cuentas

**Objetivo.** Convertir el diagnóstico en un mandato, un plan y un sistema de decisiones que la dirección reconoce como propios.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F1-KR1 | El plan anual, el presupuesto y las decisiones requeridas están aprobados por el sponsor y presentados al directorio. | Hito cumplido | El plan aprobado incluye, para cada servicio externalizado crítico, la decisión de mantener, renegociar o reemplazar el contrato. | Hito cumplido | GOB-G1.2 |
| C1-F1-KR2 | Los procesos y los activos críticos tienen un dueño de riesgo designado. | K09 ≥ 80% | Cada servicio externalizado tiene un dueño interno designado, con autoridad sobre el contrato. | KX01 ≥ 100% | GOB-G4.1 |
| C1-F1-KR3 | Las decisiones materiales de seguridad las toma el rol que tiene la autoridad y quedan registradas. | KSG03 ≥ 80% | Cada proveedor crítico tiene una revisión periódica del servicio, con acta y decisiones. | KX20 ≥ 75% | GOB-G4.1 |

### F2 · Programa, personas y presupuesto

**Objetivo.** Ordenar el programa: quién es dueño de qué, con qué capacidad y con qué presupuesto.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F2-KR1 | Los cruces críticos de la grilla de propiedad tienen un dueño nominado. | K71 ≥ 75% | Los cruces de la grilla tienen dueño y modelo de provisión declarado: cada cruce a cargo de un proveedor tiene contrato identificado y dueño interno. | K71 ≥ 75% | GOB-G2.1 |
| C1-F2-KR2 | Los controles prioritarios del portafolio tienen dueño, objetivo medible y evidencia definidos. | K99 ≥ 60% | Los controles que opera un proveedor tienen su objetivo y su evidencia definidos en un anexo operativo del contrato. | K99 ≥ 60% | GES-M1.1 |
| C1-F2-KR3 | El gasto de seguridad tiene su costo total conocido. | K104 ≥ 60% | El costo total incluye, para cada servicio externalizado crítico, el costo por unidad de resultado. | K104 ≥ 60% | GES-M1.2 |

### F3 · Identificar y proteger

**Objetivo.** Cerrar las exposiciones que no pueden esperar y fijar la base de identidad.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F3-KR1 | Las cuentas privilegiadas y las de acceso remoto usan autenticación resistente a la suplantación; el resto avanza. | K33 ≥ 50% | Las cuentas del proveedor en los entornos de la organización usan autenticación fuerte, privilegio mínimo y registro. | KX10 ≥ 80% | OPE-PR-01 |
| C1-F3-KR2 | El inventario de activos cubre todos los entornos del alcance. | K39 ≥ 70% | El proveedor entrega el inventario de lo que gestiona y ese inventario se reconcilia con el propio. | K39 ≥ 70% | OPE-ID-01 |
| C1-F3-KR3 | Las vulnerabilidades explotadas activamente y las exposiciones críticas se corrigen en plazo. | K46 ≥ 70% | El plazo de corrección está pactado como nivel de servicio y se cumple. | KX03 ≥ 85% | OPE-ID-02 |

### F4 · Detectar, responder y recuperar

**Objetivo.** Saber que un incidente grave se vería y se podría contener hoy.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F4-KR1 | Los activos críticos tienen telemetría y protección. | K41 ≥ 70% | El alcance contratado de la vigilancia cubre todos los entornos críticos. | KX19 ≥ 80% | OPE-DE-05 |
| C1-F4-KR2 | Los acuerdos y los contactos de respuesta están vigentes y verificados. | K130 ≥ 90% | El tiempo de traspaso entre el proveedor y el equipo interno se midió en un ejercicio y está dentro del objetivo. | KX12 ≤ 60 minutos | GES-M5.1 |
| C1-F4-KR3 | Los sistemas críticos tienen respaldos inalterables y una restauración probada. | K28 ≥ 50% | El proveedor ejecuta la restauración de prueba en presencia de la organización y entrega la evidencia. | K28 ≥ 50% | OPE-RC-01 |

### F5 · Ecosistema

**Objetivo.** Conocer y gobernar lo que operan terceros y lo que corre en cada entorno.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F5-KR1 | Los proveedores críticos están identificados, evaluados y con cláusulas de seguridad. | K31 ≥ 60% | Los servicios críticos externalizados tienen niveles de servicio medibles por resultado. | KX02 ≥ 65% | OPE-ID-04 |
| C1-F5-KR2 | La cobertura de control está medida en cada entorno y la paridad entre entornos mejora. | K123 ≥ 50% | Los datos y los registros en poder de cada proveedor tienen localización, retención y devolución acordadas. | KX22 ≥ 70% | GES-M3.2 |
| C1-F5-KR3 | Las capacidades con herramientas solapadas tienen una decisión: consolidar, mantener o reemplazar. | K122 ≤ 20% | Los contratos críticos tienen las cláusulas mínimas. | KX21 ≥ 70% | GES-M3.2 |

### F6 · IA y agentes

**Objetivo.** Saber qué IA y qué agentes existen, y poner reglas antes de escalar.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C1-F6-KR1 | Los sistemas de IA y los agentes están inventariados, con dueño y propósito. | K49 ≥ 70% | Los proveedores declararon el uso de IA y de agentes en sus servicios, los datos que emplean y la supervisión humana. | KX17 ≥ 60% | OPE-ID-07 |
| C1-F6-KR2 | Los casos de uso nuevos de IA tienen una evaluación de riesgo e impacto antes de ponerse en marcha. | K51 ≥ 60% | Los contratos nuevos y los renovados exigen la evaluación previa de los casos de uso de IA del proveedor. | K51 ≥ 60% | GOB-G2.2 |
| C1-F6-KR3 | Cada agente tiene un dueño humano y una autoridad delegada acotada. | K50 ≥ 60% | Los agentes del proveedor que actúan en los entornos de la organización tienen identidad propia y permisos acotados. | K165 ≥ 65% | GES-M2.2 |

### Criterios de salida de la etapa (7)

1. Mandato, plan anual y presupuesto aprobados.
2. Dueños designados para los riesgos prioritarios, los cruces críticos de la grilla y los servicios externalizados.
3. Exposiciones críticas cerradas, o con plan fechado y riesgo aceptado por su dueño.
4. Capacidad mínima de respuesta verificada: acuerdos vigentes, un ejercicio y una restauración probada.
5. Brechas contractuales de los servicios críticos con decisión: mantener, renegociar o reemplazar.
6. Inventario de IA y agentes, y política de uso aprobada.
7. Informe de los 90 días entregado a las tres audiencias.

## Ciclo 2 · Adecuar · días 91 a 180

**Objetivo.** Llevar las funciones al nivel que el riesgo exige en todos los entornos: apetito, políticas, estructura, contratos y controles con la misma regla en cada nube y con cada proveedor.

**Pregunta que responde.** ¿Cada función opera al nivel requerido, en todos los entornos y con quien corresponde?

**Trampa habitual.** Gobierno decorativo: comités informativos, apetito sin umbrales y contratos sin niveles de servicio medibles.

**Resultado.** Sistema de gobierno operando; funciones críticas en nivel «Implementado»; contratos críticos con niveles de servicio y evidencia.

**En la versión 1.0.** F4 Instalar el sistema de gobierno y gestión · H180 Sistema de gobierno operando · 30 actividades del plan anterior.

### F1 · Gobierno y rendición de cuentas

**Objetivo.** Instalar el gobierno del riesgo: apetito, políticas y cumplimiento con evidencia.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F1-KR1 | El directorio aprobó el apetito de riesgo, con umbrales medibles para los escenarios prioritarios. | K86 ≥ 80% | El apetito fija un límite a la dependencia de un mismo proveedor y la concentración está dentro de ese límite. | KX14 ≤ 45% | GOB-G4.2 |
| C2-F1-KR2 | Las políticas y los estándares están dentro de su ciclo de revisión. | K74 ≥ 90% | Las políticas aplicables están incorporadas a los contratos críticos, junto con las cláusulas mínimas. | KX21 ≥ 90% | GOB-G2.2 |
| C2-F1-KR3 | Las obligaciones aplicables están mapeadas a controles con evidencia vigente. | K57 ≥ 70% | La evidencia que depende de los proveedores se entrega en plazo y permite verificar. | KX04 ≥ 80% | GOB-G3.2 |

### F2 · Programa, personas y presupuesto

**Objetivo.** Dotar el programa: estructura, capacidades y cadencias.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F2-KR1 | La estructura y la dotación objetivo están aprobadas, y las capacidades críticas, cubiertas. | K12 ≥ 75% | Cada función externalizada tiene capacidad interna acreditada para supervisarla. | KX15 ≥ 75% | GES-M1.2 |
| C2-F2-KR2 | Las cadencias operativas de los controles prioritarios se cumplen. | K100 ≥ 70% | Las cadencias a cargo del proveedor figuran en el anexo operativo y se revisan en cada reunión de servicio. | KX20 ≥ 90% | GES-M1.1 |
| C2-F2-KR3 | La hoja de ruta del año avanza según lo comprometido. | K18 ≥ 50% | Los hitos de la hoja de ruta que dependen de proveedores tienen compromiso contractual y avanzan según lo comprometido. | K18 ≥ 50% | GES-M1.1 |

### F3 · Identificar y proteger

**Objetivo.** Extender la protección a todos los entornos con la misma política.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F3-KR1 | La paridad de control entre entornos alcanza el nivel objetivo. | K123 ≥ 70% | Los servicios contratados cubren todos los entornos del alcance con el mismo nivel de servicio. | KX19 ≥ 95% | GES-M3.2 |
| C2-F3-KR2 | Los accesos privilegiados dejan de ser permanentes. | K34 ≥ 60% | Los accesos del proveedor cumplen privilegio mínimo, autenticación fuerte y registro. | KX10 ≥ 95% | OPE-PR-02 |
| C2-F3-KR3 | Los datos sensibles están clasificados y protegidos. | K37 ≥ 60% | Los datos en poder de proveedores tienen localización, retención y devolución acordadas. | KX22 ≥ 90% | OPE-PR-06 |

### F4 · Detectar, responder y recuperar

**Objetivo.** Detectar y contener dentro de los tiempos que el negocio tolera.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F4-KR1 | Las técnicas de ataque priorizadas tienen detección validada. | K43 ≥ 50% | La validación de las detecciones del proveedor la realiza la organización o un tercero independiente, según el plan. | KX05 ≥ 65% | OPE-DE-02 |
| C2-F4-KR2 | El tiempo medio de detección está dentro del objetivo. | K42 ≤ 24 horas | Los tiempos de detección y de contención pactados como nivel de servicio se cumplen. | KX03 ≥ 90% | OPE-DE-01 |
| C2-F4-KR3 | Los escenarios críticos tienen una guía de actuación probada. | K32 ≥ 60% | Las guías definen qué ejecuta el proveedor y qué decide la organización: no hay acciones reservadas ejecutadas sin aprobación. | KX13 ≤ 0 n.º | GES-M5.1 |

### F5 · Ecosistema

**Objetivo.** Poner los contratos y los entornos al nivel que el riesgo exige.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F5-KR1 | Los proveedores críticos entregan evidencia de control actualizada. | K132 ≥ 60% | Todos los servicios críticos tienen niveles de servicio medibles por resultado. | KX02 ≥ 100% | GES-M6.2 |
| C2-F5-KR2 | Las cuentas, las suscripciones y los proyectos de nube están bajo la línea base de la organización. | K134 ≥ 85% | La discrepancia entre lo que informa el proveedor y lo que se verifica está dentro de la tolerancia. | KX06 ≤ 10% | GES-M6.2 |
| C2-F5-KR3 | Los incidentes de terceros se notifican dentro del plazo contractual. | K62 ≥ 80% | Los subcontratistas de los servicios críticos están identificados y aprobados. | KX11 ≥ 85% | GES-M6.2 |

### F6 · IA y agentes

**Objetivo.** Dar a cada agente identidad, límites y supervisión.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C2-F6-KR1 | Los agentes en producción tienen identidad propia y permisos por herramienta revisados. | K165 ≥ 65% | El uso de IA y de agentes por parte de los proveedores está declarado y gobernado en los contratos. | KX17 ≥ 85% | OPE-PR-11 |
| C2-F6-KR2 | Las interacciones con IA están protegidas contra la fuga de datos. | K52 ≥ 60% | Las plataformas de IA de terceros aplican los permisos y las etiquetas de los datos de la organización. | K52 ≥ 60% | OPE-PR-06 |
| C2-F6-KR3 | La actividad de los agentes está integrada a la vigilancia. | K53 ≥ 60% | Los agentes operados por proveedores entregan sus trazas a la vigilancia de la organización. | K53 ≥ 60% | OPE-DE-06 |

### Criterios de salida de la etapa (7)

1. Apetito de riesgo aprobado por el directorio, con umbrales.
2. Sistema de gobierno operando: comité, políticas vigentes, registro de riesgos y calendario cumplido.
3. Estructura y dotación objetivo aprobadas; modelo de provisión decidido por función.
4. Funciones críticas en nivel «Implementado» en todos los entornos del alcance.
5. Contratos críticos con niveles de servicio por resultado, evidencia y cláusulas mínimas.
6. Tiempos de detección y de contención medidos y dentro del objetivo del ciclo.
7. Agentes en producción con identidad propia, dueño y vigilancia.

## Ciclo 3 · Evolucionar y probar · días 181 a 270

**Objetivo.** Probar lo que se afirma y avanzar hacia la política dinámica, el mínimo privilegio y la automatización, con agentes y proveedores bajo las mismas reglas.

**Pregunta que responde.** ¿Lo que decimos que tenemos funciona cuando se lo exige, también en lo que opera un tercero?

**Trampa habitual.** Confundir actividad con efectividad: controles configurados que nunca se probaron y contratos que nunca se verificaron.

**Resultado.** Capacidades críticas en nivel «Probado»; reversibilidad de los servicios críticos comprobada; agentes evaluados antes de ampliar su autonomía.

**En la versión 1.0.** F5 Ejecutar y probar · H270 Capacidades probadas · 16 actividades del plan anterior.

### F1 · Gobierno y rendición de cuentas

**Objetivo.** Decidir con riesgo cuantificado y evidencia continua.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F1-KR1 | Los escenarios prioritarios están cuantificados. | K89 ≥ 80% | Los escenarios cuantificados incluyen la falla o el compromiso de cada proveedor crítico. | K89 ≥ 80% | GOB-G5.1 |
| C3-F1-KR2 | Los controles clave entregan su evidencia de forma automática. | K80 ≥ 40% | La evidencia de los proveedores llega en plazo y en un formato que permite verificarla. | KX04 ≥ 95% | GOB-G3.2 |
| C3-F1-KR3 | Las decisiones solicitadas a la dirección se resuelven en plazo. | K95 ≥ 80% | Las decisiones solicitadas se resuelven en plazo, incluidas las que exigen renegociar o reemplazar contratos. | K95 ≥ 80% | GOB-G6.1 |

### F2 · Programa, personas y presupuesto

**Objetivo.** Hacer sostenible la operación con personas, proveedores y agentes.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F2-KR1 | El trabajo no planificado del equipo baja al nivel objetivo. | K101 ≤ 45% | El tiempo de traspaso con el proveedor baja al nivel objetivo y reduce la carga del equipo interno. | KX12 ≤ 30 minutos | GES-M1.1 |
| C3-F2-KR2 | El personal con funciones de alto riesgo tiene formación específica vigente. | K106 ≥ 85% | El personal que supervisa los servicios externalizados está capacitado para hacerlo. | KX15 ≥ 90% | GES-M1.2 |
| C3-F2-KR3 | Cada tarea operativa tiene un responsable definido: persona, proveedor o agente. | K107 ≥ 85% | Las tareas a cargo del proveedor figuran en la matriz de responsabilidades del contrato. | K107 ≥ 85% | GES-M1.2 |

### F3 · Identificar y proteger

**Objetivo.** Pasar de la cobertura a la política dinámica y al mínimo privilegio.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F3-KR1 | El acceso a los recursos críticos lo decide una política que evalúa identidad, dispositivo y contexto. | K118 ≥ 65% | Ningún acceso del proveedor queda fuera de esa política. | KX10 ≥ 100% | GES-M3.1 |
| C3-F3-KR2 | La segmentación de los activos críticos está verificada con pruebas. | K36 ≥ 60% | La segmentación verificada incluye las conexiones del proveedor: su acceso se limita a lo contratado. | K36 ≥ 60% | OPE-PR-08 |
| C3-F3-KR3 | Las identidades no humanas tienen dueño, rotación y privilegio revisado. | K148 ≥ 55% | Las integraciones del proveedor usan identidades propias, con rotación y privilegio revisado. | K148 ≥ 55% | OPE-PR-03 |

### F4 · Detectar, responder y recuperar

**Objetivo.** Demostrar bajo presión que se detecta, se contiene y se recupera.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F4-KR1 | Se realizó un ejercicio de adversario de extremo a extremo y sus hallazgos críticos se corrigieron y se revalidaron. | K144 ≥ 60% | El ejercicio verifica lo que el proveedor informa: la discrepancia queda dentro de la tolerancia. | KX06 ≤ 10% | OPE-ID-05 |
| C3-F4-KR2 | Las pruebas de recuperación cumplen los objetivos de tiempo y de punto de recuperación. | K30 ≥ 60% | Las pruebas se hacen con el proveedor de recuperación presente y en todos los entornos. | K30 ≥ 60% | OPE-RC-02 |
| C3-F4-KR3 | La recuperación de la identidad y de la plataforma de control está probada en un entorno aislado. | K181 ≥ 50% | La recuperación probada no depende del acceso de un proveedor que usa esa misma plataforma. | K181 ≥ 50% | OPE-RC-03 |

### F5 · Ecosistema

**Objetivo.** Probar la reversibilidad y reducir la dependencia.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F5-KR1 | Los servicios críticos concentrados en un proveedor sin alternativa están dentro del límite del apetito. | K27 ≤ 30% | Los servicios críticos externalizados tienen un plan de salida probado. | KX08 ≥ 40% | GES-M6.2 |
| C3-F5-KR2 | Los servicios críticos usan telemetría, identidad y evidencia portables. | K135 ≥ 50% | La exportación de datos, configuraciones y reglas de cada servicio crítico se comprobó en un formato utilizable. | KX09 ≥ 50% | GES-M6.2 |
| C3-F5-KR3 | Los hallazgos de los proveedores críticos se corrigen en plazo. | K143 ≥ 60% | Los hallazgos de la revisión de cada servicio se corrigen en plazo. | KX18 ≥ 70% | OPE-ID-04 |

### F6 · IA y agentes

**Objetivo.** Probar los agentes antes de darles más autonomía.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C3-F6-KR1 | Los agentes en producción tienen una evaluación adversarial vigente. | K166 ≥ 55% | Los agentes de terceros entregan el resultado de su evaluación antes de actuar en los entornos de la organización. | K166 ≥ 55% | OPE-PR-11 |
| C3-F6-KR2 | La detención de emergencia de los agentes con autonomía de ejecución está probada. | K167 ≥ 70% | La detención probada incluye a los agentes operados por proveedores: la organización puede detenerlos. | K167 ≥ 70% | OPE-PR-11 |
| C3-F6-KR3 | Los procesos críticos que usan IA pueden operar sin ella. | K56 ≥ 50% | Los procesos críticos pueden operar sin la plataforma de IA del proveedor. | K56 ≥ 50% | OPE-RC-04 |

### Criterios de salida de la etapa (6)

1. Funciones críticas en nivel «Probado»: ejercicio de adversario, prueba de recuperación y ejercicio de crisis realizados.
2. Recuperación de la identidad y de la plataforma de control probada en un entorno aislado.
3. Acceso a los recursos críticos decidido por una política con señales de contexto.
4. Reversibilidad comprobada: plan de salida ensayado y portabilidad verificada en los servicios críticos.
5. Escenarios prioritarios cuantificados y evidencia automática en los controles clave.
6. Agentes evaluados de forma adversarial y con detención de emergencia probada.

## Ciclo 4 · Demostrar y sostener · días 271 a 365

**Objetivo.** Rendir cuentas con evidencia, decidir con los datos del año qué se opera, qué se contrata y qué se cambia, y dejar instalado el ciclo que se repite cada año.

**Pregunta que responde.** ¿Cuál es nuestro nivel real de riesgo, mejoramos, invertimos bien y estamos preparados?

**Trampa habitual.** Un informe de logros sin pendientes, o un segundo año que repite el primero sin recalibrar.

**Resultado.** Informe anual al directorio y a los síndicos; plan y presupuesto del año 2; mandato renovado.

**En la versión 1.0.** F6 Demostrar y renovar · H365 Rendición de cuentas anual · 26 actividades del plan anterior.

### F1 · Gobierno y rendición de cuentas

**Objetivo.** Rendir cuentas con evidencia y renovar el mandato.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F1-KR1 | El informe anual se presentó al directorio y a los síndicos, con resultados, pendientes y aprendizajes. | Hito cumplido | El informe anual incluye el desempeño de cada servicio externalizado crítico y la dependencia de proveedores. | Hito cumplido | GOB-G6.1 |
| C4-F1-KR2 | Los riesgos altos tuvieron una revisión independiente. | K85 ≥ 50% | Los servicios críticos tuvieron la verificación independiente prevista. | KX05 ≥ 85% | GOB-G4.1 |
| C4-F1-KR3 | El mandato se revisó, y el plan y el presupuesto del año 2 están aprobados. | K65 ≥ 100% | El mandato revisado incluye la decisión de provisión de cada función para el año 2. | K65 ≥ 100% | GOB-G1.1 |

### F2 · Programa, personas y presupuesto

**Objetivo.** Dejar el programa en condiciones de repetirse cada año.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F2-KR1 | La ejecución presupuestaria cierra dentro del desvío tolerado. | K103 ≤ 10% | El costo por unidad de resultado de los servicios críticos cierra dentro del desvío tolerado. | KX16 ≤ 15% | GES-M1.2 |
| C4-F2-KR2 | El talento crítico se retiene. | K13 ≥ 85% | Ninguna función externalizada queda sin capacidad interna de supervisión. | KX15 ≥ 100% | GES-M1.2 |
| C4-F2-KR3 | Las funciones críticas alcanzan el nivel de evidencia «Probado». | KSG05 ≥ 3 nivel (0 a 4) | Las funciones que opera un proveedor también alcanzan el nivel «Probado», verificadas por la organización o por un tercero independiente. | KSG05 ≥ 3 nivel (0 a 4) | GES-M1.1 |

### F3 · Identificar y proteger

**Objetivo.** Sostener la postura y medir el resultado.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F3-KR1 | Los resultados del perfil objetivo se alcanzan. | K22 ≥ 50% | Los resultados del perfil objetivo se alcanzan también en las funciones que opera un proveedor. | K22 ≥ 50% | GOB-G2.1 |
| C4-F3-KR2 | No quedan desviaciones críticas de configuración abiertas más allá de lo tolerado. | K120 ≤ 3 n.º | El proveedor informa la deriva de lo que gestiona y la corrige dentro del plazo pactado. | K120 ≤ 3 n.º | GES-M3.2 |
| C4-F3-KR3 | Los controles clave tienen su efectividad probada. | K60 ≥ 60% | Los controles operados por proveedores tienen su efectividad probada de forma independiente. | K60 ≥ 60% | GES-M3.2 |

### F4 · Detectar, responder y recuperar

**Objetivo.** Convertir cada incidente y cada ejercicio en mejora.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F4-KR1 | Las acciones correctivas posteriores a los incidentes se cierran en plazo. | K48 ≥ 70% | Las acciones a cargo de los proveedores se cierran en plazo. | KX18 ≥ 85% | GES-M5.2 |
| C4-F4-KR2 | El tiempo de restauración de los servicios críticos queda dentro del objetivo. | K47 ≤ 100% del RTO | El tiempo de restauración se midió en una prueba con el proveedor de recuperación y queda dentro del objetivo. | K47 ≤ 100% del RTO | OPE-RC-02 |
| C4-F4-KR3 | Los falsos positivos de las detecciones prioritarias bajan al nivel objetivo. | K170 ≤ 40% | El proveedor reduce los falsos positivos al nivel pactado sin perder cobertura. | K170 ≤ 40% | OPE-DE-02 |

### F5 · Ecosistema

**Objetivo.** Decidir, con los datos del año, qué se opera, qué se contrata y qué se cambia.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F5-KR1 | La decisión de provisión de cada función —propia, co-gestionada o externalizada— se revisó con el costo y el resultado del año. | Hito cumplido | La renovación, la renegociación o el reemplazo de cada contrato crítico se decidió con el desempeño medido del año. | Hito cumplido | GES-M1.2 |
| C4-F5-KR2 | Los requisitos de seguridad de clientes y contratos se cumplen en plazo. | K23 ≥ 80% | Se cumplen en plazo también los requisitos que los clientes trasladan sobre la cadena de proveedores. | K23 ≥ 80% | GOB-G3.1 |
| C4-F5-KR3 | La paridad de control entre entornos alcanza el nivel de fin de año. | K123 ≥ 80% | Los servicios cubren todos los entornos del alcance. | KX19 ≥ 100% | GES-M3.2 |

### F6 · IA y agentes

**Objetivo.** Escalar la IA con autonomía gobernada.

| ID | Resultado clave (operación propia) | Meta | Resultado clave si la función está externalizada | Meta | Función |
|---|---|---|---|---|---|
| C4-F6-KR1 | Cada tipo de acción de los agentes en producción tiene un nivel de autonomía aprobado por el dueño del riesgo. | K88 ≥ 80% | El nivel de autonomía aprobado alcanza también a los agentes de proveedores. | K88 ≥ 80% | GOB-G4.2 |
| C4-F6-KR2 | Las acciones de agentes que deben revertirse se mantienen por debajo del límite. | K175 ≤ 2% | El proveedor informa las reversiones de sus agentes y se mantienen por debajo del límite. | K175 ≤ 2% | OPE-DE-06 |
| C4-F6-KR3 | Las decisiones automatizadas de alto impacto tienen supervisión humana verificada. | K98 ≥ 80% | La supervisión humana verificada alcanza a las decisiones que toma un sistema del proveedor. | K98 ≥ 80% | GOB-G6.2 |

### Criterios de salida de la etapa (6)

1. Informe anual presentado al directorio y a los síndicos, con pendientes y aprendizajes.
2. Verificación independiente de los riesgos altos y de los servicios críticos realizada.
3. Decisión de provisión revisada para cada función, con el costo y el resultado del año.
4. Plan, presupuesto y compromisos del año 2 aprobados; mandato renovado.
5. Ciclo anual de gobierno documentado: qué se repite cada año, cuándo y quién.
6. Indicadores con línea base, meta y tendencia de cuatro ciclos para las tres audiencias.

## El informe de los 90 días

El día 90 cierra el ciclo 1. Para entonces el diagnóstico lleva un mes cerrado, el plan y el presupuesto están aprobados y hay un primer avance que mostrar. Ocupa el lugar del informe de los 100 días de la versión 1.0 y coincide con el primer cierre trimestral de OKR.

## Cómo se corre el ciclo 1

El ciclo 1 es distinto de los otros tres porque empieza sin línea base.

| Momento | Qué se hace |
|---|---|
| Día 1 | Los seis objetivos del ciclo se abren como hipótesis de trabajo. |
| Desde las primeras semanas | Empiezan las correcciones que no admiten espera: autenticación resistente a la suplantación en las cuentas privilegiadas, vulnerabilidades explotadas activamente, telemetría de los activos críticos y una restauración probada. No esperan el cierre del diagnóstico. |
| Día 60 | Cierra el diagnóstico. Con la línea base se confirman o se corrigen las metas del ciclo 1. |
| Día 90 | Se puntúa el ciclo, se verifican los criterios de salida y se presentan el plan, el presupuesto y las decisiones requeridas a las tres audiencias. |

Si la organización no puede corregir en paralelo con el diagnóstico, la parte no alcanzada de las metas de K33, K46, K41 y K28 pasa al ciclo 2. Es el supuesto SUP-07 del documento 15 «Trazabilidad, fuentes, supuestos provisorios y silencios».

## Antes del día 1

El plan anterior incluye 7 actividades previas a la asunción: investigar el negocio, acordar el mandato y preparar la recepción. Siguen vigentes y están en la hoja «Actividades v1.0» del libro de plan anual.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

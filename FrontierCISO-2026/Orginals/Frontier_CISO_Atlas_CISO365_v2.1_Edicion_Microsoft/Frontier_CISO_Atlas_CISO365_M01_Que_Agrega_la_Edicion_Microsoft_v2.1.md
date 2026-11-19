# Qué agrega la edición Microsoft y qué no cambia

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M01 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Dos planos

El modelo separa dos planos, tal como lo hace TheNextCISO GM-24 V7.1.

|  | Plano A · Núcleo 2.0 | Plano B · Edición Microsoft |
|---|---|---|
| Qué contiene | Funciones, indicadores, OKR, criterios Zero Trust, cadencias, roles y narrativas | Capacidades contratadas, cobertura, licencias, tareas de operación, formación y fuentes de medición |
| De qué depende | De marcos y estándares abiertos | De los productos de un proveedor, de sus licencias y de su documentación |
| Cuándo cambia | Cuando cambia un marco o cuando la experiencia lo corrige | Cuando el proveedor cambia un producto, una licencia o una fecha |
| Quién lo usa | Cualquier organización | La que eligió la plataforma de Microsoft |

**Regla:** nada del plano B modifica el plano A. Si la organización cambia de proveedor, el núcleo queda igual y se reconstruye el plano B. Si Microsoft cambia un producto, cambia esta edición y no el plan.

## 2. Qué agrega esta edición

| Pregunta | Respuesta de la edición | Dónde está |
|---|---|---|
| ¿Con qué se cumple cada función? | 50 capacidades en 14 dominios, asignadas a 50 funciones | Hoja Funciones × Microsoft; documento M02 «Capacidades de Microsoft por función y por licencia» |
| ¿Qué licencia la trae? | Inclusión de cada capacidad en Microsoft 365 E3, E5 y E7, o si es de consumo | Hoja Capacidades; documento M02 «Capacidades de Microsoft por función y por licencia» |
| ¿Hasta dónde llega fuera de Microsoft? | Cobertura de cada capacidad en cinco entornos, con su límite y su fuente | Hoja Capacidades; documento M03 «Cobertura multicloud: hasta dónde llega Microsoft fuera de Microsoft» |
| ¿Cómo se diagnostica? | 11 herramientas de evaluación que aportan evidencia | Hoja Diagnóstico con Microsoft; documento M04 «Diagnóstico con herramientas de Microsoft» |
| ¿Cómo se opera? | 325 tareas por cadencia en ocho dominios, 11 guías oficiales y 12 guías del autor | Hoja Operación por cadencias; documento M05 «Operación por cadencias: excelencia operacional» y documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron» |
| ¿Con qué guía se adopta cada producto? | 23 guías del repositorio del autor: 833 acciones de configuración, de rutina y de respuesta, y 184 indicadores técnicos | Hojas Guías del repositorio, Acciones de las guías e Indicadores técnicos; documento M11 «Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación» |
| ¿Cómo se forma al equipo? | 15 programas asignados a los 25 roles, por ciclo | Hojas Formación y Plan de formación; documento M06 «Plan de formación con los Ninja Training» |
| ¿Dónde se mide? | Fuente y tipo de medición de los 224 indicadores | Hoja Indicadores × Microsoft; documento M07 «OKR e indicadores sobre la plataforma de Microsoft» |
| ¿Cómo se cuenta? | Ajustes a las tres narrativas | documento M08 «Narrativas para una organización que eligió la plataforma de Microsoft» |

## 3. Qué no cambia

- Las 59 funciones, sus identificadores y su escala de evidencia.
- Los 224 indicadores, sus fórmulas y sus umbrales.
- Los 24 objetivos y los 72 resultados clave, con su versión para funciones externalizadas.
- Los cuatro ciclos trimestrales del año. El diagnóstico ocupa los primeros 60 días del ciclo 1, que cierra el día 90.
- La regla de gobierno de los proveedores: se los mide por resultados y se los verifica. **Microsoft es un proveedor más y se le aplica la misma regla.**

## 4. Cuánto resuelve la plataforma

| Aporte de Microsoft | Funciones | Qué significa |
|---|:--:|---|
| Cubre | 23 | La plataforma aporta la capacidad principal de la función en los entornos que alcanza. |
| Cubre en parte | 16 | Aporta una parte; el resto depende de procesos, de personas o de otras herramientas. |
| Apoya | 12 | Aporta datos o evidencia, pero la función se resuelve fuera de la plataforma. |
| Fuera de la plataforma | 8 | Es una práctica de gobierno o de gestión: no hay capacidad de la plataforma que la cubra. |
| Total | 59 |  |

La plataforma cubre o cubre en parte 39 de las 59 funciones. Las demás son prácticas de gobierno y de gestión: ninguna herramienta las reemplaza. Un plan que se limita a activar productos deja sin atender esa parte, que es la que el directorio supervisa.

## 5. Lo que una plataforma única da y lo que quita

| Da | Quita o exige |
|---|---|
| Señales integradas entre identidad, dispositivos, correo, datos y nube | Dependencia de un proveedor: se mide con K27 y KX14 y pide un límite aprobado |
| Menos herramientas solapadas (K122) y un solo modelo de datos | Cobertura desigual fuera de Azure: hay funciones que requieren complemento |
| Capacidades ya incluidas en las licencias | Riesgo de pagar lo que no se usa: la adopción se mide capacidad por capacidad |
| Guías de operación y de evaluación del propio fabricante | Costos de consumo que crecen con el uso: ingesta de registros y protección de cargas |
| Un plano de control común para varias nubes | Fechas de retiro y cambios de producto que obligan a mantener el plano B |

## 6. Decisiones de diseño

1. **El núcleo no se toca.** Esta edición no agrega funciones, indicadores ni resultados clave.
2. **La cobertura se verifica en documentación oficial.** Donde la documentación no lo afirma, el valor es «no confirmado»; no se supone.
3. **La cobertura de una función es la mejor entre sus capacidades.** Indica que al menos una capacidad alcanza el entorno, no que la función esté resuelta allí.
4. **La adopción se mide.** Tener una licencia no es tener el control: cada capacidad lleva su estado de despliegue.
5. **Las tareas conservan su práctica de origen.** Cada tarea de producto ejemplifica una práctica que no depende de la plataforma.
6. **Lo que no pudo confirmarse se declara.** Ver el documento M09 «Fuentes, supuestos y silencios de la edición Microsoft».

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

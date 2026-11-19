# Evaluación de la actualización y plan de construcción

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 01 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Conclusión

Sí conviene actualizar el plan, y conviene hacerlo como una **versión 2.0 que extiende la 1.0 sin reemplazarla**. La razón principal no es Zero Trust para la IA, que es la vertiente menos madura. Es lo que le faltaba a la versión 1.0 y lo que cambió en la serie GM-24 entre las versiones 4 y 7.1.

## 2. Qué le faltaba a la versión 1.0

| Tema | Versión 1.0 | Versión 2.0 |
|---|---|---|
| Estructura del año | 7 fases y 7 hitos (H0 a H365) | Cuatro ciclos trimestrales de OKR —el primero empieza con un diagnóstico de 60 días—, con 34 criterios de salida |
| Qué hacer | 130 actividades en el libro (142 en el paquete integral del 13 de noviembre) y 54 rituales | Se conservan las 142 actividades, ubicadas en las etapas nuevas; se agregan 18 cadencias de operación del plan |
| Funciones | Las 24 unidades de gobierno y gestión de GM-24 | 59 funciones: las 24 anteriores y 35 servicios de operación |
| Operación | Sin indicadores por servicio de identificar, proteger, detectar, responder y recuperar | 90 indicadores de operación: 19, 36, 14, 11 y 10 por servicio |
| Indicadores | 64 del catálogo 1.2 y 6 del sistema de gestión | 224: los 70 anteriores sin cambios y 154 nuevos |
| OKR | Seis objetivos anuales | 24 objetivos y 72 resultados clave en cuatro ciclos y seis frentes |
| Servicios externalizados | 18 servicios descriptos, sin medición propia | Versión externalizada de cada función, resultado clave e indicador; 22 indicadores KX, 14 comprobaciones de contrato y 8 cláusulas mínimas |
| Arquitectura | Zero Trust mencionado como referencia | 42 criterios Zero Trust en ocho dominios, incluido el de IA y agentes |
| Varias nubes y varios proveedores | No tratado | Cobertura por entorno, paridad de control y solapamiento de herramientas |
| Diagnóstico | 56 entrevistas y 32 elementos de recepción | Se conservan; se agregan la calificación de 59 funciones, los criterios Zero Trust, los contratos y 24 preguntas nuevas |
| Impacto en la organización | Implícito | 12 categorías de presupuesto, 25 roles y 30 decisiones de impacto |
| Narrativas | Seis preguntas del directorio | Tres narrativas: CIO y CTO, CEO y CFO, directorio y síndicos |

## 3. Qué se tomó de TheNextCISO GM-24 V7.1

GM-24 V7.1 tiene 379 conceptos (245 K, 52 AMP, 40 HC y 42 PA), 139 más que los 240 de la versión 4. De ese cuerpo se tomó solo lo que no depende de un proveedor:

- **El control como producto con dueño**: objetivo, configuración de referencia y evidencia.
- **La grilla de propiedad** que cruza las funciones del marco con los dominios Zero Trust.
- **La operación por cadencias**: lo que se hace cada día, cada semana, cada mes y cada trimestre.
- **La fuerza de trabajo híbrida**: personas, proveedores y agentes.
- **El gobierno de los agentes**: identidad propia, límites, supervisión, retiro y una escala de autonomía de L0 a L4.
- **Los requisitos de IA en los contratos de servicios gestionados** y las **bases multiplataforma**.
- **La separación en dos planos**: el corpus, que no depende de proveedores, y las capacidades contratadas, que sí. Este documento es plano A; la edición Microsoft es plano B.

## 4. Qué aportó la investigación sobre Zero Trust

- Ninguna de las tres organizaciones consultadas tiene un estándar formal dedicado a «Zero Trust para la IA». Solo Microsoft usa esa denominación.
- En NIST son finales SP 800-207 (2020), SP 800-207A (2023), SP 1800-35 (2025) y CSWP 20 (2022). Lo referido a agentes y a IA está en borrador, en documento conceptual o en una entrada de blog.
- En The Open Group, los Zero Trust Commandments figuran como estándar; el modelo de referencia sigue en una versión preliminar y no trata la IA.
- Las fuentes coinciden en cinco prácticas para los agentes: identidad propia, mínimo privilegio por tarea, política aplicada fuera del modelo, registro independiente y aprobación humana para las acciones de alto impacto.

El documento 07 «Zero Trust y Zero Trust para la IA» desarrolla estos hallazgos y lista las fuentes.

## 5. Qué es firme y qué es provisorio

| Elemento | Firme | Provisorio | Por qué es provisorio |
|---|:--:|:--:|---|
| Criterios Zero Trust | 36 | 6 | Los de IA y agentes se apoyan en borradores y en guía de un proveedor |
| Indicadores | 208 | 16 | Miden prácticas de IA y agentes que los marcos aún no fijaron |
| Resultados clave | 60 | 12 | Los del frente F6, IA y agentes |

Además, los umbrales y las metas de los 154 indicadores nuevos son propuestas del modelo sin referencia externa. Los 8 supuestos y lo que haría revisarlos están en el documento 15 «Trazabilidad, fuentes, supuestos provisorios y silencios».

## 6. Decisiones de diseño

1. **La versión 1.0 no se toca.** Queda como versión anterior y como detalle de actividades.
2. **El año se mide en cuatro ciclos trimestrales.** Cada ciclo dura 90 días y el último termina el día 365. El diagnóstico ocupa los primeros 60 días del ciclo 1. Las duraciones son parámetros.
3. **El informe de los 100 días pasa a ser el de los 90 días.** Cierra el ciclo 1, con el plan y el presupuesto aprobados, y coincide con el primer cierre trimestral de OKR.
4. **Tres planos.** Gobierno y gestión siguen las 24 unidades de GM-24; operación se organiza por las funciones de NIST CSF 2.0.
5. **OKR para cambiar e indicadores para sostener.** Un resultado clave se cierra; un indicador se mide siempre.
6. **Cada elemento tiene versión externalizada.** Cambian el objetivo, el indicador y la evidencia; no cambia quién responde.
7. **Nada depende de un proveedor.** Lo específico de una plataforma es implementación y va en una edición aparte.
8. **Un único modelo de datos.** Los libros, los archivos HTML, los documentos y el catálogo JSON se generan de la misma fuente.

## 7. Qué no hace esta versión

- No fija dotaciones, salarios ni montos de presupuesto: da categorías, roles y un método.
- No traduce normas de un país o de un sector: la función GOB-G3.1 pide ese relevamiento a cada organización.
- No trae valores de referencia de otras organizaciones para los indicadores nuevos.
- No reemplaza las 56 entrevistas ni los rituales de la versión 1.0: los supone vigentes.

## 8. Revisión 2: por qué cuatro ciclos trimestrales

La primera entrega de la versión 2.0 separaba un diagnóstico de 60 días de cuatro ciclos de 75. Esa estructura tenía dos costos: los ciclos no coincidían con el trimestre —la unidad con la que la mayoría de las organizaciones fija y revisa sus OKR— y los hitos H180 y H270 de la versión 1.0 quedaban en medio de un ciclo. La revisión 2 adopta cuatro ciclos de tres meses.

| Tema | Antes | Ahora |
|---|---|---|
| Estructura del año | Diagnóstico de 60 días y cuatro ciclos de 75 días (el último, de 80): días 1–60, 61–135, 136–210, 211–285 y 286–365. | Cuatro ciclos trimestrales de 90 días (el último, de 95): días 1–90, 91–180, 181–270 y 271–365. El diagnóstico ocupa los primeros 60 días del ciclo 1. |
| Primer informe | Informe de los 100 días, dentro del ciclo 1. | Informe de los 90 días, en el cierre del ciclo 1. |
| Hitos | H30 y H60 en el diagnóstico; H100 en el ciclo 1; H180, H270 y H365 dentro de los ciclos 2, 3 y 4. | H30 y H60 dentro del ciclo 1; H90, H180, H270 y H365 coinciden con el cierre de cada ciclo. |
| Cierre de ciclo e informe trimestral | Dos momentos distintos: el ciclo cerraba cada 75 días y el informe al directorio era trimestral. | Un solo momento: el cierre de cada ciclo es el cierre del trimestre. |
| Objetivos y resultados clave | 24 objetivos y 72 resultados clave. | Los mismos 24 objetivos y 72 resultados clave, con las mismas metas. Cambia la fecha en que se miden. |
| Prácticas de operación | El núcleo no incluía prácticas de operación por cadencia. | Se agregan las prácticas independientes de la plataforma para riesgo interno y para el ciclo de vida de los datos (documento 16), y la hoja «Prácticas de operación» del libro de plan anual, con sus 56 rutinas. |

- **Qué se gana.** El plan del CISO usa el mismo calendario que el resto de la organización; el cierre de ciclo y el informe al directorio son un solo momento; y los cierres coinciden con los hitos de la versión 1.0, salvo el primero, que pasa del día 100 al día 90.
- **Qué se exige.** El ciclo 1 hace en 90 días lo que antes ocupaba 135. Es posible si las correcciones que no admiten espera empiezan antes de cerrar el diagnóstico. Los ciclos 2, 3 y 4 ganan 15 días cada uno.
- **Qué no cambia.** Las funciones, los indicadores, los 24 objetivos, los 72 resultados clave y sus metas. Las metas siguen siendo propuestas que se confirman con la línea base del día 60.
- **Cómo se revierte.** Las duraciones están en la hoja Parámetros del libro de plan anual. El supuesto SUP-07 del documento 15 «Trazabilidad, fuentes, supuestos provisorios y silencios» dice qué haría revisar la estructura.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

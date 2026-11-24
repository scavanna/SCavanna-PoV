# Gobierno, protección y observabilidad de IA

[Biblioteca](../README.md) · [Ficha de alta y evaluación](Alta-y-evaluacion-de-agentes.md) · [SOC y SOAR](SOC-y-SOAR.md)

**Entrada:** caso de uso y datos, usuario, agente o servicio que actuará. **Salida:** decisión de admitir, limitar, devolver a piloto o rechazar, con evidencia y responsable.

Separá tres perspectivas: **proteger el uso de IA**, **usar IA para defender** y **preparar la defensa frente a amenazas potenciadas por IA**. Esa distinción no es la misma que comparar tres opciones de licenciamiento.

## 1. Aplicá Zero Trust al caso concreto

La arquitectura Zero Trust exige verificar explícitamente, limitar privilegios y asumir compromiso; la ubicación en la red no concede confianza. NIST/NCCoE, The Open Group y Microsoft ofrecen referencias complementarias, no un único estándar de Zero Trust para agentes.

1. **Inventariá.** Qué sistema o agente decide o actúa, para qué proceso, con qué dueño, datos, modelos, herramientas y entornos.
2. **Identificá.** Cada agente tiene identidad y permisos propios. Una sesión de su creador, una cuenta compartida o un acceso heredado no sustituyen esa identidad.
3. **Acotá.** Limitá acciones, datos, conectores, tiempo y coste por diseño. Tratá documentos, resultados de herramientas y mensajes como datos no confiables; no como autorización para actuar.
4. **Protegé los datos.** Verificá permisos en la fuente, clasificación, minimización, ubicación y retención; probá la operación permitida y la denegada.
5. **Observá y respondé.** Registrá identidad, decisiones y uso de herramientas fuera del alcance de modificación del agente. Probá revocación, retirada y ruta sin IA.

El diagnóstico del Plan v2.0 agrega seis criterios de IA como propuesta dentro de sus 42 criterios Zero Trust. No los trates como conformidad normativa ni como un cruce 1:1 de indicadores.

## 2. Convertí el cuestionario 99×2 en agenda del CoE

Usá las 99 preguntas de agenda CISO y las 99 de IA para descubrir **decisiones sin evidencia**, no para producir un puntaje de madurez. Seleccioná las preguntas materiales al alcance, pedí evidencia con período y dueño, y clasificá el resultado: demostrado, parcial, no demostrado o no aplica con justificación.

| Dimensión | Pregunta de aceptación | Evidencia mínima |
| --- | --- | --- |
| Gobierno | ¿Quién acepta el uso, la autonomía y las excepciones? | Registro de agentes, mandato del dueño, análisis de riesgo y fecha de revisión. |
| Protección | ¿Qué impide que una identidad, herramienta o dato salga del límite aprobado? | Política efectiva, segregación y resultados de pruebas positivas y negativas. |
| Observabilidad | ¿Qué puede reconstruirse si la IA se equivoca o deja de estar disponible? | Registro correlacionado, acceso/retención, caso de prueba y evidencia del modo alternativo. |

Estas nueve combinaciones orientan la comprobación, no la compra:

| Escenario | Gobierno | Protección | Observabilidad |
| --- | --- | --- | --- |
| Capacidad actual | Delimitar cohortes habilitadas; reconciliar inventario y aprobación. | Probar acceso y DLP donde ya se aplican. | Levantar fuentes disponibles y demostrar qué se puede correlacionar. |
| Ampliación Purview Suite | Normalizar clasificación y excepciones; conservar revisión de identidad. | Confirmar asignaciones, cobertura y exclusiones por entorno. | Probar disponibilidad de eventos, retención y procedimiento de consulta. |
| Escenario Microsoft 365 E7 | Gestionar alta, alcance, recertificación y retirada por oleadas. | Verificar autorización, límites y reversión por plataforma. | Probar trazabilidad extremo a extremo y registrar exclusiones. |

## 3. Separá capacidad documentada de cobertura demostrable

Usá el análisis E7/Agent 365 **V4** como orden de comprobación: (1) inventario y responsables; (2) identidad y datos; (3) observabilidad y privacidad de registros; (4) frontera de ejecución y permisos; (5) evaluación y control de cambios; (6) evidencia y auditoría independiente; (7) recertificación. No avances una etapa si la siguiente depende de algo que aún no podés demostrar.

- **Potencial:** la documentación describe una opción. Verificar plan, contrato, región, restricciones y costes fuera de la suite.
- **Operativa:** está configurada y probada para una población concreta, con dueño y vuelta atrás.
- **Defendible ante auditoría:** además hay período, fuente, muestra, integridad, acceso, resultado y vigencia. No traslades un porcentaje editorial a un entorno real.
- **Preview:** etiquetá la evidencia y mantené una alternativa de disponibilidad general o manual. No hagas de una función preliminar el único control de un proceso crítico.

## Anexos de trabajo

- [Diagnóstico CISO v2.0](../01_Gobierno-CISO/artefactos/Frontier_CISO_Atlas_CISO365_Diagnostico_v2.0.xlsx), hoja `Zero Trust`: elegir criterios y puntuar con evidencia. Para la arquitectura de referencia, consultar [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).
- [Matriz de preguntas 99×2 v2](artefactos/99x2_Preguntas_CISO_IA_Matriz_COE_v2.xlsx): elegir preguntas por alcance y documentar evidencia y dueño. [Escenarios, evidencia y responsables](artefactos/AI_COE_escenarios_y_evidencias.xlsx): registrar qué cambia al ampliar el alcance.
- [Libro final de cobertura E7/Agent 365 V4](artefactos/M365_E7_Agent365_AI_Frameworks_V4_final.xlsx): dependencias, evidencia y límites. No acredita certificación, cobertura ni licenciamiento actuales.

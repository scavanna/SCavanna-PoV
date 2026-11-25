# Glosario y modelo conceptual

## 1. Reglas ontológicas

1. Una **amenaza** no es automáticamente un riesgo.
2. Una **vulnerabilidad** no es una amenaza ni una probabilidad.
3. Un **incidente** es una ocurrencia observada; un **escenario** es una posibilidad modelada.
4. Una técnica ATT&CK es una unidad de comportamiento, no una pérdida ni un control.
5. Una amenaza de privacidad puede existir sin ciberataque ni acceso no autorizado.
6. Un control solo reduce riesgo cuando su diseño, despliegue y operación están respaldados por evidencia.
7. “Ransomware” puede ser nombre corto de categoría; el registro ejecutivo debe descomponerlo como escenario.

## 2. Entidades mínimas

| Concepto | Definición operativa | Ejemplos | No confundir con |
|---|---|---|---|
| Activo | Recurso o capacidad valiosa con dueño y atributos críticos | ERP, identidad, dataset, reputación | Amenaza |
| Proceso | Actividad que transforma datos o presta un servicio | facturación, nómina | Activo aislado |
| Actor de amenaza | Persona, grupo o sistema con capacidad y propósito plausible | criminal, insider, proveedor | Técnica |
| Amenaza / fuente | Causa potencial de evento adverso | ransomware, error, incendio | Impacto |
| Evento amenazante | Ocurrencia modelada que altera un activo/proceso | cifrado, exfiltración | Consecuencia |
| Vulnerabilidad / precondición | Debilidad o condición explotable | MFA ausente, IAM excesivo | Evento |
| Riesgo inherente | Incertidumbre antes de efectos de controles considerados | pérdida operativa posible | Amenaza |
| Riesgo residual | Incertidumbre después de controles implantados y probados | impacto no evitado | Control |
| Consecuencia | Efecto sobre objetivos, activos o titulares | indisponibilidad, multa, daño | Causa |
| Incidente | Evento ocurrido que compromete o puede comprometer objetivos | cifrado real observado | Escenario |
| Control | Medida que modifica probabilidad, consecuencia o detectabilidad | segmentación, backup | Recomendación sin implantar |
| Evidencia | Artefacto verificable del diseño o funcionamiento | log, prueba, informe | Afirmación |
| Caso de uso | Actividad repetible con entradas, pasos, resultados y aceptación | modelar una API | Producto documental |
| Método | Procedimiento o lente para identificar amenazas | STRIDE, PASTA | Taxonomía |
| Marco | Estructura de principios/procesos aplicable al programa | NIST RMF, ISO 27005 | Técnica individual |
| Base de conocimiento | Repositorio mutable de comportamientos, patrones o mitigaciones | ATT&CK, CAPEC | Estándar normativo |

## 3. Enunciado canónico de escenario

> Existe riesgo de **[consecuencia medible]** sobre **[activo/proceso]** cuando **[evento amenazante]** es ejecutado/aprovechado por **[actor/fuente]**, facilitado por **[precondiciones/vulnerabilidades]**, afectando **[titulares/objetivos]**, dentro de **[horizonte y contexto]**.

Ejemplo:

> Existe riesgo de interrupción superior a 24 horas del ERP y pérdida de facturación cuando una intrusión cifra servidores críticos, facilitada por cuentas comprometidas, falta de segmentación o acceso privilegiado persistente, con impacto en continuidad, clientes y obligaciones de información.

## 4. Relación entre dominios

```text
Actor/fuente --ejecuta/inicia--> Evento amenazante
                                     |
                  Precondiciones -----+---- afecta --> Activo/Proceso
                                     |
                                     v
                        Escenario de riesgo
                          /        |       \
                Consecuencia    Controles    Evidencia
                          \        |       /
                           Riesgo residual
                                   |
                         Apetito / tratamiento
```

## 5. Privacidad

Para un dato personal registrar: finalidad, base legal, categorías, sujetos/titulares, ubicación, destinatarios, encadenados, transferencia, retención, derechos y impacto. LINDDUN no reemplaza ese modelo regulatorio.

## 6. Estados válidos

`propuesto`, `diseñado`, `implantado`, `probado`, `efectivo`, `inefectivo`, `no-aplicable`, con justificación y fecha. El estado debe distinguir diseño de funcionamiento; un control “implantado” no equivale a “efectivo”.

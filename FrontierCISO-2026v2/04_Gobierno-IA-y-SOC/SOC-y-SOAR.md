# SOC agéntico y SOAR: piloto defensivo verificable

[Gobierno de IA](README.md) · [Ficha de evaluación](Alta-y-evaluacion-de-agentes.md) · [Biblioteca](../README.md)

Empezá por una tarea defensiva acotada y asistida, sin escritura en producción. La arquitectura de SOC y la guía multi-SIEM v3.0 orientan el diseño, no representan un despliegue validado.

## Qué pilotear primero

| Caso | Entrada y salida permitidas | Control humano y evidencia |
| --- | --- | --- |
| Agrupación y priorización | Señales autorizadas → propuesta de duplicados y severidad. | El analista conserva la decisión. Medir un conjunto de falsos positivos y negativos, no solo la velocidad. |
| Triaje asistido | Incidentes de prueba → resumen con hechos, fuentes y lagunas. | Comparar contra evidencia, proteger datos y rechazar un resumen que no se pueda verificar. |
| Enriquecimiento entre SIEM | Casos normalizados de fuentes autorizadas → contexto y deduplicación. | Preservar procedencia, hora e ID; comprobar duplicado, pérdida, reintento y caída de fuente. |
| Cola de aprobación | Caso y justificación → solicitud de decisión, no acción automática. | El aprobador es distinto de la identidad del agente. Deben quedar registrados resultado, autoridad y motivo. |

Para un SOC híbrido, acordá cuál SIEM conserva el incidente oficial y quién responde por el traspaso entre Sentinel y el entorno local. Definí campos, calidad, retención y tiempo de origen antes de automatizar. Un conector disponible no acredita cobertura ni continuidad; conservá una cola manual probada.

## Antes de ampliar el piloto

1. **Dueño del producto-control:** define el resultado y las fronteras. El analista decide sobre el caso. Plataforma mantiene el flujo; Riesgos y Privacidad validan el tratamiento cuando corresponde.
2. **Evaluación:** contrastá con un conjunto etiquetado de casos sintéticos. Compará exactitud, omisiones, tiempo de analista y abstenciones; no sacrifiques calidad para ganar velocidad.
3. **Fallos controlados:** comprobá duplicados, fuente caída, datos contradictorios, falta de permiso y saturación de cola. La salida segura es abstenerse, escalar o pasar a modo manual.
4. **Freno:** ninguna propuesta de contención cambia estado de producción sin autoridad explícita y procedimiento aprobado. El humano debe poder detener, revertir y verificar la acción.
5. **Aceptación:** registrá la evidencia, límites y capacidad de operar sin IA. Repetí evaluación si cambia el modelo, la fuente, la identidad o la operación.

Sentinel, Logic Apps y Security Copilot tienen guías locales; Foundry y Copilot Studio aportan referencias formativas y de evaluación. No se comprobó una integración de extremo a extremo con MDASH, Perception ni Power Platform. Los perfiles del plano aplicado GM-24 son insumos de diseño, no agentes operativos.

## Registro de piloto

| Caso / fuente | Resultado actual | Meta y control de seguridad | Muestra, errores y transiciones | Decisión, dueño y reversión |
| --- | --- | --- | --- | --- |
| | | | | |

- [Assessment multi-SIEM v3.0](artefactos/Assessment_SOAR_LogicApps_Sentinel_SIEM_OnPrem_V3.xlsx): revisión de coexistencia, responsabilidades y preparación.
- [Cartera de pilotos defensivos](artefactos/cartera-pilotos-defensivos.csv): ideas de evaluación con evidencia de salida; no despliegues.
- [Responsabilidades del Product Owner](../03_Operacion-y-formacion-Microsoft/README.md) · [Respuesta y continuidad sin IA](../02_Amenazas-y-resiliencia/Ransomware.md).

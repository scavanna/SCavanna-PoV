# Ficha de alta, evaluación y retiro de un agente

[Gobierno de IA](README.md) · [Biblioteca](../README.md)

Completala por caso de uso y entorno. Esta ficha no autoriza un despliegue por sí sola. Un cambio material en datos, conectores, permisos, modelo o propósito exige nueva revisión.

| Campo | Completar |
| --- | --- |
| Propósito, servicio de negocio, responsable y suplente | |
| Usuarios, entorno, población y datos permitidos | |
| Identidad propia, herramientas y permisos mínimos | |
| Operaciones permitidas, prohibidas y sujetas a aprobación | |
| Retención, acceso a registros, responsable de privacidad | |
| Límites de autonomía y criterios para abstenerse/escalar | |
| Alternativa sin IA, responsable de suspensión y tiempo de revocación objetivo | |
| Decisor, revisión, vencimiento de excepción, referencia de evidencia | |

## Criterios de prueba

| Comprobación | Criterio observable | Evidencia |
| --- | --- | --- |
| Exactitud y límites | En un conjunto representativo de casos sintéticos, las afirmaciones importantes tienen fuente y las dudas se declaran. | Muestra, versión, evaluación humana y errores clasificados por impacto. |
| Confidencialidad | Solo ve la población autorizada; no expone datos restringidos en respuesta ni en trazas. | Resultados de pruebas permitidas y denegadas, y revisión de registros. |
| Acción y autorización | No sale del alcance ni modifica estado sin aprobación segregada; el contenido recibido no amplía permisos. | Registro de una solicitud rechazada o escalada y verificación del control fuera del agente. |
| Trazabilidad | Un revisor reconstruye qué ocurrió, con qué identidad, qué hizo la herramienta y quién decidió. | Caso correlacionado y evidencia conservada en un entorno autorizado. |
| Retiro | La suspensión y la revocación impiden nuevas acciones, y el proceso sigue de forma segura sin IA. | Prueba del apagado, control de pendientes y aceptación del dueño de negocio. |

Definí antes del piloto las metas y el conjunto de pruebas. Un acceso no autorizado, una acción fuera de alcance o una fuga de datos no se compensa con una buena exactitud promedio.

**Decisión:** rechazar / devolver al piloto / autorizar con alcance escrito. Si falta evidencia, no se autoriza el aumento de autonomía. Para retirar: suspender, revocar, conservar los registros necesarios, reconciliar pendientes y obtener conformidad del dueño del servicio.

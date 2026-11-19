# Narrativas para una organización que eligió la plataforma de Microsoft

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M08 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## Cómo usar este documento

Las tres narrativas del núcleo (documentos 12, 13 y 14) siguen siendo la base. Este documento indica qué agregar y qué cuidar cuando la organización eligió la plataforma de Microsoft. Reemplace los datos entre corchetes por los de su diagnóstico.

## 1. Lo que cambia en las tres

| Punto | Qué decir | Dato que lo sostiene |
|---|---|---|
| La plataforma ya está, en parte, pagada | Antes de pedir herramientas nuevas, mostramos cuánto de lo licenciado está desplegado. | [Capacidades licenciadas]; [capacidades con despliegue completo]; hoja Resumen, bloque 3 |
| La plataforma no resuelve el gobierno | De las 59 funciones, la plataforma cubre o cubre en parte 39. El resto son decisiones y prácticas. | Hoja Resumen, bloque 2 |
| Fuera de Azure la cobertura es desigual | Decimos dónde llega, dónde llega en parte y dónde hay que complementar. | [Funciones que requieren complemento en los entornos del alcance]; hoja Funciones × Microsoft |
| Elegir una plataforma es concentrar | Lo medimos y pedimos un límite. Microsoft es un proveedor y se lo gobierna como a cualquier otro. | [K27]; [KX14] |
| Hay costos que crecen con el uso | Separamos lo que viene en la licencia de lo que se paga por consumo. | 18 capacidades de consumo; categorías P03 y P04 del presupuesto |

## 2. Para el CIO y el CTO

**Mensaje que se agrega.** *Vamos a usar lo que ya tenemos antes de sumar herramientas, y vamos a extender la misma línea base a todas las nubes. Para eso necesito tres cosas de sus equipos: conectar las cuentas de las otras nubes, incorporar los servidores que están fuera de Azure y sumar a la telemetría central las fuentes que hoy no llegan.*

| Qué pedir | Por qué | Cómo se ve el avance |
|---|---|---|
| Conectar las cuentas y los proyectos de AWS y de Google Cloud a la postura de nube | Sin conector, ese entorno no aparece en ninguna puntuación | K134 · K123 |
| Incorporar con Azure Arc los servidores y los clústeres que están fuera de Azure | Es el requisito para extender la protección, la línea base y la actualización | K41 · K141 |
| Ingresar las señales de otras nubes y de terceros por los conectores del registro central | La correlación nativa solo incluye productos de Microsoft | K41 |
| Federar las otras nubes y las aplicaciones SaaS con el directorio | El acceso condicional y el gobierno de identidades llegan por federación | K33 · K118 |
| Planificar el paso de Microsoft Sentinel al portal de Defender | El portal de Azure deja de tener soporte después del 31 de marzo de 2027 | Hito en el plan |
| Definir quién opera las tareas por cadencia de cada dominio | Una capacidad desplegada y sin operar no es un control | Nivel de operación por dominio |

| Objeción | Respuesta |
|---|---|
| «Si ya tenemos la licencia, ya estamos cubiertos.» | La licencia da derecho a usar. La hoja Capacidades muestra qué está desplegado, y la de operación, qué se ejecuta. |
| «Microsoft cubre también las otras nubes.» | En parte. De las 250 coberturas verificadas, 87 son parciales y 64 no pudieron confirmarse en la documentación. Hay funciones que piden las herramientas nativas de cada nube. |
| «Conectar todo al registro central es caro.» | Por eso se decide fuente por fuente, con su costo de ingesta y de retención. Lo que no se ingiere se declara como fuera de la detección. |
| «Con una sola plataforma ya no hace falta arquitectura.» | Hace falta más: la plataforma integra lo suyo, y la frontera con lo demás hay que diseñarla. |

## 3. Para el CEO y el CFO

**Mensaje que se agrega.** *Ya invertimos en una plataforma. Mi primer compromiso es que rinda: voy a mostrar cuánto de lo que pagamos está en uso y qué falta para usar el resto. Lo que la plataforma no cubre lo voy a traer con nombre y con costo, y la dependencia de un proveedor la vamos a medir.*

| Qué pedir | Por qué | Cómo se ve el avance |
|---|---|---|
| Aprobar el plan de adopción de lo ya licenciado antes de nuevas compras | Es la inversión de menor costo marginal | [Adopción promedio]; K17 · K104 |
| Decidir el plan de licencias con el mapa de capacidades | De E3 a E5 se incluyen 19 capacidades; de E5 a E7, 5 más, sobre todo de identidad y de agentes | Hoja Resumen, bloque 4 |
| Presupuestar aparte lo que se paga por consumo | Crece con los servidores, los recursos y los registros | K103 · categorías P03 y P04 |
| Aprobar los complementos para lo que queda fuera | Respaldo y recuperación en otras nubes, servicios de plataforma de otras nubes y funciones de gobierno | Hoja Funciones × Microsoft, columna «Qué queda fuera» |
| Fijar el límite de concentración por proveedor | Elegir una plataforma es una decisión de riesgo | K27 · KX14 |
| Financiar la formación del equipo | La plataforma rinde según quien la opera | K12; plan de formación |

| Objeción | Respuesta |
|---|---|
| «¿Por qué pedir más si ya pagamos la licencia más alta?» | Porque 18 capacidades son de consumo en cualquier plan, y porque 20 funciones no dependen de ninguna licencia. |
| «¿No es riesgoso depender de un solo proveedor?» | Es un riesgo y se lo trata como tal: se mide, tiene un límite aprobado y un plan de salida para lo crítico. La alternativa, muchas herramientas sin integrar, tiene otro riesgo, que también se mide. |
| «¿Cómo sé que la plataforma está rindiendo?» | Por la adopción de cada capacidad, por el nivel de operación de cada dominio y por los indicadores del tablero. Los tres se informan en cada cierre de ciclo. |

## 4. Para el directorio y los síndicos

**Mensaje que se agrega.** *La organización eligió una plataforma de seguridad. Esa decisión trae integración y trae concentración. Al directorio le corresponde conocer la segunda: de cuántas funciones críticas depende un mismo proveedor, qué límite se acepta y qué plan existe si hubiera que salir.*

| Qué informar | Dónde está |
|---|---|
| Funciones críticas cuya herramienta principal es de un mismo proveedor | KX14; hoja Funciones × Microsoft |
| Servicios críticos sin alternativa | K27 |
| Lo que la plataforma no cubre en los entornos de la organización | Estado en el alcance; Frontier_CISO_Atlas_CISO365_M03_Cobertura_Multicloud_v2.1.md |
| Cuánto de lo contratado está en uso | Adopción; hoja Resumen |
| Cómo se gobiernan los agentes de IA y con qué supervisión humana | K98; frente F6 del plan |
| Fechas de cambio que obligan a decidir | Supuesto SUPM-07; Frontier_CISO_Atlas_CISO365_M09_Fuentes_Supuestos_y_Silencios_v2.1.md |

| Pregunta que el directorio debería hacer | Qué respuesta esperar |
|---|---|
| ¿De qué proveedor dependemos más y cuál es el límite aprobado? | Un número (KX14), un límite y la fecha en que se revisa |
| ¿Qué pasa si ese proveedor tiene una falla grave o cambia sus condiciones? | Un plan de continuidad y un plan de salida para lo crítico, con su última prueba |
| ¿Qué no ve la plataforma? | La lista de entornos y de funciones fuera de su alcance, con el complemento elegido |
| ¿Pagamos por capacidades que no usamos? | La adopción por dominio y el plan para cerrarla |
| ¿Quién verifica lo que la plataforma informa sobre sí misma? | La verificación independiente anual del núcleo (RT17) |

## 5. Lo que no conviene decir

- **«Con esta plataforma estamos seguros.»** Ninguna plataforma lo garantiza, y la afirmación no se puede sostener ante un incidente.
- **«La plataforma cubre todo.»** La cobertura fuera de Azure es desigual y hay funciones que ninguna herramienta resuelve.
- **«Ya lo tenemos.»** Licenciado no es desplegado, y desplegado no es operado.
- **Cifras del fabricante como propias.** Los indicadores que se informan son los de la organización, con su fuente y su fecha.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

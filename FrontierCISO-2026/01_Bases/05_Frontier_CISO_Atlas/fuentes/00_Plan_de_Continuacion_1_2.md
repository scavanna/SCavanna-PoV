# Frontier CISO Atlas — Plan de continuación (versión 1.2)

| Campo | Valor |
|---|---|
| Iniciativa | Frontier CISO Atlas 1.2: revisión crítica de la versión 1.1 y mejora |
| Fecha del plan | 15 de noviembre de 2026 |
| Solicitante y autoridad de aprobación | Santiago Cavanna |
| Pedido | Aceptación en bloque de «las decisiones propuestas». Y, en condicional: «Si es necesario someter todo al escrutinio de un agente crítico […] entonces proponé una forma de implementar la revisión crítica y la mejora posterior para obtener al final una nueva versión aún más consistente». Este plan es esa propuesta. Se ejecutó sin esperar respuesta, porque el mensaje terminaba con «informa y continua»: esa lectura queda a confirmar (decisión D-14.5) |
| Línea de partida | Frontier CISO Atlas 1.1 publicado: Taxonomía 6.0, Ontología 2.1.0, grafo candidato de 5.041 nodos, decisiones D-01 a D-10 |
| Estado | Ejecutado entre el 15 y el 16 de noviembre de 2026; el registro está en `docs/09_Bitacora_de_Tareas.md`, fases 15 a 21, y el informe en `docs/13_Revision_critica_1_2.md` |

## 1. Punto de partida

- El autor aceptó «las decisiones propuestas» en bloque, con un supuesto: que no fueran contradictorias y apuntaran a la excelencia y al rigor.
- Aceptó también que el contenido no tiene validación humana.
- Escribió que, si hacía falta el escrutinio de un agente crítico, se propusiera una forma de implementar la revisión y la mejora posterior.
- Escribió cómo entiende que funciona el Atlas: como guía y orientación, que un CISO lee sin creer nada por defecto y acepta con una responsabilidad final que no se delega.

## 2. Qué se propone

Una revisión en seis pasos:

1. **Registrar la aceptación y comprobar su condición.** Ver si las diez decisiones se contradicen y en qué orden pueden aplicarse.
2. **Congelar la versión 1.1.** Los revisores leen una copia que no cambia.
3. **Revisar con lectores de contexto independiente.** Cada revisor tiene contexto propio, un encargo escrito y un formato de hallazgo. No ve el trabajo de los demás.
4. **Decidir sobre cada hallazgo.** Corregir, corregir en parte, proponer al autor, diferir o documentar. Por escrito.
5. **Aplicar y regenerar.** Los ajustes entran por un archivo único; todo lo demás sale de los guiones.
6. **Verificar y publicar.** Regresión, verificación de cierre a cargo de revisores que no participaron, y publicación junto a las versiones anteriores.

## 3. Dimensiones de la revisión

| Dimensión | Qué se revisa | Cómo |
|---|---|---|
| Consistencia | Que los documentos digan lo que dicen los datos | Un revisor recalcula las cifras |
| Taxonomía y decisiones | Criterios de admisión, reglas, coherencia entre decisiones | Un revisor |
| Ontología y grafo | Reglas, validación, conjuntos de cambios y preguntas de competencia | Un revisor, con consultas sobre la base |
| Categorización | D20, migraciones y una muestra del corpus | Segundas lecturas; la muestra, a ciegas |
| Biblioteca cognitiva | Tipos, pilar, prácticas contra sesgos, territorios y duplicados | Tres revisores |
| Medición | Indicadores por variable, coordenada y subfunción | Tres revisores |
| Hechos externos | Versiones, fechas y estructuras de marcos y normas | Verificación contra las páginas de los organismos |
| Lectura de un CISO escéptico | Qué se sostiene, qué sobra, qué falta para usarlo | Un revisor, que además lee la serie APX |

## 4. Reglas de trabajo

Se mantienen las de los planes anteriores. Se agregan siete:

1. **Quien generó no revisa.** Los revisores trabajan con contexto independiente.
2. **Dos lecturas o una adjudicación escrita.** Un cambio de coordenada se aplica cuando dos lecturas coinciden, o cuando una adjudicación escrita se apoya en la tesis y en una regla explícita. Si no, queda como estaba y se informa.
3. **Las reglas las decide el autor.** Lo que la revisión propone sobre la taxonomía se escribe y no se aplica.
4. **Las fuentes del autor no se modifican:** ni el GM-24, ni el banco de pre-ensayos, ni la base de la Biblioteca, ni el catálogo CISO 365.
5. **Lo publicado no se toca.** Las versiones 1.0 y 1.1 quedan como están.
6. **Todo hallazgo tiene una decisión escrita.** Los de severidad crítica o alta se informan uno por uno.
7. **Los límites se dicen junto a las cifras.**

## 5. Criterio de terminado

| Tarea | Terminado cuando |
|---|---|
| Registrar la aceptación | Cada decisión está escrita como proposición, con la opción tomada, su clase y sus dependencias |
| Revisar | Todos los encargos cerraron y sus salidas pasan el validador |
| Decidir | Los hallazgos tienen decisión, acción y lugar donde se ve |
| Aplicar | El grafo valida sin errores y se reconstruye desde sus conjuntos de cambios |
| Documentar | Las cifras salen de los datos; hay un informe de la revisión y una fe de erratas de lo anterior |
| Verificar | Regresión sin diferencias, y verificación de cierre leída: lo que encuentra se corrige o se lista antes de publicar |
| Publicar | Paquete 1.2 publicado; versiones 1.0 y 1.1 intactas |

## 6. Riesgos y supuestos

| Riesgo o supuesto | Tratamiento |
|---|---|
| Los revisores comparten configuración con quien generó los artefactos | Se declara como límite: tienen contexto independiente, no juicio independiente, y pueden compartir un mismo error. La revisión humana sigue pendiente |
| Una aceptación en bloque puede leerse como validación | Se separan las decisiones de diseño de las tareas de validación |
| Corregir puede introducir errores nuevos | Cada cambio queda registrado con su valor anterior y es reversible; hay una verificación de cierre |
| Una segunda lectura con texto recortado decide peor | Se declara el recorte; lo que no coincide no se cambia |
| La revisión puede no terminar por fallas de ejecución | El estado se guarda en archivos; un revisor que falla se relanza una vez |

## 7. Resultado

13 revisores dejaron 364 hallazgos, y 3 verificaciones externas revisaron 44 puntos más. El archivo de cambios tiene 183 filas. Cuatro revisores más leyeron la versión corregida y encontraron 139 problemas, 11 de severidad alta; se corrigieron antes de publicar. Una lectura final de consistencia, sobre la versión ya corregida, dejó 16 más (2 altos, 14 medios): 14 corregidos, 2 corregidos en parte. Quedan cuatro decisiones para el autor (D-14, D-11, D-13 y D-12, en ese orden) y la revisión humana de la categorización. El detalle está en `docs/13_Revision_critica_1_2.md`.

### Lo que el plan no preveía

- **Que hubiera que interpretar el mensaje del autor.** Dos de las diez decisiones eran preguntas, el supuesto de la aceptación se cumplió en parte y el pedido de revisión estaba en condicional. El plan lo trató como un registro; la verificación de cierre mostró que eran lecturas que el autor tiene que confirmar. De ahí sale la decisión D-14.
- **Que la muestra a ciegas necesitara otro estrato.** El plan pedía «una muestra del corpus». La que se hizo no tenía pre-ensayos de confianza media; se completó en la verificación de cierre.
- **Que el triaje necesitara su propia lectura.** La regla «quien generó no revisa» no alcanzaba a quien decide qué hacer con cada hallazgo, que fue quien generó los artefactos. La verificación de cierre leyó una parte de esas decisiones.
- **Que la versión corregida tuviera errores nuevos.** El riesgo estaba previsto y el tratamiento funcionó, pero lo corregido después de la verificación de cierre no lo volvió a leer ningún revisor.

## 8. Entregables

Paquete `Frontier_CISO_Atlas_v1.2`: los documentos 01 a 13, los catálogos y el grafo candidato corregidos, 16 conjuntos de cambios, las instrucciones 7.2 del agente curador, el material completo de la revisión y este plan.

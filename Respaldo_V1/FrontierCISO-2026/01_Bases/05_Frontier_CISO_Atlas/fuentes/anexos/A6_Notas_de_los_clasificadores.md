# Notas de cierre de los clasificadores (casos dudosos y criterios aplicados)

Cada bloque es el mensaje final del agente que propuso la categorización de un lote. Sirve como lista de trabajo para el curador.

## Lote 1

**Lote 1 — cierre.** El validador responde `LOTE 1: OK (93 registros válidos)`; la salida está en `salida_1.jsonl`.

- **Registros:** 93, todos clase K, mismos ids y orden que la entrada.
- **Cambios de dominio primario hacia los nuevos:** D25: 0, D26: 0, D27: 0, D28: 6 (G2.1-K08, G2.2-K10, G3.2-K02, G3.2-K03, G3.2-K06, G5.1-K10).
- **Otros cambios respecto de `v53`:** 1, G2.2-K06 pasa de D06 a D01 por error evidente. No cambié ningún territorio.
- **Asignaciones sin valor previo:** la subfunción venía vacía en los 93 y la asigné en todos. G2.1-K11 venía sin territorio ni dominio; quedó en T08/D01.
- **Horizontes:** H01 85, H02 4, H03 0, H04 3, indeterminado 1.
- **MCCS:** OS 39, DO 28, MM 22, NX 4.
- **Confianza:** alta 54, media 38, baja 1.

**Casos dudosos**

1. **G2.2-K06 Aplicación (Enforcement):** el texto trata la aplicación de políticas y no menciona datos, por eso propuse D01. Si el D06 vigente era intencional (por ejemplo, DLP), hay que revertirlo.
2. **G3.2-K03 Supervisión de Auditorías:** propuse D28 por tratar la auditoría como disciplina. La alternativa es conservar D03, como en «Auditorías de Cumplimiento» queda en D03 con D28 secundario.
3. **G3.2-K08 KPIs de Cumplimiento:** conservé D03 con D28 secundario, por analogía con «Métricas de Apetito» queda en D02 con D28 secundario. Podría ir a D28 por tratarse de métricas e indicadores.
4. **G3.1-K06 Gestión de Privacidad:** conservé D03 con D07 secundario, aunque la tesis (finalidades, retención, derechos) coincide con D07.
5. **G1.1-K10 Mejora Continua (Gobierno):** elegí RC04 por la pista ID.IM y la etiqueta literal, lo que deja un concepto de gobierno en la función RC. Las alternativas son GV07 o ID05.
6. **G2.1-K11 CSF 2.0 completo:** sin `v53`, lo ubiqué en T08/D01/GV03 por afinidad con G2.1-K04. La tesis (ownership, perfiles para invertir) también sostiene T03 o T02 como primario.
7. **G2.1-K01 Marcos de Gobierno y G2.1-K02 COBIT:** elegí GV03 (marco como estándar) frente a GV02 (estructura de gobierno), que quedó como secundaria.
8. **G4.1-K01 Enfoque Organizacional:** puse H04 porque la tesis es gobernar el ciberriesgo dentro del riesgo corporativo; H01 también es defendible. A la inversa, dejé en H01 a G1.1-K08 y a G3.1-K07 Cumplimiento Integrado.
9. **G2.1-K10 Evolución Histórica:** confianza baja; el texto no apunta a ningún resultado y GV03 va por afinidad con la unidad.
10. **G3.2-K07 Automatización:** conservé D03 con D28 secundario y H02. La mención de un agente no lo llevó a D23 ni a T07. En MCCS elegí NX frente a DO.

## Lote 2

**LOTE 2: OK — 93 registros** (`salida_2.jsonl`, validador en verde).

- **Cambios de dominio primario:** D25 = 9, D26 = 0, D27 = 0, D28 = 11.
- **Otros cambios respecto de v53:** 4.
  - Dominio: G6.1-K07 (D14→D04), M2.1-K01 y M2.1-K03 (D06→D13).
  - Territorio: M2.1-K04 (T07→T05).
- **Asignaciones sin v53:** M3.1-K11 (T05/D25) y M3.1-K12 (T05/D27). La subfunción venía vacía en los 93 y la asigné en todos.
- **Horizontes:** H01 88, H02 5.
- **MCCS:** DO 76, OS 10, MM 5, NX 2.
- **Confianza:** alta 50, media 41, baja 2.

**Casos dudosos**
1. M3.1-K06 ZTNA (Acceso): conservé D10 con confianza baja porque el control de un pilar concreto queda en el dominio del pilar; el texto no habla de nube y apunta a D05, como M2.2-K06.
2. M3.1-K07 Microsegmentación: conservé D10 por la misma regla; el pilar podría ser D08.
3. M3.2-K08 Familias de Controles (y K01, K03, K05, K10): conservé D13, que parece el comodín de 5.3 para el ciclo de vida de controles; K08 va con confianza baja.
4. G6.2-K05 y M1.1-K07 pasaron a D28 (la métrica es el objeto), pero G6.2-K06 Efectividad Programa quedó en D04 y G5.2-K09 en D02 porque si el objeto es el riesgo y la métrica es un medio, queda en D02. La frontera es fina.
5. G6.1-K07 Gestión Expectativas: D14→D04 (el SIEM es solo el ejemplo); la alternativa es D01.
6. G6.1-K05 Reportes Factuales: D14→D28; la alternativa es D01.
7. M2.1-K04 Ciclo de Vida Datos: T07→T05, porque T07 no se asigna por mera mención de IA.
8. M2.2-K03 y M3.1-K09: conservé T07 porque el escenario es de autoridad de agentes, aunque la tesis es de arquitectura (T05 quedó como secundario).
9. M3.1-K10 Resiliencia (Diseño): D16→D25 con PR06.
10. M3.1-K12: territorio T05 frente a T08. G6.2-K07 y M1.1-K10 Mejora Continua: RC04 frente a ID05.

## Lote 3

- **Registros:** 93 (59 K y 34 AMP).
- **Cambios de dominio primario a los nuevos:** D25 = 0, D26 = 0, D27 = 0, D28 = 2 (AMP-13 desde D03 y AMP-14 desde D20).
- **Otros cambios respecto de v53:** 8, todos de dominio.
  - M4.2-K01: D12→D13, por error evidente (el objeto es la gestión de vulnerabilidades).
  - M6.2-K10: D11→D17, porque la cadena de suministro de software y de IA va en D17.
  - AMP-06, AMP-12 y AMP-25: D20→D01; AMP-17, AMP-20 y AMP-22: D20→D02. En los seis casos apliqué que gobierno, riesgo y cumplimiento de la IA van en D01, D02 o D03 con territorio T07.
  - No cambié ningún territorio. La subfunción venía vacía en los 93 y la asigné en todos.
- **Horizontes:** H01 52, H02 21, H03 14, H04 5, indeterminado 1.
- **Pilares MCCS:** DO 65, OS 10, NX 10, MM 8.
- **Confianza:** alta 57, media 33, baja 3.

**Casos dudosos**

1. **M4.2-K06 Superficie de Ataque:** conservé D12; podría ir a D13, ya que inventario de activos, configuración segura y postura van en D13. Quedó como secundario.
2. **AMP-26 Supervisión humana efectiva:** conservé D21 con confianza baja; el objeto parece gobierno de la autonomía (D01) o factores humanos (D24).
3. **AMP-28 Orquestación de agentes:** conservé D21; los traspasos entre agentes como punto de riesgo apuntan a D20.
4. **AMP-16 Homeostasis y fuerzas de cambio:** conservé D02 con confianza baja; el objeto es estabilizar el cambio, más cerca de D04 o D24.
5. **M4.2-K02 Modelado de Amenazas:** conservé T07 con confianza baja; solo la tensión menciona agentes y el resto del texto apunta a T05.
6. **M4.2-K07 Riesgos Emergentes:** conservé T06/D12; se lee como T04/D02, que quedaron como secundarios.
7. **M6.2-K10 SBOM:** el cambio a D17 es defendible pero no unánime; además dudé entre H03 y H02.
8. **AMP-12 Responsabilidad por agentes:** sale de D20, pero el destino podría ser D17 o D03 en vez de D01. La misma duda de destino vale para AMP-17 (D02 o D01) y AMP-25.
9. **M6.1-K05 Pruebas Continuidad:** quedó en D16 con D28 secundario; podría ser D28 primario, porque D28 aplica cuando el objeto es el método para demostrar o medir la eficacia. Lo mismo vale para M5.1-K06 Tabletop, que quedó en D15.
10. **M6.2-K06 Shadow AI:** conservé D20 como activos de IA no inventariados; podría ser gobierno de la IA (D01).

## Lote 4

**Lote 4 — cierre**

- **Registros:** 93, en `salida_4.jsonl`; el validador responde `LOTE 4: OK (93 registros válidos)`.
- **Cambios de dominio primario hacia los nuevos:**
  - D25: 2 (HC-015, HC-038).
  - D26: 0.
  - D27: 0.
  - D28: 3 (AMP-38, HC-018, HC-027).
- **Otros cambios respecto de `v53`:** 1 (AMP-49, D20→D17). Ningún cambio de territorio; ninguna subfunción venía informada.
- **Sin `v53` (36 registros):** asignados desde cero; 4 quedaron en D28 (G3.2-PA01, G6.2-PA01, M3.2-PA01, M3.2-PA03).
- **Horizontes:** H01 25 · H02 30 · H03 25 · H04 9 · indeterminado 4.
- **MCCS:** DO 67 · OS 19 · NX 5 · MM 2.

**Casos dudosos**

1. **AMP-37** (misma duda en HC-032): conservé D22, pero el agente es el objeto probado y la IA como instrumento de evaluación es D22; la disciplina de aseguramiento es D28. Alternativas: D28 o D20.
2. **AMP-38:** lo pasé de D22 a D28 porque prueba controles y la IA no es el instrumento. Queda desparejo con AMP-37 si se lee D22 como «pruebas de sistemas autónomos».
3. **AMP-49:** D20→D17 porque el brief pone la cadena de suministro de software y de IA en D17. El AI BOM también es inventario de activos de IA, que va en D20.
4. **AMP-48:** conservé D16 por el foco en alternativas y modo manual. El D17 ajustado explicita la cadena de suministro de software y de IA (componentes, modelos, conectores) y el riesgo de concentración.
5. **AMP-51:** conservé D10. Según el brief, inventario de activos, configuración segura y postura van en D13 (los activos de datos en D06 y los de IA en D20).
6. **HC-018:** D14→D28 porque la tesis es sostener afirmaciones de efectividad. El título empieza por observabilidad, que es D14.
7. **HC-038:** D05→D25 con D28 secundario. Podría ser D28 primario si el aseguramiento es el objeto y no la arquitectura Zero Trust.
8. **HC-012:** conservé D20, aunque el texto trata assurance, evidencia, ética y supervisión. Alternativas: D28 o D01 con T07.
9. **M3.1-PA02:** puse D09 porque el texto desarrolla la instancia de correo, y si el objeto es el control de un pilar concreto (identidad, red, datos, nube), queda en el dominio del pilar y D25 puede ir como secundario. El título generaliza a cinco instancias, lo que apuntaría a D25.
10. **M4.1-PA01:** puse D14 con DE02. Alternativas: D04 (el modelo operativo como objeto de gestión), D09 (instancia de Defender for Office 365) y RS01 como subfunción.

## Lote 5

**Lote 5: cierre**

El validador responde `LOTE 5: OK (93 registros válidos)` y la salida está en `salida_5.jsonl`.

- **Registros:** 93 (86 con `v53` y 7 PA sin `v53`).
- **Cambios de dominio primario:**
  - D25: 0.
  - D26: 2 (APC-042, APC-043).
  - D27: 0.
  - D28: 10 (APC-036, 045, 065, 088, 126, 163, 166, 167, 169, 170).
- **Otros cambios respecto de `v53`:** 0; no cambió ningún territorio ni subfunción vigente.
- **Horizontes:** H01 29, H02 36, H03 24, H04 3, indeterminado 1.
- **MCCS:** DO 59, OS 23, NX 9, MM 2.
- **Confianza:** alta 74, media 18, baja 1.

**Casos dudosos**

1. **M6.2-PA03** (baja): el objeto es la portabilidad del programa de formación. Propuse T07/D17/GV09; también caben T05/D25/PR03 o D20.
2. **M6.2-PA01:** D01 (decisión de gobierno) frente a D17 (responsabilidad compartida con la plataforma) o D20.
3. **M5.2-PA02:** D20 frente a D11, y RC04 frente a PR04. M6.2-PA02 comparte la duda D20 frente a D11.
4. **M6.1-PA01:** territorio T06 (operación del SOC) frente a T04 (continuidad).
5. **APC-036:** indicadores de un pilar movidos a D28, porque la regla solo deja fuera la obligación (D03), el riesgo (D02) y la IA como instrumento (D22). Apliqué el mismo criterio en APC-045, 065, 126 y 170; si preferís el dominio vigente, se revierten en bloque.
6. **APC-163:** la evaluación previa a producción pasó a D28. APC-164 (deriva) y APC-165 (reevaluación) quedaron en D20 con D28 secundario.
7. **APC-088:** D28 por analogía con el ejemplo del brief, que lleva la auditoría interna a D28 con D02 secundario; la alternativa es D02.
8. **APC-025:** quedó en D04 con D25 secundario; la alternativa es D25 por «arquitectura objetivo».
9. **APC-122:** la lista de materiales de IA quedó en D20, aunque el ajuste de alcance pone los activos de IA en D20 y la cadena de suministro de IA en D17. Duda parecida en APC-132: D05 frente a D26.
10. **APC-168:** quedó en D03 con D28 secundario; las alternativas son D28 o D01. APC-140 y APC-100 también se conservaron con confianza media.

## Lote 6

**LOTE 6: OK (93 registros válidos)**. La salida está en `salida_6.jsonl`, con los mismos ids y el mismo orden que la entrada.

- **Registros:** 93 (70 APC, 23 APA).
- **Cambios de dominio primario hacia los nuevos:** D25: 0 · D26: 1 · D27: 0 · D28: 5.
  - D26: APC-215, desde D06.
  - D28: APC-188, APC-235, APC-287 y APA-039 desde D03, porque D03 se delimita a las obligaciones y su conformidad, y la evidencia de eficacia, las pruebas y la medición pasan a D28; APA-014 desde D20.
- **Otros cambios respecto de `v53`:** 0. No cambié ningún territorio, ninguna subfunción ni ningún otro dominio.
- **Horizontes:** H01 28 · H02 41 · H03 19 · H04 2 · indeterminado 3.
- **MCCS:** DO 60 · OS 15 · NX 14 · MM 4.
- **Confianza:** alta 79 · media 14 · baja 0.

Dos criterios que apliqué en todo el lote y conviene que el curador conozca:
- D28 quedó como secundario en 18 registros donde la medición es un medio y no el objeto, por analogía con la regla «Si el objeto es el riesgo y la métrica es un medio, queda en D02».
- Agregué T07 como territorio secundario en 38 registros cuyo objeto es la IA o los agentes, para conservar el territorio vigente como primario.

**Casos dudosos**
1. **APA-014** — pasé D20→D28: el objeto es el mapa de aseguramiento, pero también es un catálogo de controles de IA.
2. **APA-045** — conservé D06 (D28 secundario), aunque es paralelo a APC-188, que sí pasó a D28.
3. **APC-251** — conservé D13 (D28 secundario): verificar salvaguardas activo por activo con evidencia roza la evaluación de controles.
4. **APA-008** — conservé D03 (D28 secundario): la mitad es comparación con pares y la otra mitad brecha regulatoria.
5. **APC-192** — conservé D21: agentes de seguridad tratados como identidades privilegiadas admite D05 o D20.
6. **APC-185** — conservé D10: la matriz de responsabilidad compartida de IA admite D17 o D20.
7. **APC-277** — conservé T03/D04: el saneamiento de pilotos de IA admite D20 o D13.
8. **APA-031** — conservé D09/PR03 aunque la tesis dice que no es solo el correo; APA-024, de tema muy cercano, está en D24.
9. **APA-035 / APC-196** — mismo tema con dominio vigente distinto (D21 y D04); conservé ambos.
10. **APC-216 / APC-256** — puse H01 (los fundamentos no cambian con la IA) frente a H02; conservé T04.

## Lote 7

**LOTE 7: OK** — 93 registros en `salida_7.jsonl`, mismos ids y orden; el validador responde «LOTE 7: OK (93 registros válidos)».

**Cambios de dominio primario hacia dominios nuevos (10)**
- D25: 1 (APA-047)
- D26: 1 (APA-116)
- D27: 0
- D28: 8 (APA-077, 080, 082, 117, 136, 175, 188, 191)

**Otros cambios respecto de v53 (4)**, todos de dominio y por el ajuste de alcance que lleva gobierno, riesgo y cumplimiento de la IA a D01, D02 o D03:
- APA-049, APA-091 y APN-04: D20→D01.
- APA-090: D20→D02.

No cambié ningún territorio ni subfunción.

**Horizontes:** H01 34 · H02 30 · H03 29 · H04 0 · indeterminado 0.
**MCCS:** DO 62 · OS 16 · NX 11 · MM 4.
**Confianza:** alta 70 · media 23 · baja 0.

**Casos dudosos**
1. **APA-091** (mismo criterio en APN-04 y APA-049): lo pasé a D01 como política de uso de IA; si se lee como seguridad del uso de IA, vuelve a D20.
2. **APA-090**: D20→D02 por transferencia del riesgo de IA, pero el territorio vigente es T04 y no T07.
3. **APA-113**: conservé D20; «aseguramiento razonable» con T08/GV08 también admite D28.
4. **APA-175**: D02→D28 por analogía con el ejemplo del brief, que lleva a D28 la revisión independiente de la gestión de riesgos con D02 secundario; puede quedar en D02.
5. **APA-080**: D13→D28 porque los hallazgos son de auditoría; además dudé entre NX (aprendizaje) y DO.
6. **APA-117**: D04→D28 (evaluación de controles); la lectura vigente de priorización de inversión sigue siendo posible.
7. **APA-084**: conservé D05, aunque el objeto es la exactitud de la cobertura declarada a la aseguradora (D28 o D02).
8. **APA-182**: conservé D11; el inventario de activos va en D13, así que podría moverse.
9. **APA-047**: D05→D25 (Zero Trust como estrategia), aunque la fricción medida es de acceso.
10. **APA-158** frente a **APA-130**: temas gemelos (cobertura de controles sobre IA) quedan en D20 y D01 por conservar v53.

Criterio transversal a revisar: usé H03 para gobierno y seguridad propios de IA y agentes, y H02 cuando una disciplina clásica se extiende a la IA. Si el curador traza esa frontera en otro lugar, cambia buena parte de los 59 registros H02/H03.

## Lote 8

**Lote 8 — cierre.** `LOTE 8: OK`, 88 registros en `salida_8.jsonl`.

- **Cambios de dominio primario:** D25: 2 (APF-21, APF-22) · D26: 1 (APN-22) · D27: 0 · D28: 9 (APN-14, APS-11, APS-13, APS-14, APS-15, APS-16, APS-20, APS-28, APF-12).
- **Otros cambios respecto de v53:** 0; territorio y subfunción se conservaron en los 88.
- **Horizontes:** H02 73 · H03 12 · indeterminado 3 (APN-25, APF-17, APF-18) · H01 0 · H04 0.
- **MCCS:** DO 70 · OS 12 · NX 5 · MM 1.
- **Confianza:** alta 73 · media 15.

**Casos dudosos**
1. APN-22: pasé a D26 porque D26 incluye la gestión de claves y secretos; la alternativa es conservar D06 (fuga por prompts).
2. APS-13: D28 frente a D22, porque si la IA es el instrumento de la prueba, queda en D22; dejé D22 como secundario.
3. APS-15: misma duda que APS-13.
4. APS-28: pasé a D28 por tratar el ejercicio como prueba técnica; la alternativa es conservar D14.
5. APN-14: D28 (evidencia de la revisión humana) frente a conservar D20.
6. APF-12: D28 (paquete de evidencia para auditoría) frente a conservar D05.
7. APF-22: D25 frente a conservar D20, por ser arquitectura específica de IA.
8. APF-02: conservé D04, aunque la medición de madurez figura entre los objetos de D28.
9. APN-43: conservé D06/PR02; el objeto se parece más a un compromiso contractual (D03/GV06).
10. APF-16: conservé D06/PR02; la garantía al cliente con evidencia admite D28.

## Lote 12 · muestra de control

**Lote 12 — 48 registros** (validador: `LOTE 12: OK`)

**Cambios de dominio primario hacia dominios nuevos**
- D25: 1 (M3.1-K10)
- D26: 1 (APN-22)
- D27: 0
- D28: 3 (G6.2-K05, APA-175, APS-13)

**Otros cambios respecto de `v53`:** 2, ambos de dominio (AMP-22 D20→D02 y APA-049 D20→D01). No cambié ningún territorio ni subfunción informados.

**Horizontes:** H01 24 · H02 17 · H03 5 · H04 1 · indeterminado 1

**Pilares MCCS:** DO 32 · OS 14 · MM 1 · NX 1

**Casos dudosos**
1. **G6.2-K05** — Pasé D01→D28 porque las métricas de gobierno miden eficacia. Por analogía con el ejemplo del brief («Métricas de Apetito» queda en D02 con D28 secundario) podría quedar en D01.
2. **M3.2-K10 (POA&M)** — Conservé D13 con D28 secundario, aunque el territorio es T08 y la tesis pide evidencia de cierre. También dudo entre RC04 (elegida) e ID05.
3. **AMP-22** — D20→D02 no es dominio nuevo: apliqué que gobierno, riesgo y cumplimiento de la IA van en D01, D02 o D03 con territorio T07. Misma decisión en APA-049 (D20→D01); si había que conservar D20, se revierten ambos.
4. **APA-175** — D02→D28 porque el objeto es la validación independiente del modelo. La alternativa es D02, por ser cuantificación del riesgo.
5. **APS-13** — D03→D28 con D22 secundario. La alternativa es D22 primario, porque si la IA es el instrumento de la prueba, queda en D22.
6. **APN-22** — D06→D26 porque el catálogo de D26 incluye gestión de claves y secretos. La alternativa es D06 si se lee como fuga de datos por prompts.
7. **APC-100** — Conservé T03/D04/GV01 aunque título y producto son apetito de riesgo de IA. Dejé T04, T07, D02 y GV04 como secundarios.
8. **APC-095** — H04 por la integración de la seguridad en ingeniería y producto. La alternativa es H01.
9. **HC-002** — No lo marqué H04 porque no alcanza con que sea un híbrido: la tesis tiene que ser la convergencia; quedó en H01 y D02 con D25 secundario. HC-006 quedó en indeterminado y D04 con D28 secundario.
10. **AMP-45** — H02 (forense existente extendida a agentes) frente a H03. La misma frontera afecta a APC-134 (H02) y a AMP-22, G4.2-PA01 y APA-049 (H03).

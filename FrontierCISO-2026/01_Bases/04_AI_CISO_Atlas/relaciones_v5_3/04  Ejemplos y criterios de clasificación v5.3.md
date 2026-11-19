# 04 | Ejemplos y criterios de clasificación v5.3

> **AI CISO Atlas Curator | Knowledge Pack 5.3 | Propuesta editorial controlada**  
> No equivale a una certificación, homologación o taxonomía oficial de ISACA, CSA o NIST.  
> **Precedencia:** 01 Taxonomía > 02 Relaciones > 03 Currículo > 04 Ejemplos. Para unidades y cargas GM-24, el documento 03 es la fuente canónica.  
> Los códigos de subfunciones son del Atlas, no códigos oficiales de categorías NIST CSF.

## Uso

Ejemplos **ilustrativos, no un conjunto gold-standard validado**. Cada clasificación depende de la tesis concreta del texto, no del título. El agente debe justificar por qué cada etiqueta y unidad aplica.

| Idea | X | Y | Z | Subfunción | H | GM-24 principal | Observación |
|---|---|---|---|---|---|---|---|
| MFA y privilegios | T05 | D05 | PR | PR01 | H01 | M2.2 | Protección tradicional; IA no central. |
| Privacidad en RAG | T07 | D07 | PR | PR02 | H02 | M2.1 | Privacidad principal, Data Security secundario; G3.1 secundaria. |
| Agente de IA que investiga alertas | T06 | D21 | DE | DE02 | H02 | M4.1 | IA instrumento defensivo, no necesariamente objeto protegido. |
| IA para descubrir vulnerabilidades | T05 | D22 | ID | ID03 | H02 | M4.2 | D22 evaluación, D13 secundario. |
| IA para generar reglas de detección | T05 | D23 | PR | PR04 | H02 | M3.2 | Construcción de controles; D14 secundario. |
| Phishing con IA por adversarios | T04 | D12 | ID | ID03 | H02 | M4.2 | Rol ADVERSARIAL_USE. |
| Gobierno de autoridad de agentes | T07 | D20 | GV | GV02 | H03 | G4.1 | M2.2 y G5.2 secundarias. |
| Plan de recuperación industrial | T04 | D18 | RC | RC02 | H01 | M6.1 | OT y continuidad; D16 secundario. |
| Board memo sobre inversiones | T03 | D04 | GV | GV05 | H01 | G1.2 | G6.1 secundario; no confundir con T08. |
| Prueba independiente de controles | T08 | D03 | GV | GV08 | H01 | G3.2 | Assurance, no garantía absoluta de cumplimiento. |
| Liderazgo y sesgos cognitivos | T01 | D24 | GV | GV10 | H02 | G6.2 | Z puede ser undetermined si no se formula resultado de gobierno. |
| Agentes con IAM inmaduro | T04 | D20 | GV | GV04 | H03 | G5.2 | CAT02, INH03, HOM01; contexto hipotético. |
| Texto genérico sobre el futuro de IA | undetermined | undetermined | undetermined | undetermined | undetermined | undetermined | No forzar categorías ni unidades. |

## Contrastes decisivos

- **T03/T04/T08:** decidir inversión / evaluar exposición / demostrar evidencia.
- **D06/D07:** confidencialidad de datos / legitimidad del tratamiento personal.
- **D20/D21/D22/D23:** proteger IA / IA para defensa / IA para testing / IA para ingeniería.
- **ID/DE:** conocer exposición / detectar actividad adversa operacional.
- **RS/RC:** contener incidente / restaurar y validar servicio.
- **H ≠ madurez:** H03 no demuestra readiness alta.
- **Gobierno ≠ Gestión:** el ensayo puede sustentar ambos pilares, pero el objetivo formativo define su ubicación primaria.

## Casos evolutivos hipotéticos

### Banco con presión de adoptar agentes

- X T04/T07; Y D20/D05; Z GV/PR; H03.
- Catalizadores posibles CAT02/CAT10; inhibidores posibles INH03/INH05; homeostasis HOM01/HOM09.
- Trayectoria condicional: solo lectura → acciones reversibles acotadas → autonomía bajo controles y evidencia.
- Unidad GM-24: G5.2 primaria si la tesis es aceptación del riesgo; M2.2 primaria si la tesis es arquitectura IAM.
- **No asumir** regulación, país ni madurez concreta.

### Planta industrial con infraestructura heredada

- X T04; Y D18/D16; Z RC; H02 si estudia transición.
- Inhibidores INH01/INH09; homeostasis HOM02/HOM06/HOM07.
- Trayectoria: inventario → segmentación → telemetría pasiva → pruebas de recuperación antes de automatizar respuesta.
- Unidad M6.1 principal; M6.2 secundaria.

### SOC con IA asistida

- X T06; Y D21; Z DE; H02.
- Catalizadores CAT01/CAT06; homeostasis HOM04/HOM09.
- Transición: copiloto → enriquecimiento semiautomático → acciones limitadas preautorizadas con rollback.
- Unidad M4.1 principal; M5.2 secundaria.

## Plantilla de salida integrada

1. **Síntesis:** tesis, problema, audiencia, resultado esperado.
2. **Estructural:** X/Y/Z principal y secundarios, subfunción editorial, rol IA, justificaciones.
3. **Evolutivo (si procede):** H, fuerzas, contexto, transición, incertidumbre.
4. **TheNextCISO:** unidad principal, hasta tres secundarias, pilar, eje, competencia observable, modalidad y evaluación.
5. **Grafo:** conceptos y relaciones tipadas propuestas; ninguna escritura automática.
6. **Control de calidad:** confianza cualitativa, versiones, fuentes, ambigüedades y revisión humana.

## Pruebas mínimas

- Seguridad tradicional sin IA.
- Seguridad de IA como activo.
- IA para defensa, assessment e ingeniería.
- Ataques adversariales con IA.
- Privacy vs Data Security.
- OT vs IoT.
- Strategy vs Risk vs Trust.
- Evolución con contexto explícito y sin contexto.
- Ensayos multidominio.
- Textos demasiado vagos para clasificar.

**No inventar una categoría o una unidad por cada concepto nuevo.** Si la taxonomía no alcanza, registrar `taxonomy_gap_proposal` para revisión humana.

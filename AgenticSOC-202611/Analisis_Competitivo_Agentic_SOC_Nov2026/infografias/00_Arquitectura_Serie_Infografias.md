# Arquitectura y Auditoría de la Serie de 7 Infografías — Agentic SOC Noviembre 2026

**Fecha de corte documental y visual:** 25 de noviembre de 2026  
**Universo cubierto:** 12 fabricantes enterprise + 6 especialistas pure-play · 10 dimensiones ponderadas · 40 fuentes primarias verificadas  
**Formatos entregados:** `.svg` vectorial editable (`1920×1200`), `.png` 4K Retina (`3840×2400`) y `.jpg` de alta densidad (`3840×2400`) — **21 archivos gráficos** + visor interactivo HTML.

---

## 1. Criterio de Partición en 7 Piezas (Control de Saturación y Carga Cognitiva)

Siguiendo la metodología de planificación y auditoría visual (`visual-series-planning-and-audit`), condensar 12 fabricantes, 10 dimensiones, 56 capacidades GA vs. Preview, arquitectura Microsoft de 6 planos, coexistencia SIEM/SOAR, AppSec agéntico y gobierno de agentes en 1 o 2 láminas produciría **saturación severa** y pérdida de legibilidad.

Por ello, el corpus se particionó en **7 infografías independientes pero cohesivas** (gramática visual común, cabecera/pie trazables y codificación semántica doble color + etiqueta textual):

| Código | Archivo Base | Pregunta Rectora | Arquetipo Visual | Control de Densidad |
|---|---|---|---|---|
| **IG-01** | `IG-01_Ranking_Global_12_Fabricantes` | ¿Quién lidera el mercado Agentic SOC Enterprise y cuál es la distancia real entre escalones? | Ranking cuantitativo (0–100) + 3 bloques analíticos laterales | 4 KPIs + 12 barras horizontales + línea de media (77.8) + resumen de 6 pure-plays |
| **IG-02** | `IG-02_Arquitectura_Microsoft_6_Planos` | ¿Cómo encajan ISOC, Perception, Security Copilot (+18 agentes), Logic Apps, MDASH, GHAS y Agent 365 sin solaparse? | Arquitectura en 6 capas apiladas + reglas explícitas de desambiguación | 6 planos horizontales diferenciados + 5 reglas anti-confusión a la derecha |
| **IG-03** | `IG-03_Mapa_Calor_10_Dimensiones` | ¿Dónde están las fortalezas y los puntos ciegos exactos de los 12 proveedores en cada dominio técnico? | Matriz de calor cuantitativa `12 × 10` con doble codificación accesible | Puntaje `1.0–5.0` + etiqueta textual (`ALTO+`, `FUERTE`, `MEDIO`, `BRECHA`) + 3 hallazgos |
| **IG-04** | `IG-04_Realidad_GA_vs_Preview_Nov2026` | ¿Qué está realmente en producción (GA) hoy frente a lo anunciado en Preview, Gated o M&A pendiente? | Auditoría comparativa GA vs. Preview en dos carriles por fabricante | KPI `57.1% GA vs 42.9% Preview` + desglose exacto en los Top 6 + síntesis #7–#12 |
| **IG-05** | `IG-05_SOAR_LogicApps_y_Coexistencia_SIEM` | ¿Cómo posicionar Azure Logic Apps frente a XSOAR, Fusion, FortiSOAR y Torq en un SOC híbrido con Splunk/QRadar? | Patrón arquitectónico de plano único + tabla comparativa de motores SOAR | Flujo de 3 carriles (coexistencia multi-anual + beneficio E5/P2) + matriz de 6 motores |
| **IG-06** | `IG-06_AppSec_Agentico_MDASH_CodeMender_Continuum` | ¿Qué diferencia al nuevo AppSec agéntico con PoC verificable del SAST tradicional? | Pipeline de 5 etapas Código-a-SOC + comparativa de 6 plataformas | Ciclo `Descubrimiento -> Sandbox PoC -> Parche PR -> Riesgo vivo -> Regla SOC` |
| **IG-07** | `IG-07_Gobierno_y_Contencion_Agentes_IA` | Cuando un agente IA se desvía o es comprometido, ¿quién puede revocar su identidad y contener sus datos hoy? | Pila de 5 capas de intervención + auditoría de *Kill Switches* del mercado | Contraste `Corte de Gateway LLM` vs. `Revocación Full-Stack (Identidad + Endpoint + Datos)` |

---

## 2. Auditoría de Calidad Visual y Semiótica

1. **Accesibilidad cromática (No solo color):** Todas las celdas del mapa de calor (`IG-03`) y estados de madurez (`IG-04`, `IG-06`, `IG-07`) combinan color de alto contraste con etiquetas explícitas (`[GA]`, `[PREV]`, `ALTO+`, `FUERTE`, `MEDIO`, `BRECHA`).
2. **Cero solapamientos y márgenes verificados:** Todas las piezas fueron renderizadas con motor Chromium/Edge a `3840×2400` px e inspeccionadas visualmente para verificar ausencia de recortes, colisiones tipográficas o desbordes de contenedores.
3. **Fidelidad documental estricta:** Cada puntaje, fecha y estado (`GA`, `Public Preview`, `Early Access`, `Q4 FY27`) refleja exactamente las matrices verificadas en `Matriz_Competitiva_Agentic_SOC_12_Fabricantes_Nov2026.xlsx` y `Catalogo_Microsoft_Agentic_Security_Ignite2026.xlsx`.

---

## 3. Estructura de Carpetas Entregadas

- `svg\` — 7 archivos `.svg` vectoriales nativos (`1920×1200`), 100% editables en Illustrator, Figma, Inkscape, Visio o PowerPoint.
- `png\` — 7 archivos `.png` (`3840×2400`, 4K sin pérdida) listos para presentaciones ejecutivas y documentación técnica.
- `jpg\` — 7 archivos `.jpg` (`3840×2400`, alta calidad editorial) livianos para distribución por correo, portales o mensajería.
- `Galeria_Serie_7_Infografias_Nov2026.html` — Visor web autocontenido con acceso directo a las 3 versiones de cada lámina.

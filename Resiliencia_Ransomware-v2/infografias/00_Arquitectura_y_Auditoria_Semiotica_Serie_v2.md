# Arquitectura y Auditoría Semiótica de la Serie de Infografías — Resiliencia ante Ransomware v2.0

**Paquete de origen:** `PKG-RANSOM` (`Resiliencia_Ransomware-v2`, edición integrada v2.0 · 12 de noviembre de 2026)  
**Correlación canónica preservada:** `PKG-CISO365` (v1.0) · `PKG-KPI-OKR` (v1.2) · `PKG-NINJA` (`NT-01..NT-15`, v2026-11-08)  
**Formatos generados:** `.svg` vectorial editable (`1920×1200`), `.png` 4K Retina (`3840×2400`) y `.jpg` de alta densidad (`3840×2400`) — **24 archivos gráficos (8 piezas × 3 formatos)** + visor HTML local.

---

## 1. Justificación de Cantidad (8 Piezas) y Control de Saturación

El kit `Resiliencia_Ransomware-v2` articula **15 guías operativas**, **3 libros Excel**, **7 fases anuales (`F0..F6`)**, **21 controles (`CT-01..21`)**, **13 detecciones (`DE-01..13`)**, **7 playbooks (`PB-01..07`)**, **9 roles (`ROL-01..09`)**, **8 formularios fuera de banda (`F1..F8`)**, **3 ensayos anuales (`E1..E3`)** y **12 capas Full Microsoft (`MS-CAP-01..12`)**.

Conforme a las reglas de `visual-series-planning-and-audit`:
- **Consecuencia de menos piezas (ej. 3–4 láminas):** colapso de tipografía bajo `10px`, mezcla indebida de catálogos no-MECE con flujos secuenciales y pérdida de condiciones críticas de seguridad (límites de revocación `MS-10`, no apagar por rutina `MS-05`, modo sin IA `K56`).
- **Consecuencia de más piezas (ej. >12 láminas):** fragmentación excesiva del hilo operativo entre detección, contención, custodia y recuperación.
- **Decisión óptima:** **8 infografías (`RR-01` a `RR-08`)** organizadas en progresión **pedagógica y decisional** (Gobierno y Fases → Preparación/Controles → Procesos de Crisis → Validación y Operación Sostenida), donde cada pieza mantiene lectura autónoma y densidad controlada.

---

## 2. Especificación Estructural de las 8 Piezas

| ID y Prioridad | Archivo Base | Pregunta que Responde | Dimensión Principal | Arquetipo Visual | Qué Preserva y Qué Comprime |
|---|---|---|---|---|---|
| **RR-01 (P1)** | `RR-01_Mapa_Maestro_Ciclo_y_Fases_365` | ¿Cuáles son las fases del ciclo anti-ransomware y cómo se despliegan en los primeros 365 días del CISO? | **Fases e Hitos** (`4 macro-fases`, `3 olas`, `F0..F6` / `H0..H365`) | `flow-diagram` + `timeline-matrix` | Preserva los 7 hitos, controles por fase y trampas habituales; aclara que las 3 olas son prioridad de ejecución (`[MS-01]`), no dependencia técnica universal. |
| **RR-02 (P1)** | `RR-02_Gobierno_Roles_Autoridad_y_Activacion` | ¿Quién tiene autoridad para decidir, quién ejecuta y cómo se coordina una crisis fuera de banda? | **Responsables y Gobierno** (`3 niveles`, `7 roles`, `DD01..DD18`, `6 pasos`) | `modular-grid` + `authority-matrix` | Separa `A` (aprueba) de `R` (ejecuta); preserva que ningún proveedor declara `DD10` y que `DD18` (suspender agente IA) no autoriza desconectar servicios críticos (`DD11`). |
| **RR-03 (P1)** | `RR-03_Catalogo_21_Controles_y_Escala_Evidencia` | ¿Cuáles son las 21 tareas/controles verificables y qué diferencia un control `Implementado` de uno `Probado`? | **Tareas de Preparación** (`CT-01..21` + escala de `5 estados` vs `EV##` y `E1–E5`) | `progression-bar` + `modular-grid` (4 columnas) | Declara explícitamente que las 4 agrupaciones funcionales se refuerzan entre sí (no-MECE) y que todo control exige alcance y denominador conocido. |
| **RR-04 (P1)** | `RR-04_Proceso_Monitoreo_13_Detecciones_y_Triage` | ¿Cómo opera el proceso de monitoreo y triage reproducible ante las 13 señales de ataque (incluida IA y ceguera)? | **Proceso Crítico 1: Detección y Triage** (`6 pasos` + `DE-01..DE-13` + cadencia SOC) | `flow-diagram` + `detection-matrix` | Preserva el doble chequeo de cierre, la independencia entre extorsión (`DE-07/08`) y cifrado (`DE-06`), la alerta por caída de sensor (`DE-11`) y el uso de mediana/p90. |
| **RR-05 (P1)** | `RR-05_Proceso_Contencion_Playbooks_y_Revocacion` | ¿Cómo contener e invalidar el acceso adversario sin destruir evidencia ni asumir cierre prematuro? | **Proceso Crítico 2: Contención y Repudio** (`5 invariantes`, `6 pasos`, `PB-01..07`, `6 superficies`) | `flow-diagram` + `playbook-cards` + `surface-grid` | Preserva los 7 playbooks (incluido `PB-07` para agentes/MCP) y el riesgo residual exacto en AD, Entra (`CAE`/tokens), cookies SaaS, APIs, equipos offline y RAG. |
| **RR-06 (P1)** | `RR-06_Proceso_Forense_Continuidad_y_Recuperacion` | ¿Cómo preservar cadena de custodia legal mientras se recupera en zona limpia dentro de RTO/RPO? | **Proceso Crítico 3: Forense y Recuperación** (`6 pasos custodia` + `7 pasos recuperación` + `4 ámbitos MS`) | `dual-track-flow` + `recovery-matrix` | Separa hechos/inferencias/hipótesis/lagunas, detalla el orden de restitución de cimientos y exige modo degradado sin IA probado (`K56`). |
| **RR-07 (P2)** | `RR-07_Proceso_Comunicaciones_Pruebas_y_Formularios` | ¿Cómo controlar comunicaciones externas por audiencia y validar competencias reales sin pistas (`E1–E3`)? | **Proceso Crítico 4: Comunicaciones, Ensayos y Formularios** (`8 audiencias`, `E1–E3`, `F1–F8`) | `flow-diagram` + `modular-grid` | Evita suponer plazos legales universales ("72h"), exige demostración individual de titular y suplente sin ayuda y documenta las herramientas fuera de banda. |
| **RR-08 (P2)** | `RR-08_Arquitectura_Full_Microsoft_y_Dotacion_Roles` | ¿Cómo aterriza la operación diaria en las 12 capas Full Microsoft, los 9 roles técnicos y los 6 sectores? | **Operación Tecnológica y Responsables Técnicos** (`MS-CAP-01..12`, `ROL-01..09`, `6 sectores`, `Q1–Q6`) | `layered-matrix` + `role-sizing-grid` | Mantiene los límites críticos por capa (`Resource Guard` separado, `SCU` gobernadas, `M365 Backup` vs `Files Restore`) y las `1.572 h / 3.144 h` de formación Ninja. |

---

## 3. Diccionario Semiótico Común y Accesibilidad

1. **Flechas direccionales (`→`):** reservadas exclusivamente a secuencias operativas o temporales demostradas en las guías (`Triage 1→6`, `Bucle PB 1→6`, `Custodia 1→6`, `Recuperación 1→7`, `Comunicaciones 1→5`, `Hitos F0→F6`). Nunca se usan flechas para simples listas o catálogos.
2. **Doble codificación accesible (Color + Etiqueta + Trazo):**
   - `[BASE / VERIFICADO]` — Verde (`#DCFCE7` / `#14532D`), borde continuo: condición de aceptación comprobada o capacidad base.
   - `[DECISIÓN / GATE]` — Azul (`#DBEAFE` / `#1E3A8A`), borde continuo: punto de autorización formal (`CI`, `Negocio`, `Legal`, `DD##`).
   - `[ATENCIÓN / CONDICIÓN]` — Ámbar (`#FEF9C3` / `#713F12`), borde continuo: precondición operativa, modo degradado o validación pendiente.
   - `[LÍMITE / PROHIBIDO]` — Rojo suave (`#FEE2E2` / `#7F1D1D`), **borde discontinuo (`4,2`)**: invariante de seguridad, trampa habitual o riesgo residual no cubierto automáticamente.
3. **Portabilidad:** todos los artefactos de esta carpeta carecen de rutas absolutas locales, datos personales o secretos, cumpliendo las reglas de publicación del repositorio `Resiliencia_Ransomware-v2`.

---

## 4. Estructura del Subdirectorio

- `svg/` — 8 archivos `.svg` vectoriales (`1920×1200`).
- `png/` — 8 archivos `.png` 4K (`3840×2400`).
- `jpg/` — 8 archivos `.jpg` 4K (`3840×2400`).
- `Galeria_Serie_Infografias_Resiliencia_Ransomware_v2.html` — Visor local portable con acceso directo a los 3 formatos de cada pieza.
- `generar_infografias_v2.py` — Script generador reproducible en Python (sin rutas fijas de usuario).

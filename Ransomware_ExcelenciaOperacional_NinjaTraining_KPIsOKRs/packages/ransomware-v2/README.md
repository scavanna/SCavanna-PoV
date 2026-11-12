# Programa operativo de resiliencia ante ransomware · Edición integrada v2.0

**Versión:** 2.0, 12 de noviembre de 2026. **Estado:** paquete portable de **23 archivos** (plantilla operativa y estratégica integrada; no constituye un assessment ni certifica controles de una organización). **Objetivo:** detectar actividad adversaria antes del impacto, interrumpirla, preservar evidencia y restablecer operaciones prioritarias dentro de RTO/RPO aprobados, **vinculando cada acción con las prioridades del negocio, el plan de primeros 365 días del CISO, el sistema de KPIs/OKRs, la operación sobre un stack Full Microsoft y las rutas de entrenamiento de Ninja Training 2026**.

## Qué incorpora la versión 2.0 frente a v1.1

1. **Vinculación por nombres canónicos portables (sin rutas rígidas):** todas las referencias apuntan a los nombres canónicos e identificadores estables de los otros tres artefactos (`PKG-CISO365`, `PKG-KPI-OKR` y `PKG-NINJA`), permitiendo mover o publicar las carpetas en OneDrive, SharePoint o GitHub Pages sin romper la trazabilidad.
2. **Contextualización por prioridades organizacionales y sectoriales:** cruce directo con los **7 perfiles sectoriales** (`FIN`, `GOB`, `ELE`, `OYG`, `IND`, `LOG`, `ORG`), las **6 preguntas del Directorio (`Q1`–`Q6`)**, los **derechos de decisión (`DD01`–`DD22`)** y la secuencia de instalación en **7 fases e hitos (`F0/H0` a `F6/H365`)**.
3. **Arquitectura de operación para un cliente Full Microsoft (`MS-CAP-01` a `MS-CAP-12`):** qué tecnologías operar en prevención, identidad híbrida/nube, XDR/SIEM/SOAR, SOC asistido/agéntico, protección contra exfiltración, custodia forense, respaldo inmutable (`Azure Backup` + `Resource Guard` + `Microsoft 365 Backup` + `Azure Site Recovery`) y gobierno de IA/agentes (`CT-21`, `DE-13`, `PB-07`).
4. **Plan de recursos y entrenamiento sobre `Ninja_Training_Seguridad_Microsoft_2026`:** asignación exacta de los **15 programas (`NT-01` a `NT-15`)**, códigos de módulos y carga horaria en tres olas para **titulares y suplentes** de los 9 roles operativos (`ROL-01` a `ROL-09`), diferenciando laboratorio (`[LAB]`) y práctica controlada en producción (`[SOLO-PRODUCCION]`).

## Registro resumido de paquetes canónicos vinculados

| Código | Artefacto canónico de referencia | Elementos clave vinculados |
|---|---|---|
| `PKG-RANSOM` | Programa Operativo de Resiliencia ante Ransomware (`v2.0`) | `CT-01..21`, `DE-01..13`, `PB-01..07`, `SRC-01..09`, `T-01..04`, `E1..E3`, `ROL-01..09`, `MS-CAP-01..12` |
| `PKG-CISO365` | `AI_CISO_Atlas_CISO365_Plan_y_Ciclo_Anual_v1.0.xlsx`, `Evaluacion_y_Entrevistas_v1.0.xlsx`, `Tablero_Rendicion_de_Cuentas_v1.0.xlsx`, serie `00..08_v1.0.md` y `Catalogo_v1.0.json` | Fases `F0..F6`, hitos `H0..H365`, recepción `RC01..32`, actividades `ACT-001..130`, rituales `R01..54`, decisiones `DD01..22`, prácticas `EV01..51`, servicios `S01..18`, preguntas `Q1..Q6` |
| `PKG-KPI-OKR` | `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_v1.0_2026-11-09.xlsx` (base) y `v1.2_2026-11-10.xlsx` (integrado CISO 365) + `Guia` y `Catalogo` JSON | `K01..K64` (8 territorios `T01..T08`), `KSG01..KSG06`, estadios `E1..E5` (meta `E3` año 1, `E4` año 2), perfiles sectoriales y OKR `A1-O1..O6` / régimen |
| `PKG-NINJA` | `Ninja_Training_Seguridad_Microsoft_2026` (`README.md`, `index.html`, `MANIFIESTO_VERSION.json`, `01_Sentinel` a `15_Seguridad_de_agentes_de_IA_en_Foundry` y anexos de laboratorio) | 15 programas (`NT-01..NT-15`), 387 módulos (~2.000 h), 2.165 ejercicios etiquetados `[LAB]`, `[LAB-PARCIAL]` y `[SOLO-PRODUCCION]` |

## Jerarquía de uso del paquete (23 archivos)

| Nivel | Documento o herramienta | Decisión o producto esperado |
|---|---|---|
| Estrategia y mapeo | [13-Mapeo-canonico-y-prioridades.md](13-Mapeo-canonico-y-prioridades.md), `03-Correlacion-Prioridades-FullMS-Ninja.xlsx`, `Mapa-de-correlacion-y-prioridades.html`, `Catalogo-correlacion-v2.json` | Priorización por sector y fase CISO 365 (`H0..H365`), cruce 360° con KPIs/OKRs y resolución de nombres canónicos. |
| Stack y recursos | [14-Operacion-Full-Microsoft.md](14-Operacion-Full-Microsoft.md), [15-Plan-de-entrenamiento-y-recursos.md](15-Plan-de-entrenamiento-y-recursos.md) | Diseño operativo sobre cliente Full Microsoft (`MS-CAP-01..12`), dotación de titulares/suplentes y plan de horas Ninja por ola. |
| 0 · Gobierno | [01-Gobierno.md](01-Gobierno.md) | Mandato, roles, suplentes, derechos de decisión (`DD01..DD22`), severidad y autoridad de emergencia. |
| 1 · Diagnóstico | [02-Evaluaciones.md](02-Evaluaciones.md) y `01-Evaluacion-y-controles.xlsx` | Recepción (`RC##`), línea base (`H60`), evaluación trimestral, BIA, brechas y cruce con `EV01..51` y estadios `E1..E5`. |
| 2 · Controles | [03-Controles-y-plan.md](03-Controles-y-plan.md) y `Panel-de-resiliencia.html` | Arquitectura agnóstica, implementación Full Microsoft y criterios verificables de `CT-01` a `CT-21` (incluye IA/agentes). |
| 3 · SOC | [04-Monitoreo-y-triage.md](04-Monitoreo-y-triage.md) y `02-Operacion-y-pruebas.xlsx` | Salud de fuentes `SRC-01..09`, detecciones `DE-01..13` en Sentinel/Defender XDR/Purview, triage y escalamiento. |
| 4 · Contención | [05-Respuesta-y-repudio.md](05-Respuesta-y-repudio.md), [10-Tarjetas-de-respuesta.md](10-Tarjetas-de-respuesta.md), `Consola-de-incidente.html` | Playbooks `PB-01..07`, invalidación de tokens/cookies/agentes, decisiones trazables y reversión controlada. |
| 5 · Forense y DR | [06-Evidencia-y-forense.md](06-Evidencia-y-forense.md), [07-Continuidad-y-recuperacion.md](07-Continuidad-y-recuperacion.md) | Custodia con Purview Audit/eDiscovery, modo degradado (sin TI y sin IA), zona limpia y restauración `E2`. |
| 6 · Crisis y pruebas | [08-Comunicaciones.md](08-Comunicaciones.md), [09-Pruebas-y-metricas.md](09-Pruebas-y-metricas.md) | Notificaciones revisadas por Legal (`DD12/DD13`), ejercicios `E1/E2/E3`, competencias sin pistas y métricas `K##`/`KSG##`. |
| Apoyo | [11-Fuentes-y-cobertura.md](11-Fuentes-y-cobertura.md), [12-Formularios.md](12-Formularios.md) | Trazabilidad documental de los 4 paquetes, límites de lectura y formularios imprimibles fuera de banda. |

## Principios no negociables

- **El impacto de negocio y la seguridad humana mandan sobre el volumen de alertas.** Toda desconexión crítica sigue los umbrales y derechos de decisión acordados (`DD10`, `DD11`, `DD14`, `DD18`).
- **Licencia Full Microsoft ≠ control desplegado ≠ capacidad probada.** Comprar M365 E5, Defender for Cloud, Sentinel o Security Copilot no convierte ningún control `CT-*` en `Probado` ni lleva un KPI a `E3`/`E4` sin cobertura medida y ensayo documentado [MS-09].
- **Sincronización no es respaldo independiente.** Versionado y OneDrive Files Restore ayudan en su alcance; la recuperación empresarial exige copias inmutables/aisladas (`Azure Backup` con inmutabilidad/MUA, `Microsoft 365 Backup`, `AD Forest Recovery`) y pruebas reales contra RTO/RPO (`K28`, `K30`) [MS-02, MS-07, MS-08].
- **Revocar acceso abarca humanos, cargas y agentes de IA.** Bloqueo de cuenta, `Revoke-MgUserSignInSession`, CAE, cookies propias de aplicaciones, service principals y agentes (`Entra Agent ID` / `Agent 365`) tienen latencias y planos distintos (`K34`, `K50`, `K56`) [MS-10].
- **Entrenamiento medido por ejecución sin pistas.** Completar horas Ninja prepara al equipo, pero `Competencias` y `K12`/`K16` exigen que titular y suplente demuestren su rol en ejercicio.
- **Uso seguro de las apps HTML y libros Excel:** los tres HTML funcionan 100 % offline en el navegador, sin telemetría, almacenamiento persistente ni conexión a SIEM/EDR/correo. Exportar archivos JSON/CSV reales únicamente a un repositorio cifrado, etiquetado con MIP y con acceso restringido.

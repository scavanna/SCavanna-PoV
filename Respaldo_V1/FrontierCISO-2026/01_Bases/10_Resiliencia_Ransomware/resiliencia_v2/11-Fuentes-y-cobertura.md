# 11. Fuentes, trazabilidad y límites de cobertura (v2.0 · incluye artefactos canónicos vinculados)

**Fechas de consulta:** 11 y 12 de noviembre de 2026 (UTC). **Naturaleza:** análisis de recomendaciones públicas y lecturas **parciales** de presentaciones internas mediante WorkIQ, no auditoría de un entorno ni certificación de un programa. Se sintetizan las ideas con redacción propia; cada recomendación operativa requiere adaptación, autorización y evidencia local.

## 1. Perfil de las fuentes y calidad

La solicitud está en español y define un **objetivo prescriptivo** (construir un kit operacionalizable), no una constatación de controles presentes. Las páginas de Microsoft, CISA y NIST están en inglés y son guías técnicas/normativas de distinta profundidad; los títulos y productos en inglés dentro del kit no cambian su idioma predominante español. Las presentaciones son una mezcla de material técnico, comercial y de taller: recomendaciones y preguntas **no son hechos observados** en una organización. Se conservaron nombres y números de diapositiva provistos por WorkIQ; no se extrajeron localmente los PPTX sincronizados, ni se inspeccionó manualmente cada diapositiva.

**Cobertura interna verificable:** se enumeraron **68 PPTX, 2.880.928.251 bytes** en `MS Ransomware 2601` (colección canónica OneDrive). Se consultaron seis por WorkIQ Ask; **cuatro** respuestas son atribuibles al archivo exacto (**4/68**) y **dos** presentan discrepancias de versión/identificador (**no aceptadas como evidencia**). Los 64 archivos restantes no tienen lectura atribuible y completa. Los números de diapositiva proceden de WorkIQ, no de inspección visual independiente. Una lectura parcial no prueba cobertura de todo el deck ni despliegue en un cliente.

## 2. Registro de fuentes públicas

| Código | Fuente exacta y parte consultada | Límite |
|---|---|---|
| `MS-01` | [Microsoft: Quickly protect your organization against ransomware attacks](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware), pasos y prioridades. | Orden de prioridad general, no obligación cronológica técnica universal. |
| `MS-02` | [Microsoft: Ransomware attack recovery plan](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase1), respaldos, documentación y pruebas. | Recomendación, no prueba de respaldo de esta organización. |
| `MS-03` | [Microsoft: Limit the impact of ransomware attacks](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase2), acceso privilegiado, detección/respuesta. | Capacidades sujetas a cobertura, configuración y licencias. |
| `MS-04` | [Microsoft: Defend against ransomware attacks](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase3), prioridad frente a otros pasos. | Consulta parcial; no extraer controles específicos sin corroborar. |
| `MS-05` | [Microsoft Defender XDR: Responding to ransomware attacks](https://learn.microsoft.com/en-us/defender-xdr/playbook-responding-ransomware-m365-defender), contención, investigación y recuperación. | Playbook general, no guion de comandos universales. |
| `MS-06` | [Microsoft Defender for Endpoint: Take response actions on a device](https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts), descripción de acciones. | Consulta parcial; revisar permisos y versión antes de actuar. |
| `MS-07` | [Microsoft Azure: Backup and restore plan to protect against ransomware](https://learn.microsoft.com/en-us/azure/security/fundamentals/backup-plan-to-protect-against-ransomware), plan de backup/restauración. | Consulta parcial; diseño de copia y retención son decisiones locales. |
| `MS-08` | [Microsoft Support: Restore your OneDrive](https://support.microsoft.com/en-us/office/restore-your-onedrive-fa231298-759d-41cf-bcd0-25ac53eb8a15), restauración de actividad de archivos. | Capacidad acotada al producto/alcance; no restablece una aplicación entera. |
| `MS-09` | [Microsoft Defender XDR: Pilot and deploy](https://learn.microsoft.com/en-us/defender-xdr/eval-overview), componentes y pilotos. | Una función/licencia/piloto no demuestra implantación ni ensayo. |
| `MS-10` | [Microsoft Entra: Revoke user access](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access), access/refresh tokens y cookies. | Los tiempos/efectos dependen de aplicación y protocolo. |
| `EXT-01` | [CISA: #StopRansomware Guide](https://www.cisa.gov/resources-tools/resources/stopransomware-guide), **ficha** y descripción. | PDF completo no examinado; no atribuir pasos específicos a su texto. |
| `EXT-02` | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), **ficha** de gestión de incidentes. | No se leyó el texto completo; ejercicios/criterios del kit son derivados. |
| `EXT-03` | [NIST SP 800-34 Rev. 1 Update 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), **ficha** de planificación de contingencia. | No se leyó el texto completo; no afirmar alineamiento exhaustivo. |

El diseño de ejercicios E1/E2/E3 y los criterios de aceptación son **propuestas del kit**, apoyadas por el principio de ensayo en `MS-02`, pero no son una lista textual de CISA/NIST. Ninguna referencia pública informa plazos legales aplicables a un cliente determinado.

## 3. Registro interno leído por WorkIQ

| Código | Archivo y localizador comunicado por WorkIQ | Afirmación atribuible al material | Interpretación permitida |
|---|---|---|---|
| `INT-01` | `2601 - Human Operated Ransomware.pptx`, diap. 36–37. | Tratar aislamiento de equipos, protección de respaldos y ejercicio BC/DR. | Corrobora la pertinencia del tema; **no** que un ensayo se haya realizado. |
| `INT-02` | `202601 - Microsoft Security ADS - 3 - Modern SecOps.pptx`, diap. 25–33, 39. | Priorización de señales XDR e incidentes agrupados; automatización contextual de acciones de bajo riesgo. | Orientación de diseño, **no** evidencia de SOC implantado ni autorización de automatización disruptiva. |
| `INT-03` | `Cybersecurity Incident Response Customer Deck (2).PPTX`, diap. 10. | Fases de contención/restauración inicial y posterior estabilización/endurecimiento con servicios especializados. | Presentación de servicio; **no** runbook local ni garantía contractual. |
| `INT-04` | `Ransomware Experience Workshop - Workshop V3-Scavanna23.pptx`, diap. 37 y 47–48. | Propone probar restauración aislada de AD y discutir el orden de recuperación de cargas críticas. | Preguntas de taller; **no** prueba ejecutada ni decisión ya aprobada. |
| `INT-X1` | `202601 Ransomware Foundational Five - Shareable.pptx`, respuesta citó una versión sin `202601`. | No se acepta una afirmación del archivo exacto. | Requiere identificar versión y repetir consulta. |
| `INT-X2` | `Microsoft SAF -End to End Zero Trust Architecture - 202505 v2.pptx`, el identificador de archivo citado difiere del solicitado. | No se acepta una afirmación del archivo exacto. | Requiere resolver identidad de archivo. |

Los localizadores son números de diapositiva devueltos por WorkIQ; los enlaces de OneDrive recibidos abren el **archivo**, no la diapositiva precisa. No reproducir gráficos, tablas ni texto extensos de presentaciones. La clasificación y los derechos de uso del origen deben revisarse antes de distribuir un derivado de ellas.

## 4. Segmentos y afirmaciones atómicas relevantes

Los segmentos públicos se identifican como `SEG-01` (`MS-01` prioridades), `SEG-02` (`MS-02` copias y pruebas), `SEG-03` (`MS-03` privilegio/detección), `SEG-04` (`MS-05` contención), `SEG-05` (`MS-08` restauración de archivos), `SEG-06` (`MS-10` tokens/sesiones). Los internos `SEG-07` a `SEG-10` corresponden respectivamente a `INT-01` a `INT-04` y a sus diapositivas en la tabla. Fuente inglesa mayoritaria, con traducción analítica al español; se preserva `must`/`should` como recomendación de la **fuente** y no como obligación legal o estado observado.

| Claim | Segmento, clase y modalidad | Afirmación analítica y límite |
|---|---|---|
| `CLM-001` | `SEG-01`, recomendación de fuente, `recommended`. | Microsoft prioriza preparar recuperación, limitar daño y después dificultar entrada; no implica que todos los pasos deban ejecutarse secuencialmente. |
| `CLM-002` | `SEG-02`, recomendación de fuente, `required` en la guía. | Proteger copias de sistemas/datos críticos contra borrado, conservar documentos de recuperación y ejercitar BC/DR; no se observa cobertura real. |
| `CLM-003` | `SEG-03`, recomendación de fuente, `required` en la guía. | Privilegios protegidos y detección/respuesta rápida limitan alcance; licencias por sí solas no prueban capacidad. |
| `CLM-004` | `SEG-04`, fuente explícita, `recommended`. | Contención e investigación deben avanzar simultáneamente, priorizando contener; impacto humano/negocio condiciona la ejecución. |
| `CLM-005` | `SEG-04`, fuente explícita, `recommended` bajo condición. | Si es seguro y aplicable, aislar dispositivos comprometidos preservando sistemas; no apagar por defecto. |
| `CLM-006` | `SEG-05`, fuente explícita, `possible`. | La restauración de OneDrive puede revertir actividad de archivos en su alcance; no sustituye restauración de identidad o aplicaciones. |
| `CLM-007` | `SEG-06`, fuente explícita, `conditional`. | Bloqueo y revocación en Entra pueden tener latencia; una app controla su propia cookie y puede requerir revocación aparte. |
| `CLM-008` | `SEG-07`, atribuido a material, `recommended`. | El deck trata aislamiento, respaldo y ensayos; no certifica el estado de un entorno. |
| `CLM-009` | `SEG-08`, atribuido a material, `recommended`. | El deck plantea consolidar señales; no justifica automatización masiva sin aprobación. |
| `CLM-010` | `SEG-09`, atribuido a material, `asserted` como oferta. | Una secuencia de servicio de respuesta no es un procedimiento propio ya vigente. |
| `CLM-011` | `SEG-10`, material pedagógico, `questioned`. | Probar AD aislado y ordenar servicios es una actividad de taller; no un resultado observado. |
| `CLM-012` | `SEG-02/04/06`, **recomendación derivada**, `intended`. | El kit exige verificar efecto, evidencia y autorización de cada intervención; criterio propuesto, no cita literal. |

La confianza en `CLM-001..007` es alta para el alcance de las páginas leídas; en `CLM-008..011` es **parcial** por consulta selectiva de diapositivas. `INT-X1/X2` no sustentan ningún claim. Las negaciones críticas se conservan: **no** sustituir backup por sincronización; **no** inferir ausencia de exfiltración por silencio de logs; **no** equiparar revocación de refresh token con invalidación inmediata de todas las cookies.

## 5. Entidades, relaciones y arquitectura

Entidades analíticas: `ENT-01` función crítica (activo/proceso); `ENT-02` identidad/privilegio (control/tecnología); `ENT-03` respaldo (activo/capacidad); `ENT-04` SOC/guardia (actor/capacidad); `ENT-05` evidencia (dato); `ENT-06` CI y negocio (actores/decisiones); `ENT-07` Legal/Comunicaciones (actores); `ENT-08` entorno de recuperación (capacidad). No confundir “proveedor Microsoft” con dueño del incidente en el cliente.

Relaciones aceptadas: `REL-01` (explícita, `CLM-001`): prioridad editorial de recuperación frente a endurecimiento, **no** dependencia de infraestructura; `REL-02` (explícita, `CLM-004`): contención e investigación simultáneas; `REL-03` (explícita, `CLM-007`): app emite/controla su cookie de sesión; `REL-04` (inferencia analítica, `CLM-002/012`): BIA aprobado más prueba permite evaluar RTO/RPO. Relación descartada `REL-X1`: deck de SOC -> “la organización ya automatiza contención”; **sin evidencia de despliegue**. Relación descartada `REL-X2`: preguntas de taller -> “AD restaurado”; **pregunta no es resultado**. Ningún dibujo de flujo debe insinuar causalidad o cobertura que no existe.

**Pregunta `QST-001`:** ¿cómo evaluar, construir, operar y probar resiliencia integral ante ransomware sin afirmar capacidad no demostrada? Patrones `STP-001` clasificación de capacidades, `STP-002` proceso de decisión en crisis, `STP-003` dependencia de recuperación por servicio, `STP-004` estado/observabilidad y `STP-005` incertidumbre legal y forense. Ejes `AXS-001` gobierno/BIA, `AXS-002` recuperación, `AXS-003` prevención/privilegios, `AXS-004` detección/contención, `AXS-005` evidencia/continuidad, `AXS-006` comunicaciones/ejercicios. Cada eje tiene salida propia en los documentos 01–10; los solapamientos son deliberados (identidad también condiciona recuperación, evidencia también condiciona comunicación).

**Arquitectura `ARC-001`: híbrida y parcialmente MECE.** Es posible repartir **artefactos** por función principal (BIA, matriz de controles, registro de incidentes, mensajes), pero las **capacidades y los riesgos** se solapan y no deben forzarse a categorías mutuamente excluyentes. Se descartó un único proceso lineal: las pistas de contención/investigación y continuidad/legal operan en paralelo. Riesgos visuales `VIS-001`: interpretar todos los `No evaluado` como fallos probados; `VIS-002`: dar a un orden de prioridad el aspecto de dependencia técnica; `VIS-003`: mostrar el recuento de filas de plantilla como cobertura real. Los HTML señalan estas reservas.

## 6. Contradicciones, ambigüedades, lagunas y auditoría

**Contradicciones `CON`:** ninguna confirmada en las afirmaciones usadas; diferencias de alcance entre soporte de archivos y recuperación empresarial no son contradicción. **Ambigüedades `AMB-01/02`:** identificación de versión en `INT-X1/X2`, excluida. **Lagunas `GAP-01..06`:** organización/activos y BIA; despliegue/licencias/cobertura; puntos de copia y ensayos; jurisdicciones/obligaciones; autoridad/contactos; lectura de 64 presentaciones no atribuibles y textos completos CISA/NIST. No se inventan para cerrar el contrato.

Control de calidad: todas las recomendaciones sustantivas del kit enlazan códigos de fuente o están marcadas como **diseño derivado**; ejemplos de comandos/productos no se traducen en ejecución; no se atribuyen cifras, plazos legales o resultados operativos a la colección. Para un programa específico, la próxima etapa es completar BIA, validar fuentes/documentos faltantes y recoger evidencia de controles antes de publicar un estado de madurez.

## 7. Trazabilidad y estado de lectura de los tres artefactos canónicos vinculados en v2.0

El 12 de noviembre de 2026 se inspeccionaron directamente los catálogos estructurados y guías locales de los tres paquetes solicitados por el usuario para construir la versión 2.0, preservando sus **nombres canónicos** dado que su ubicación definitiva se definirá posteriormente:

| Paquete canónico | Archivos leídos y verificados directamente | Cobertura y límites explícitos |
|---|---|---|
| `PKG-NINJA` · `Ninja_Training_Seguridad_Microsoft_2026` | `MANIFIESTO_VERSION.json` (`v2026-11-08`: 15 programas, 387 módulos, ~2.000 h, 2.165 ejercicios), `README.md` general y `Anexo_Entorno_de_practica.md` (créditos Visual Studio Enterprise, pruebas M365 E5/Purview/Entra/Defender/Sentinel, límites de SCU y práctica segura en producción). | Todos los códigos de módulo y duraciones en horas de `ROL-01..09`, `CT-01..21`, `DE-01..13` y `PB-01..07` fueron validados programáticamente contra `MANIFIESTO_VERSION.json`. Las condiciones de licenciamiento y precios citadas heredan fecha de corte 6–8 de noviembre de 2026 y deben revalidarse tras Microsoft Ignite (17–20 de noviembre de 2026). |
| `PKG-KPI-OKR` · `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera` | `AI_CISO_Atlas_KPIs_OKRs_Catalogo_v1.0.json`, `AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_Guia_v1.0.md` y `AI_CISO_Atlas_KPIs_OKRs_Catalogo_v1.1.json` (hidratados localmente: 64 KPIs `K01..K64`, 6 `KSG01..KSG06`, 7 perfiles sectoriales, paquetes de Directorio/Esenciales y OKR territoriales/sectoriales/Año 1). | Los archivos `v1.2` (`Catalogo_v1.2.json`, `Guia_v1.2.md`, `v1.2_2026-11-10.xlsx`) estaban marcados en OneDrive bajo demanda sin hidratar localmente (`os error 389`); su referencia canónica y los 70 indicadores integrados se verificaron mediante `AI_CISO_Atlas_CISO365_Catalogo_v1.0.json` (`measurement_catalog: v1.2`) y `07_Sistema_de_Medicion_KPIs_y_OKR_v1.0.md`. |
| `PKG-CISO365` · `AI_CISO_Atlas_CISO365` | `AI_CISO_Atlas_CISO365_Catalogo_v1.0.json` completo (7 fases, 7 hitos/40 criterios, 130 actividades, 54 rituales, 32 rubros de recepción, 22 derechos de decisión, 51 prácticas, 56 entrevistas, 18 servicios, 6 preguntas del directorio y tabla de 70 indicadores), `00_Indice_y_Guia_de_Uso_v1.0.md` y `07_Sistema_de_Medicion_KPIs_y_OKR_v1.0.md`. | `08_Validacion_con_la_Formacion_v1.0.md` estaba sin hidratar en disco local, pero su resumen estructurado (`reference_training`) se leyó íntegramente desde `AI_CISO_Atlas_CISO365_Catalogo_v1.0.json`. Ningún mapeo en v2.0 afirma que una organización haya ejecutado las actividades `ACT-*` o alcanzado estadios `E3`/`E4`. |

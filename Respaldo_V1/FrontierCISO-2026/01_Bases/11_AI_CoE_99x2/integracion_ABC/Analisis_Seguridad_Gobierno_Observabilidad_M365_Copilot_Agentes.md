# Análisis de seguridad, gobierno y observabilidad para Microsoft 365 Copilot y agentes de IA
**Fecha de corte:** 21 de septiembre de 2026  
**Universo de planeamiento:** 10.000 usuarios  
**Escenarios:** actual; agregar Microsoft Purview Suite; migrar a Microsoft 365 E7
> **Conclusión ejecutiva.** El escenario actual tiene una base de amenaza sólida por la cobertura Defender, pero no ofrece cobertura homogénea de seguridad de datos ni del plano de control avanzado de agentes. Agregar Purview Suite cierra la brecha de datos y cumplimiento, pero no la de identidad, lifecycle, herramientas/MCP y observabilidad agentic. Migrar los 10.000 usuarios a Microsoft 365 E7 es el único de los tres escenarios que alinea licenciamiento de Copilot, Purview, Defender, Entra Suite y Agent 365 a escala completa. La licencia, sin embargo, no sustituye configuración, asignación, ALM, controles de Power Platform, operación SOC ni capacidad de Copilot Studio fuera de los usos zero-rated.

## 1. Hallazgos y decisión
- **Estado actual:** 100% de la población tiene Defender Suite; Purview avanzado cubre solo **500–600 usuarios (5%–6%)**, Microsoft 365 Copilot **5.000–5.100 (50%–51%)** y E7/Agent 365 avanzado **100 (1%)**. Los rangos reflejan solapamiento no informado.
- **Agent 365 ya aporta una capa base:** el registro, acciones básicas de gobierno, automatización básica de lifecycle y sincronización de metadatos están incluidos con planes Microsoft 365 elegibles. Las plantillas de políticas, observabilidad avanzada, Graph API, controles de herramientas/MCP, Entra agent governance y las capacidades agent-specific de Purview/Defender requieren E7/G7 o Agent 365 según la descripción de servicio vigente. [S07] [S09]
- **Escenario 2 — Purview para 10.000:** es el mejor paso inmediato para proteger datos, investigar prompts/respuestas y aplicar DLP, IRM, Communication Compliance, eDiscovery y retención a escala. Requiere **9.400–9.500 licencias adicionales** para llegar a 10.000; si primero se protege solo la cohorte Copilot, requiere **4.400–5.000**, según el solapamiento real y la posibilidad de reasignar los derechos existentes.
- **Escenario 3 — E7 para 10.000:** es el estado objetivo si la organización pretende que toda la población use Copilot/agentes o si los agentes empresariales acceden a datos y herramientas distribuidos. E7 integra E5, Microsoft Copilot, Entra Suite y Agent 365. [S05] [S06]
- **Recomendación:** adoptar Purview para todos los usuarios Copilot como requisito mínimo de 90 días; ampliar a 10.000 si las políticas abarcan toda la población; migrar a E7 por oleadas para cohortes agentic de alto impacto y, si la estrategia es enterprise-wide, completar la migración. No mantener agentes críticos fuera del perímetro plenamente licenciado.

## 2. Alcance, supuestos y advertencias
| ID | Supuesto | Valor | Implicación |
|---|---|---|---|
| A01 | Población de planeamiento | 10.000 usuarios | Se usa como denominador porque el inventario mayor es 10.000 licencias Defender Suite. |
| A02 | Solapamiento E7 | Las 100 licencias E7 están dentro de los 10.000 usuarios | Evita sumar usuarios fuera del universo; si fueran adicionales, recalcular a 10.100. |
| A03 | Solapamiento Purview/E7 | No informado | La cobertura avanzada única de Purview está entre 500 y 600 usuarios (5%–6%). |
| A04 | Solapamiento Copilot/E7 | No informado | La cobertura única de Microsoft 365 Copilot está entre 5.000 y 5.100 usuarios (50%–51%). |
| A05 | Nombre del SKU Defender | “M365 E5 Defender Suite” se interpreta como Microsoft Defender Suite, no como Microsoft 365 E5 completo | Es crítico para Security Copilot: la inclusión documentada aplica a Microsoft 365 E5/E7, no se asume para un add-on Defender aislado. |
| A06 | Escenario “Agregar Purview Suite” | Extender Purview Suite a toda la población de 10.000 | Se muestran también los asientos necesarios para cubrir solo la cohorte Copilot. |
| A07 | Escenario “Migrar a M365 E7” | Asignar M365 E7 a los 10.000 usuarios | E7 incluye E5, Microsoft Copilot, Entra Suite y Agent 365 según fuentes vigentes. |
| A08 | Cobertura vs. habilitación | Tener licencia no equivale a tener el control configurado | Todos los estados “Completo” presuponen asignación, roles, conectores, políticas, onboarding, pruebas y operación. |
| A09 | Costos | Sin precios ni descuentos contractuales | No se realiza TCO; se señalan licencias incrementales y oportunidades de racionalización. |
| A10 | Fecha de corte | 21 de septiembre de 2026 | Las capacidades cloud cambian; validar Product Terms, Service Descriptions y Message Center antes de compra o despliegue. |

### Advertencia crítica de SKU
Este análisis interpreta “M365 E5 Defender Suite” como **Microsoft Defender Suite** (add-on), no como **Microsoft 365 E5 completo**. La inclusión de Security Copilot documenta 400 SCU/mes por cada 1.000 licencias pagas **Microsoft 365 E5 o E7**, hasta 10.000 SCU. Por ello, el cálculo conservador actual usa solo 100 E7 = **40 SCU/mes**. Si las 10.000 licencias fueran en realidad Microsoft 365 E5 completas, el tenant tendría **4.000 SCU/mes** y debe corregirse la comparación. [S15]

## 3. Modelo de arquitectura y responsabilidad
La referencia de diseño es **agente administrado + datos administrados**. Un agente administrado se registra, publica metadatos, usa identidad Zero Trust, emite telemetría y está gobernado; los datos administrados clasifican, protegen y diferencian actividad de agentes. Agent 365 actúa como plano de control y experiencia consolidada, pero los controles se ejecutan en los productos fuente. [I01] [I02] [S07] [S08]

| Capa | Producto/portal principal | Función | Enforcement real |
|---|---|---|---|
| Inventario y lifecycle | Microsoft 365 admin center / Agent 365 | Registro, propietarios, aprobación, despliegue, bloqueo, retiro, políticas y mapa | Acciones administrativas sobre disponibilidad y lifecycle |
| Identidad y acceso | Microsoft Entra | Agent ID, blueprints, CA, Identity Protection, access packages, sponsor, expiración, red/MCP | Autenticación, autorización, CA y revocación |
| Datos y cumplimiento | Microsoft Purview | DSPM/AI observability, etiquetas, DLP, IRM, Audit, eDiscovery, retención, Compliance Manager | Bloqueo/advertencia DLP, derechos VIEW/EXTRACT, retención y holds |
| Amenazas | Microsoft Defender XDR/MDE | Descubrimiento, postura, incidentes, hunting, runtime protection y bloqueo de tool calls | Detección, alertas y bloqueo cuando la integración está habilitada |
| Plataforma low-code | Power Platform/Copilot Studio | Entornos, conectores, MCP, DLP/data policies, publicación, ALM, capacidad | Bloqueo/suspensión/cuarentena de recursos y fallos runtime |
| Operación | Security Copilot + SIEM/Sentinel | Investigación, automatización y correlación | Acelera análisis; no reemplaza controles subyacentes |

El enfoque sigue Zero Trust —verificar explícitamente, mínimo privilegio y asumir brecha— y las seis áreas del workshop: mapear riesgo, registrar agentes, asegurar autenticación/acceso, asegurar red, asegurar datos, construir de forma segura y detectar/responder. [S02] [S03] [S04]

## 4. Cobertura cuantitativa
| Dominio | Actual | Agregar Purview | Migrar a E7 | Observación |
|---|---:|---:|---:|---|
| Defender XDR / Defender Suite | 10.000 (100%) | 10.000 (100%) | 10.000 (100%) | Usuarios con cobertura base de amenazas [S05] [S16] |
| Purview avanzado - mínimo | 500 (5%) | 10.000 (100%) | 10.000 (100%) | Mínimo único asumiendo solapamiento total de las 100 E7 dentro de las 500 Purview [S11] [S13] |
| Purview avanzado - máximo | 600 (6%) | 10.000 (100%) | 10.000 (100%) | Máximo único asumiendo que las 100 E7 no solapan las 500 Purview [S11] [S13] |
| Microsoft 365 Copilot - mínimo | 5.000 (50%) | 5.000 (50%) | 10.000 (100%) | Mínimo único asumiendo solapamiento total de E7 con Copilot [S05] [S14] |
| Microsoft 365 Copilot - máximo | 5.100 (51%) | 5.100 (51%) | 10.000 (100%) | Máximo único asumiendo que E7 no solapa los 5.000 add-ons [S05] [S14] |
| M365 E7 / Entra Suite / Agent 365 avanzado | 100 (1%) | 100 (1%) | 10.000 (100%) | Derechos completos integrados por usuario [S05] [S07] [S08] |
| Agent 365 inventario y gobierno básico | 10.000 | 10.000 | 10.000 | Disponible con planes M365 elegibles; no confundir con observabilidad/controles avanzados [S07] [S09] |

**Lectura:** la activación de una capacidad tenant-wide no amplía automáticamente los derechos de uso. En Purview, cualquier usuario que se beneficie requiere licencia; en ubicaciones compartidas, owners y members requieren licencia cuando la política se usa sobre el sitio/equipo. [S11]

## 5. Comparación de escenarios
| Escenario | Entitlements | Qué habilita | Brechas | Adecuación | Acción |
|---|---|---|---|---|---|
| 1. Actual | 10.000 Defender Suite; 500 Purview Suite; 100 E7; 5.000 M365 Copilot | Defensa XDR amplia; Copilot para ~50%; inventario y gobierno básico de agentes; pequeño enclave E7 integrado | Purview avanzado solo 5%–6%; Agent 365/Entra avanzados 1%; controles y telemetría fragmentados; posible brecha de Security Copilot si Defender no es M365 E5 completo | Apto para piloto/control por cohortes; no para escalar agentes de alto impacto a 10.000 usuarios sin segmentación y compensaciones | Mantener como estado transitorio; restringir agentes críticos a cohortes plenamente licenciadas. |
| 2. Agregar Purview Suite | Extender Purview Suite a 10.000; mantener Defender, E7 y Copilot actuales | Cierra protección, investigación y gobierno de datos para toda la población: DSPM, DLP, etiquetas, IRM, Communication Compliance, eDiscovery, Audit Premium y retención | Agent 365 avanzado, Entra Suite y protección agente-específica de Defender siguen en 1%; Copilot permanece en ~50%; Power Platform y créditos externos siguen siendo requisitos separados | Mejor opción para reducir rápidamente riesgo de datos y shadow AI sin ampliar Copilot a todos | Agregar 9.400–9.500 Purview Suite para 10.000; o 4.400–5.000 para cubrir primero la cohorte Copilot, sujeto a reconciliar asignaciones. |
| 3. Migrar a Microsoft 365 E7 | Asignar E7 a 10.000 usuarios y racionalizar add-ons solapados al renovar | Cobertura integrada 100%: E5 + Copilot + Entra Suite + Agent 365; Purview y Defender avanzados; observabilidad, identidad, ciclo de vida y acceso a agentes | No elimina necesidad de configuración, operación, PAYG/Copilot Credits para usos no zero-rated, licencias de productos externos ni controles de Power Platform/Foundry | Mejor estado objetivo para adopción agentic enterprise-wide y simplificación de SKUs | Ejecutar por oleadas y retirar add-ons duplicados solo después de validar contrato, asignaciones, uso y dependencia. |

### 5.1 Escenario actual
**Puede hacer:**
- Operar Defender XDR para usuarios, endpoints, identidades, correo y SaaS en 10.000 usuarios; descubrir uso de apps de IA y aplicar controles existentes de amenaza.
- Dar Microsoft 365 Copilot y agentes integrados a aproximadamente la mitad de la población. Los usuarios con M365 Copilot pueden usar Copilot Studio para extender Copilot; classic answers, generative answers y grounding con Microsoft Graph en Copilot Chat, Teams o SharePoint son zero-rated. [S14]
- Usar el inventario y las acciones básicas de Agent 365 con planes M365 elegibles, además del enclave E7 de 100 usuarios para funciones avanzadas. [S07] [S09] [S10]
- Aplicar Purview avanzado, de forma licenciada, a 500–600 usuarios y ejecutar un piloto integrado E7 para 100.
**Brechas principales:**
- Entre **4.400 y 5.000 usuarios Copilot** podrían carecer de Purview avanzado, según el solapamiento y la asignación real; esto limita DLP avanzado, DSPM profundo, IRM, Communication Compliance, eDiscovery/Audit Premium y retención avanzada.
- Solo 1% tiene E7: la observabilidad avanzada, CA/riesgo para agentes, access packages/sponsors, controles MCP y protección Defender específica de agentes no escalan al universo completo.
- La protección de Copilot Studio en tiempo real exige onboarding de Agent 365, conector M365 y coordinación entre Security Admin y Power Platform Admin. La licencia Defender por sí sola no configura esta integración. [S16]
- El estado actual debe limitar agentes críticos a usuarios/datos cubiertos o aplicar medidas compensatorias: datos no sensibles, solo lectura, herramientas allowlisted, revisión humana y bloqueo de publicación externa.

### 5.2 Agregar Purview Suite
**Puede hacer adicionalmente:**
- Proteger a toda la población con clasificación y etiquetado automático, DLP para Copilot/agentes, Endpoint DLP para IA de terceros, DSPM/AI observability, Insider Risk/Adaptive Protection, Communication Compliance, eDiscovery, Audit Premium y retención.
- Tratar instancias de agentes como sujetos de política, incorporándolas explícitamente o mediante grupos. Purview soporta actividad human-to-agent, agent-to-human, agent-to-tools y agent-to-agent en auditoría; la aplicabilidad varía por solución. [S13]
- Investigar y remediar sobreexposición de datos sin esperar una migración completa a E7.
**Brechas que permanecen:**
- Agent 365 avanzado/Entra Suite continúa en 100 usuarios. El escenario mejora profundamente el **data plane**, pero no completa el **identity/control plane** agentic.
- No amplía Microsoft 365 Copilot más allá de 5.000–5.100 usuarios.
- No cubre por sí solo Copilot Credits, premium connectors, canales externos, Azure consumption, licencias de sistemas conectados ni controles ALM/Power Platform.

### 5.3 Migrar a Microsoft 365 E7
**Puede hacer adicionalmente:**
- Dar a 10.000 usuarios la pila integrada: M365 E5 + Microsoft Copilot + Entra Suite + Agent 365. [S05] [S06]
- Extender identidad y gobierno de acceso a agentes con Agent ID, blueprints, Conditional Access, Identity Protection, sponsors, expiración y access packages. [S17]
- Habilitar observabilidad y política avanzada Agent 365, Purview agentic y Defender agent-specific a escala, sujeto a onboarding y compatibilidad de plataforma. [S07] [S13] [S16]
- Recibir **4.000 SCU/mes** de Security Copilot para 10.000 E7, compartidas en el tenant; las SCU no usadas no se trasladan. [S15]
**Brechas/requisitos que permanecen:**
- E7 no corrige permisos de SharePoint, no crea etiquetas/políticas, no diseña entornos ni mantiene dueños; esas son responsabilidades operativas.
- El consumo Copilot Studio no zero-rated sigue requiriendo Copilot Credits/PAYG/prepago. [S14]
- Agentes no soportados, no registrados o sin SDK/conector pueden mantener puntos ciegos. Drafts no se visualizan uniformemente en todas las plataformas. [S09]

## 6. Matriz resumida de capacidades
La matriz completa está en la hoja **Matriz_Capacidades** del Excel. Los puntos de decisión son:
| Dominio | Actual | Agregar Purview | E7 |
|---|---|---|---|
| Agent 365 | Básico tenant; avanzado 100 | Igual | Avanzado 10.000 |
| Entra para agentes | 100 | 100 | 10.000 |
| Purview avanzado | 500–600 | 10.000 | 10.000 |
| Defender XDR core | 10.000 | 10.000 | 10.000 |
| Defender agent-specific | 100/condicional | 100/condicional | 10.000/condicional |
| Microsoft 365 Copilot | 5.000–5.100 | 5.000–5.100 | 10.000 |
| Copilot Studio zero-rated M365 | 5.000–5.100 | 5.000–5.100 | 10.000 |
| Power Platform governance | Debe implementarse | Debe implementarse | Debe implementarse |
| Security Copilot | 40 SCU/mes* | 40 SCU/mes* | 4.000 SCU/mes |

## 7. Requisitos de asignación y configuración
| Área | Regla | Acción | Fuente |
|---|---|---|---|
| Purview - regla general | Cada usuario que se beneficia de una función Purview debe tener la licencia correspondiente asignada. | No habilitar políticas avanzadas de alcance general sin cubrir a los usuarios beneficiados. | [S11] |
| Purview - ubicaciones personales | Mailbox, OneDrive, Teams chats y dispositivos se asocian a usuario; el usuario requiere licencia cuando aplica la política. | Cruzar el alcance de políticas con el inventario de licencias. | [S11] |
| Purview - ubicaciones compartidas | En SharePoint/Groups/Teams, propietarios y miembros necesitan licencia; visitantes/view-only no. | Licenciar miembros/owners de sitios cubiertos y revisar membresía. | [S11] |
| M365 Copilot | Asignar a cada usuario que use grounding de trabajo, apps M365 y agentes incluidos. | Usar grupos dinámicos y proceso Joiner/Mover/Leaver. | [S05] [S14] |
| Copilot Studio - autor | Acceso mediante M365 Copilot o configuración de Copilot Studio; el rol/licencia de maker no sustituye capacidad tenant cuando aplica. | Separar maker, publisher y admin; usar grupos de seguridad. | [S14] |
| Copilot Studio - consumo | Zero-rated solo para usos definidos en Copilot Chat/Teams/SharePoint por usuarios M365 Copilot; otros canales/acciones pueden consumir Copilot Credits. | Presupuesto, alertas y PAYG/prepago por entorno. | [S14] |
| Agent 365 | Licenciamiento por usuario; funciones avanzadas vía E7/G7 o Agent 365 standalone. | Licenciar operadores/usuarios beneficiados y validar Product Terms para alcance tenant. | [S07] [S08] |
| Agent 365 básico | Inventario y ciertas acciones básicas vienen con planes M365 elegibles; no confundir con observabilidad y controles premium. | Habilitar ya el registro; marcar explícitamente funciones no licenciadas. | [S07] |
| E7 | Debe asignarse a los usuarios objetivo; compra sin asignación no amplía derechos. | Migrar por grupos, verificar service plans y retirar add-ons solo tras validación. | [S05] |
| Security Copilot | Inclusión documentada para M365 E5/E7; capacidad tenant compartida y reinicia mensualmente. | Confirmar si “Defender Suite” es add-on o M365 E5 completo antes de contabilizar SCU. | [S15] |
| Defender agentes locales | MDE debe estar activo; onboarding de agentes locales es separado. | Inventariar endpoints y validar modo activo/salud del sensor. | [S16] |
| Defender Copilot Studio | Conectar M365 y Power Platform; coordinar Security Admin y Power Platform Admin. | Prueba de bloqueo + generación de alerta/incidente end-to-end. | [S16] |
| Roles privilegiados | AI Admin/Global Admin para acciones críticas; Compliance Admin, Security Admin y roles Purview; Azure AI Owner para start/stop Foundry. | PIM/JIT, cuentas separadas, aprobación y revisión trimestral. | [S09] [S10] [S13] [S16] |

## 8. Controles organizacionales obligatorios
| ID | Control | Evidencia | Dueño | KPI propuesto |
|---|---|---|---|---|
| C01 | Consejo de IA y decisión de riesgo: Carta, miembros, umbrales, excepciones y escalación | Acta y registro de decisiones; Trimestral | Sponsor ejecutivo / CISO | % agentes de alto riesgo revisados [S01] [S04] [S19] |
| C02 | Política de uso aceptable y shadow AI: Apps permitidas/prohibidas, datos admitidos, reporte y sanciones | Política publicada y aceptación; Semestral | Legal + CISO + RR.HH. | Cobertura de aceptación; apps no sancionadas [S01] [S03] |
| C03 | Clasificación de agentes por riesgo: Tiers: personal, equipo, empresarial, misión crítica; autonomía y blast radius | Ficha de clasificación; En alta y cambio mayor | AI Council | % inventario con tier y criticidad [S03] [S19] |
| C04 | Propietario, sponsor y data owner: Responsabilidad 1:1, suplente y fecha de expiración | Registro sin huérfanos; Mensual | Business Owner + IAM | % agentes con owner/sponsor/data owner [S09] [S17] [S19] |
| C05 | Intake y aprobación: Caso de negocio, datos, herramientas, permisos, privacidad, RAI y threat model | Gate firmado; Cada release | AI CoE / Seguridad | % releases con aprobación completa [S03] [S19] |
| C06 | Zonas de entorno y ALM: Dev/Test/Prod, soluciones, pipelines, segregación y rollback | Pipeline y bitácora de release; Continuo | Power Platform CoE | % agentes prod desplegados por pipeline [S18] [S19] |
| C07 | Gobierno de conectores y MCP: Allow/deny/restrict, clasificación Business/Non-business, revisión de acciones | Matriz de conectores y excepciones; Mensual | Power Platform Admin + Arquitectura | Conectores/MCP no aprobados; edad de excepción [S07] [S18] |
| C08 | Mínimo privilegio para usuarios y agentes: Agent ID, CA, access packages, expiración, revisiones, sin secretos | Access review y evidencia CA; Trimestral | IAM/Entra | Permisos altos; accesos vencidos; agentes riesgosos bloqueados [S02] [S03] [S17] |
| C09 | Gobierno de datos para IA: Etiquetas, EXTRACT, DLP, DSPM, IRM, retención, eDiscovery | Mapa de políticas y pruebas; Mensual | Data Security / Purview | % población licenciada y cubierta; DLP incidents [S11] [S12] [S13] |
| C10 | Observabilidad unificada: Registro + Purview AI observability + Defender + Entra + SIEM | Dashboard, logs y reglas; Continuo | SOC + AI Platform | % agentes con señales; MTTD; cobertura 30 días [S07] [S09] [S13] [S16] |
| C11 | Protección runtime y pruebas adversarias: Prompt injection, jailbreak, tool abuse, exfiltración, contenido inseguro | Resultados de red team y bloqueo; Por release y trimestral | Product Security / SOC | % críticos probados; tasa de bloqueo; hallazgos abiertos [S01] [S03] [S16] |
| C12 | Respuesta a incidentes de IA: Runbooks para fuga, agente comprometido, acción indebida y rollback | Ejercicio y postmortem; Semestral | SOC/CSIRT | MTTD/MTTR; % acciones dentro de SLA [S03] [S04] [S16] |
| C13 | Auditoría, retención y evidencia: Retención diferenciada, holds, exportación, cadena de custodia | Prueba de búsqueda/exportación; Trimestral | Compliance/Legal | % fuentes con retención; éxito de eDiscovery [S11] [S13] |
| C14 | FinOps de Copilot y agentes: Licencias, Copilot Credits, SCU, Azure, third-party, showback | Dashboard de costo/uso; Mensual | FinOps + Product Owner | Costo por agente activo; crédito por outcome; capacidad restante [S14] [S15] [S19] |
| C15 | Gestión de cambios, formación y comunicación: Formación por rol, safe prompting, desarrollo seguro, champions | Plan y asistencia; Trimestral | Adoption Lead + HR | Adopción segura; incidentes por error humano [S01] [S19] |
| C16 | Desmantelamiento y conservación: Bloqueo, exportación/hold, eliminación, revocación y cierre de costos | Checklist de retiro; Mensual | Agent Owner + Admins | Agentes inactivos; huérfanos; tiempo a retirar [S10] [S13] [S17] |

## 9. Modelo madurativo
Los niveles siguen el modelo oficial 100–500 y añaden criterios de salida **propuestos** para este cliente; no son benchmarks de Microsoft. [S19]
| Nivel | Estado | Criterios de salida propuestos | Encaje de escenario |
|---|---|---|---|
| 100 - Inicial | Agentes aislados, sin inventario confiable ni estándares específicos; controles reactivos. | ≥60% agentes detectados; ≥80% con owner; 100% agentes críticos bloqueados o en revisión. | No escalar agentes con datos sensibles. |
| 200 - Repetible | Controles tenant básicos y revisiones manuales; entornos y aprobación aplicados de forma inconsistente. | ≥85% inventario soportado; ≥90% con tier/owner; 100% releases productivos con checklist. | Escenario actual puede llegar aquí si restringe alcance y ejecuta controles compensatorios. |
| 300 - Definido | Gobierno, seguridad y cumplimiento documentados y aplicados; registro central; métricas y ALM formal. | ≥95% agentes registrados; 100% críticos con threat model, DLP, CA y retención; ≥90% cobertura licenciada objetivo. | Escenario 2 habilita mejor este nivel desde datos; Agent 365 avanzado sigue limitado. |
| 400 - Capaz | Gobierno basado en riesgo y parcialmente automatizado; monitoreo continuo y remediación proactiva. | 100% críticos con runtime protection; ≥95% señales al SOC; MTTR objetivo <4h para severidad alta; 0 agentes huérfanos >7 días. | E7 a la población agentic facilita este nivel; objetivos son propuestos, no benchmarks Microsoft. |
| 500 - Eficiente | Agentes operados como servicios digitales por tier; cumplimiento continuo; operación predictiva y auto-optimizada. | ≥99% cumplimiento de baseline; recertificación continua; retiro automático por inactividad/riesgo; valor y riesgo revisados juntos. | Objetivo de largo plazo; mantener inversión y evitar estancamiento. |

### Trayectoria sugerida
1. **Actual → 200 Repetible:** inventario, owners, política, tiers, entornos y telemetría base; restringir agentes críticos.
2. **Purview completo → 300 Definido:** protección y cumplimiento de datos a escala; ALM y gates formales; falta completar control plane agentic.
3. **E7 para población agentic → 400 Capaz:** identidad, políticas, observabilidad y runtime protection integrados; automatización con supervisión humana.
4. **500 Eficiente:** operación por SLO, cumplimiento continuo, predictive risk, self-healing controlado y revisión conjunta de valor/riesgo.

## 10. Roadmap de ejecución
| Horizonte | Frente | Acción | Responsable | Resultado |
|---|---|---|---|---|
| 0–30 días | Licenciamiento | Confirmar SKU exacto de las 10.000 “Defender Suite”, base licenses y solapamientos de E7/Purview/Copilot. | Licensing + M365 Admin | Export de asignaciones reconciliado; decisión sobre SCU. |
| 0–30 días | Inventario | Activar/revisar Agent Registry, conectar plataformas soportadas y clasificar draft/shared/production. | AI Admin | Inventario único con owner, plataforma, estado y criticidad. |
| 0–30 días | Datos | Mapear 5.000 usuarios Copilot contra 500 Purview y 100 E7; no permitir datos críticos fuera de cobertura. | Purview + IAM | Lista de usuarios sin cobertura y controles compensatorios. |
| 0–30 días | Power Platform | Definir zonas de entornos y congelar publicación directa a producción para agentes de alto riesgo. | Power Platform CoE | Política Dev/Test/Prod y grupos de seguridad. |
| 31–60 días | Purview | Piloto de etiquetas, EXTRACT, DSPM, DLP Copilot/agents, Endpoint DLP e IRM en modo auditoría. | Purview Admin | Reporte de falsos positivos y plan de enforcement. |
| 31–60 días | Entra | Registrar agentes críticos, asignar owner/sponsor, aplicar CA en report-only y paquetes de acceso. | IAM | Cobertura de identidades y revisión de permisos. |
| 31–60 días | Defender | Onboard Agent 365 security, conector M365 y Copilot Studio real-time protection; validar alertas. | SOC + Power Platform | Prueba end-to-end con alerta, incidente y bloqueo. |
| 31–90 días | Gobierno | Aprobar política de uso, tiering, intake, RACI, excepciones y playbooks. | AI Council | Paquete de gobierno aprobado. |
| 31–90 días | Decisión escenario | Elegir cobertura Purview: 5.000 usuarios Copilot primero o 10.000 enterprise-wide. | CISO + CIO + Legal | Decisión y asignación financiada. |
| 61–120 días | Enforcement | Pasar DLP/CA/connector controls de test a bloqueo por oleadas, con break-glass y rollback. | Security + Platform | % políticas en enforce; incidentes de impacto. |
| 61–120 días | Observabilidad | Integrar logs de Entra, Purview, Defender y Agent 365 en SOC/SIEM; construir KPIs. | SOC | Dashboard operacional y retención probada. |
| 90–180 días | ALM/RAI | Implementar pipelines, threat modeling, evaluaciones Responsible AI y red teaming por tier. | AI CoE + Product Security | 100% agentes críticos con gates. |
| 3–6 meses | E7 | Si se elige E7, migrar cohortes de alto riesgo/alto valor y validar servicio antes de ampliar. | M365 Program | Oleada piloto con criterios de salida cumplidos. |
| 6–12 meses | Optimización | Racionalizar add-ons duplicados, automatizar lifecycle y revisar consumo Copilot Credits/SCU. | FinOps + Licensing | Ahorro/uso validado sin pérdida de control. |
| Continuo | Madurez | Medir nivel 100–500 trimestralmente y actualizar controles por nuevas capacidades/regulación. | AI Council | Scorecard y backlog trimestral. |

## 11. Criterios de go/no-go para agentes de producción
Un agente no debe pasar a producción si falta cualquiera de estos puntos:
- [ ] Agente inventariado, con identidad compatible cuando aplique, owner, sponsor, data owner, criticidad y fecha de expiración.
- [ ] Usuarios y ubicaciones beneficiadas con licencias correctas; no basarse en que la función sea visible tenant-wide.
- [ ] Threat model de prompts, grounding, herramientas, MCP, acciones, agent-to-agent y dependencias externas.
- [ ] Mínimo privilegio probado; CA/access package/consentimiento administrativo y revisión de permisos.
- [ ] Datos clasificados; etiquetas, VIEW/EXTRACT y DLP probados en modo auditoría y bloqueo.
- [ ] Conectores, entornos y canales aprobados; Dev/Test/Prod y rollback disponible.
- [ ] Logs visibles en los portales fuente y correlacionados en SOC; retención y eDiscovery probadas.
- [ ] Pruebas de prompt injection, jailbreak, exfiltración, tool abuse y contenido inseguro completadas.
- [ ] Human-in-the-loop y límites de autonomía definidos según el tier.
- [ ] Presupuesto y alertas de Copilot Credits/SCU/Azure establecidos; criterio de retiro por bajo valor o riesgo.

## 12. Fuentes
### Oficiales
- **[S01] [Build a strong security posture for AI](https://learn.microsoft.com/en-us/security/security-for-ai/posture)** — Marco Prepare–Discover–Protect–Govern; riesgos de fuga, sobreexposición, prompt injection y shadow AI.
- **[S02] [Overview - Use Zero Trust security to prepare for AI companions, including Microsoft Copilots](https://learn.microsoft.com/en-us/security/zero-trust/copilots/apply-zero-trust-copilots-overview)** — Zero Trust: verificar explícitamente, mínimo privilegio y asumir brecha; protección por tipo de grounding.
- **[S03] [Microsoft Zero Trust Workshop - AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security)** — Áreas de implementación: mapear riesgo, registrar agentes, acceso, red, datos, desarrollo seguro y detección/respuesta.
- **[S04] [Adopt and secure AI and data](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-scenario-secure-ai)** — Adopción segura: proteger la IA y usar IA para mejorar seguridad; disciplinas de estrategia, arquitectura, identidad, datos y SecOps.
- **[S05] [Prepare for Microsoft Copilot by comparing E3, E5, and E7 license features](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-license-feature-overview)** — E7 = E5 + Microsoft Copilot + Entra Suite + Agent 365; comparación de Purview, Security Copilot, Copilot y agentes.
- **[S06] [Microsoft 365 E7 for Enterprise](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7)** — Descripción comercial vigente de E7; unifica E5, Copilot, Entra Suite y Agent 365.
- **[S07] [Microsoft Agent 365 - Service Descriptions](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)** — Distingue inventario y gobierno básico incluido en planes M365 de las funciones avanzadas que requieren E7/G7 o Agent 365.
- **[S08] [Microsoft Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)** — Agent 365 como plano de control para observar, gobernar y proteger; licencia por usuario; GA comercial desde 1-may-2026.
- **[S09] [Agent overview in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide)** — Prerrequisitos, licenciamiento, inventario, métricas, plataformas y roles administrativos.
- **[S10] [Governance and Lifecycle actions for agents available in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions?view=o365-worldwide)** — Acciones instalar, bloquear, eliminar, publicar, reasignar propietario y operar Foundry.
- **[S11] [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)** — Regla de beneficio por usuario y disponibilidad de Audit, Communication Compliance y otras cargas.
- **[S12] [Considerations for deploying Microsoft Purview Data Security Posture Management (DSPM) for AI](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-considerations)** — Prerrequisitos de auditoría, licencias, onboarding de endpoint/navegador, PAYG y políticas de un clic.
- **[S13] [Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365](https://learn.microsoft.com/en-us/purview/ai-agent-365)** — Cobertura de DSPM, auditoría, clasificación, etiquetas, DLP, IRM, comunicación, eDiscovery y ciclo de vida para agentes.
- **[S14] [Licensing for agents powered by the standard harness](https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing)** — Licenciamiento de Copilot Studio, Copilot Credits y consumo zero-rated para usuarios con Microsoft 365 Copilot en canales M365.
- **[S15] [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)** — 400 SCU/mes por cada 1.000 licencias pagas M365 E5/E7, hasta 10.000 SCU; autoaprovisionamiento y límites.
- **[S16] [Enable security for AI agents using Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/get-started-defender-security-for-ai)** — Onboarding de Agent 365, conector M365, protección local con MDE activo y protección en tiempo real para Copilot Studio.
- **[S17] [Microsoft Entra security for AI overview](https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview)** — Agent ID, blueprints, Conditional Access, Identity Protection, access packages, sponsors, inventario y Secure Web/AI Gateway.
- **[S18] [Data policies - Power Platform](https://learn.microsoft.com/en-us/power-platform/admin/wp-data-loss-prevention)** — Políticas de datos, conectores, MCP, controles de diseño y ejecución, cuarentena y latencia de aplicación.
- **[S19] [Agentic AI maturity model - AI governance and security](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-security-governance)** — Modelo de madurez de cinco niveles: 100 Inicial a 500 Eficiente.
### Internas relevantes
Los documentos internos se usaron para contexto arquitectónico y de adopción; para licencias y disponibilidad prevalecen Product Terms, Service Descriptions y documentación oficial vigente.
- **[I01] [Security for AI reference architecture](https://microsoft-my.sharepoint.com/personal/scavanna_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7BF88BA673-2A06-4ADC-9CF5-B560CFD68B72%7D)** — Arquitectura de señales, sesiones, evaluaciones de riesgo y actuadores; datos y agentes administrados/no administrados.
- **[I02] [Securing AI Agents End to End](https://microsoft-my.sharepoint.com/personal/scavanna_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B121142E8-3792-4651-80AC-C6F493310789%7D)** — Integración conceptual de Purview DSPM, Agent 365 y AI Security Dashboard; usar fuentes oficiales para derechos de uso.
- **[I03] [SAF - AI Security - Strategy and Governance Planning](https://microsoft-my.sharepoint.com/personal/scavanna_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7BBB5CA240-359D-4077-AE6A-218988641CBF%7D)** — Material de estrategia y gobierno alineado con Security Adoption Framework.
- **[I04] [FY27 Securing AI - Microsoft Answer Presenter Slide Deck - Aug 5](https://microsoft.sharepoint.com/teams/LevelUpSkilling/_layouts/15/Doc.aspx?sourcedoc=%7BE7A26113-16B8-442A-85FD-908D4A43E9AA%7D)** — Narrativa FY27 de seguridad de IA y enfoque Zero Trust.
- **[I05] [Secure the AI Estate - FY27 QuickStart Series - Security CSU (2)](https://microsoft-my.sharepoint.com/personal/scavanna_microsoft_com/_layouts/15/Doc.aspx?sourcedoc=%7B64A40846-ED71-49DD-9ACE-58A9CA9F591C%7D)** — QuickStart interno sobre protección de datos, postura y adopción segura de IA.

---
**Nota de validación:** los cálculos de cobertura se reconciliaron contra un universo de 10.000; los rangos preservan la incertidumbre de solapamiento. El Excel contiene las fórmulas, la matriz completa, RACI, controles, madurez, roadmap y registro de fuentes.
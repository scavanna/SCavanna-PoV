# Nivel 3 · Avanzado · Ingeniería de plataforma y contenido

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Experto agéntico →](04_Nivel_4_Experto_agentico.md)

<a id="avanzado"></a>

Normalización, KQL avanzado, casos de uso, contenido como código, conectores propios, APIs, notebooks, data lake y graph, y operación multi-inquilino. Equivale a la parte 5 del Ninja original, ampliada.

*L400 · 9 módulos · ~59 horas · 130 recursos*

**Módulos de este nivel:** [A1 ASIM](#a1) · [A2 KQL avanzado](#a2) · [A3 Casos de uso](#a3) · [A4 Contenido como código](#a4) · [A5 Conectores CCF](#a5) · [A6 APIs](#a6) · [A7 Notebooks y ML](#a7) · [A8 Data lake y graph](#a8) · [A9 Multi-inquilino y MSSP](#a9)

<a id="a1"></a>

## A1 · ASIM: normalización con el Advanced Security Information Model

*L400 · ~6 h · Origen: Módulo 9 · Advanced SIEM information model and normalization*

Trabajar con decenas de fuentes y esquemas distintos complica escribir reglas, búsquedas y libros, y correlacionar entre ellas. El **Advanced Security Information Model (ASIM)** resuelve el problema con esquemas normalizados —autenticación, sesiones de red, procesos, DNS, archivos, web, auditoría, registro y más— y **parsers** que mapean cada fuente a esos esquemas en tiempo de consulta, alineados con el modelo abierto OSSEM.

El resultado es contenido independiente de la fuente: una regla de fuerza bruta o de viaje imposible funciona con cualquier origen compatible, incluso con los que agregues después. Este módulo cubre los esquemas, los parsers integrados y desplegados en el workspace, el contenido basado en ASIM, el impacto en el rendimiento y cómo desarrollar, probar y contribuir tus propios parsers.

**Qué vas a lograr**

- Explicar el modelo de normalización en tiempo de consulta y sus esquemas.
- Usar parsers unificadores y filtrantes en consultas y reglas.
- Desarrollar y probar un parser ASIM para una fuente personalizada.

> **Consejo Ninja.** Nombres de parsers: integrados `_Im_<esquema>`, específicos por fuente `_Im_<esquema>_<fuente>V<versión>` y desplegados en el workspace `im<esquema>`. Usa siempre los parámetros de filtrado y, si necesitas campos no normalizados, el parámetro `pack` los agrupa en AdditionalFields ([parsers ASIM](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-parsers)).

> **Atención.** Reglas actuales para desarrollar parsers: operaciones locales a cada registro, sin joins, watchlists, `externaldata`, `mv-expand` ni `summarize` ([desarrollar parsers](https://learn.microsoft.com/en-us/azure/sentinel/isv/normalization-develop-parsers)). Revisa la [disponibilidad por función](https://learn.microsoft.com/en-us/azure/sentinel/feature-availability): la documentación conceptual ya no muestra aviso de vista previa, pero la tabla de disponibilidad la ha listado como preview.

> **Novedad.** Esquemas disponibles: Agent, Alert, Audit, Authentication, DHCP, DNS, Email, File, Network Session, Process, Registry, User Management, Web Session y Asset Entity ([normalización](https://learn.microsoft.com/en-us/azure/sentinel/normalization)).

> **Atención.** Un aviso del Message Center (MC1281506) documenta un cambio importante en `ImProcessCreate`: revisa reglas y búsquedas que usen ese parser ([archivo comunitario del aviso](https://mc.merill.net/message/MC1281506)).

**¿Tienes poco tiempo?**

- [Using the Advanced Security Information Model (ASIM) parsers](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-parsers) · Documentación

### Documentación, cursos y credenciales

- [Using the Advanced Security Information Model (ASIM) parsers](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-parsers) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 oct 2026. Lista de parsers unificadores por esquema y uso de parámetros de filtrado y del parámetro pack para mejorar rendimiento.
- [The Advanced Security Information Model (ASIM) parsers (overview)](https://learn.microsoft.com/en-us/azure/sentinel/normalization-parsers-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 may 2026. Diferencia entre parsers integrados y desplegados en el workspace, jerarquía unificador/específico y convenciones de nombres (_Im_<schema>, _Im_<schema>_<source>V<version>).
- [Normalization and the Advanced Security Information Model (ASIM)](https://learn.microsoft.com/en-us/azure/sentinel/normalization) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 9 ('ASIM y normalización') del skill-up de Learn: doc «Convert existing rules».
- [Develop Advanced Security Information Model (ASIM) parsers](https://learn.microsoft.com/en-us/azure/sentinel/isv/normalization-develop-parsers) · Documentación · Oficial · Microsoft Learn. Proceso completo para desarrollar parsers ASIM propios: muestras, mapeo, parser filtrante y sin parámetros, pruebas, despliegue y contribución.
- [Advanced Security Information Model (ASIM) workspace deployed parsers](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-workspace-parsers) · Documentación · Oficial · Microsoft Learn. Cómo desplegar y personalizar parsers ASIM en el workspace (im<schema>) y añadir parsers propios a los unificadores.
- [User-defined functions in KQL](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/functions/user-defined-functions) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 9 ('ASIM y normalización') del skill-up de Learn: doc «KQL functions».
- [Advanced Security Information Model (ASIM) documentation](https://aka.ms/AzSentinelNormalization) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft (aka.ms). Enlace del Módulo 9 ('ASIM y normalización') del skill-up de Learn: doc «ASIM documentation».

### Webinars, videos y podcasts

- [Brewing KQL: Smarter Threat Intel Feeds with AI & MISP with Sergio Albea (KQL Cafe, May 2026)](https://www.youtube.com/watch?v=e-mg6XYcCAY) · Video · Comunidad · Nuevo · Gianni Castaldi, Alex Verboon, Sergio Albea · KQL Cafe (YouTube) · 26 may 2026. Episodio sobre evaluación de feeds de TI con KQL e IA, mejoras del portal de advanced hunting y un cambio disruptivo en la función ASIM ImProcessCreate.
- [Deep Dive into Microsoft Sentinel normalizing parsers and normalized content](https://www.youtube.com/watch?v=zaqblyjQW6k) · Webinar · Oficial · Legado aún útil · Ninja original · Microsoft Sentinel team · YouTube · 11 ago 2021. Material enlazado en el Módulo 9 ('ASIM y normalización') del skill-up de Learn: webinar «Deep Dive into Microsoft Sentinel normalizing parsers and normalized content» ofrecido en YouTube, MP3, presentation.

### Laboratorios, GitHub y herramientas

- [Parsers folder, including ASIM parsers (Azure-Sentinel on GitHub)](https://github.com/Azure/Azure-Sentinel/tree/master/Parsers) · GitHub · Oficial · Legado aún útil · Ninja original · GitHub. Enlace del Módulo 9 ('ASIM y normalización') del skill-up de Learn: github «_ parsers_».

**Manos a la obra**

1. `Laboratorio` Escribe una regla de fuerza bruta independiente de la fuente con `_Im_Authentication` y sus parámetros de filtrado.
2. `Laboratorio` Desarrolla un parser ASIM para una fuente Syslog de laboratorio, en versión filtrante y sin parámetros, y pruébalo con las herramientas de prueba de ASIM ([desarrollar parsers](https://learn.microsoft.com/en-us/azure/sentinel/isv/normalization-develop-parsers)).
3. `Laboratorio` Compara el rendimiento de una consulta con el parser unificador frente al parser específico de la fuente.

**¿Quieres profundizar?**

- [Brewing KQL: Smarter Threat Intel Feeds with AI & MISP with Sergio Albea (KQL Cafe, May 2026)](https://www.youtube.com/watch?v=e-mg6XYcCAY) · Video

<a id="a2"></a>

## A2 · KQL avanzado y optimización

*L400 · ~8 h · Origen: Módulo 10 · Kusto Query Language (segunda parte) y #7b Optimizing KQL*

Con lo básico dominado, el siguiente nivel es escribir consultas que **escalen** y expresen patrones complejos: correlaciones con `join` y `lookup`, ventanas deslizantes, funciones reutilizables y parametrizadas, `materialize`, series temporales con `make-series` y detección de anomalías, análisis de grafos con `make-graph` y `graph-match`, y datos externos con `externaldata`.

También es el momento de entender **el costo de cada consulta** —filtrar temprano, usar el tiempo de ingesta, evitar operadores costosos— y las diferencias entre la búsqueda avanzada del portal de Defender, Log Analytics y el data lake. Un buen KQL avanzado es la diferencia entre una regla que funciona en el laboratorio y una que escala en producción.

**Qué vas a lograr**

- Optimizar consultas siguiendo las buenas prácticas oficiales.
- Construir funciones reutilizables y consultas parametrizadas.
- Aplicar series temporales, detección de anomalías y operadores de grafos.
- Adaptar consultas entre búsqueda avanzada, Log Analytics y el data lake.

> **Consejo Ninja.** Buenas prácticas de rendimiento: filtra temprano por tiempo, prefiere `has` a `contains` y `==` a `=~`, usa `materialize()` para expresiones `let` reutilizadas, `lookup` cuando la tabla derecha es pequeña y `hint.shufflekey` con alta cardinalidad ([buenas prácticas de KQL](https://learn.microsoft.com/en-us/kusto/query/best-practices?view=microsoft-fabric)).

> **Consejo Ninja.** Para anomalías, `series_decompose_anomalies` usa por defecto un umbral de 1,5 y estacionalidad autodetectada ([función](https://learn.microsoft.com/en-us/kusto/query/series-decompose-anomalies-function?view=microsoft-fabric)); para relaciones, `make-graph` crea grafos en memoria y `graph-match` busca patrones ([semántica de grafos](https://learn.microsoft.com/en-us/kusto/query/graph-semantics-overview?view=microsoft-fabric)).

**¿Tienes poco tiempo?**

- [Best practices for Kusto Query Language queries](https://learn.microsoft.com/en-us/kusto/query/best-practices?view=microsoft-fabric) · Documentación
- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta
- [(DxBP) Part 2 - Detection Engineering Best Practices: Performance, Readability & Maintenance](https://kqlquery.com/posts/dxbp-part2/) · Blog

### Documentación, cursos y credenciales

- [Best practices for Kusto Query Language queries](https://learn.microsoft.com/en-us/kusto/query/best-practices?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Tabla de buenas prácticas de rendimiento KQL: filtrar temprano, has vs contains, materialize(), lookup vs join, hints de shuffle/broadcast y parse vs extract.
- [Graph semantics overview (KQL)](https://learn.microsoft.com/en-us/kusto/query/graph-semantics-overview?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Explica la semántica de grafos en KQL: grafos transitorios con make-graph, grafos persistentes (modelos/snapshots) y consultas de patrones, rutas y caminos de ataque.
- [Advanced hunting with Microsoft Sentinel data in Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender) · Documentación · Oficial · Microsoft Learn. Cómo consultar datos de Sentinel junto con Defender XDR en advanced hunting, qué esperar con tablas de Defender transmitidas a Sentinel (retención, columnas, filtros de tiempo) y problemas conocidos.
- [Anomaly detection and forecasting (KQL time series)](https://learn.microsoft.com/en-us/kusto/query/anomaly-detection?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Explica el modelo de descomposición de series temporales en KQL para detectar anomalías y pronosticar con make-series, series_decompose y series_decompose_forecast.
- [Common scenarios for using KQL graph semantics](https://learn.microsoft.com/en-us/kusto/query/graph-scenarios?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Escenarios prácticos de make-graph/graph-match (redes sociales, logs, análisis de seguridad multidominio, series temporales) con consultas de ejemplo.
- [series_decompose_anomalies()](https://learn.microsoft.com/en-us/kusto/query/series-decompose-anomalies-function?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Referencia de la función de detección de anomalías por descomposición de series (estacionalidad, tendencia, umbral, método Tukey) con ejemplos.

### Webinars, videos y podcasts

- [Brewing KQL with Michael Crane: Governance, Auditability, MCP & AI for Sentinel (KQL Cafe, Feb 2026)](https://www.youtube.com/watch?v=3XexqnAowQ4) · Video · Comunidad · Alex Verboon, Gianni Castaldi, Michael Crane · KQL Cafe (YouTube) · feb 2026. Sesión sobre KQL para gobierno, auditoría y optimización de costes en Sentinel, tiering de logs, transformaciones DCR y mapeo de detecciones a MITRE/controles.
- [Accelerating Innovation with KQL - Henning Rauch](https://www.youtube.com/watch?v=Lc-TgF9Oklg) · Video · Empleado de Microsoft · Henning Rauch · YouTube - KQL Cafe · feb 2026. Charla de KustoCon sobre la evolución de la plataforma Kusto: grafos en KQL, soporte de GQL/openCypher, biblioteca de funciones de ciberseguridad, NL2KQL y MCP para Kusto.
- [Brewing KQL with Laurie Rhodes: Kustainer UI, KQL Graph, Sentinel Pricing & Copilot Governance (KQL Cafe, Apr 2026)](https://www.youtube.com/watch?v=Bb7wHCk047E) · Video · Comunidad · Alex Verboon, Gianni Castaldi, Laurie Rhodes · KQL Cafe (YouTube) · abr 2026. Demostración de un entorno KQL local (Kusto emulator), funciones de grafo KQL, cálculo de costes de Sentinel con la API de precios y gobierno de Copilot/agentes.

### Laboratorios, GitHub y herramientas

- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta · Comunidad · Nuevo · Ugur Koc y comunidad · kqlsearch.com · nov 2026. Buscador comunitario de consultas KQL para Sentinel, Defender y Azure Monitor, filtrable por tabla y autor, con aportes actualizados de la comunidad.
- [reprise99/Sentinel-Queries](https://github.com/reprise99/Sentinel-Queries) · GitHub · Empleado de Microsoft · Legado aún útil · Matt Zorich · GitHub (comunidad) · ene 2026. Colección clásica de consultas KQL para Sentinel con un README que enseña la anatomía de una consulta y fundamentos (tiempo, where, summarize, parse/split). *Nota:* Mayormente sin cambios desde hace años (algunas actualizaciones recientes); el autor fue MVP y hoy trabaja en Microsoft (GHOST)
- [Tutorial: Detect and analyze anomalies using KQL machine learning capabilities in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/kql-machine-learning-azure-monitor) · Laboratorio · Oficial · Microsoft Learn. Tutorial práctico con entorno demo: crear series con make-series sobre la tabla Usage, detectar anomalías y analizar causa raíz con diffpatterns.

### Comunidad: blogs, libros, newsletters y eventos

- [(DxBP) Part 2 - Detection Engineering Best Practices: Performance, Readability & Maintenance](https://kqlquery.com/posts/dxbp-part2/) · Blog · MVP · Nuevo · Bert-Jan Pals · kqlquery.com · 11 may 2026. Optimización de rendimiento y legibilidad de detecciones KQL: elección de operadores (has vs contains, in~), consumo de CPU, funciones integradas y mantenibilidad.
- [The Definitive Guide to KQL: Using Kusto Query Language for operations, defending, and threat hunting](https://www.microsoftpressstore.com/store/definitive-guide-to-kql-using-kusto-query-language-9780138293383) · Libro · Empleado de Microsoft · Mark Morowczynski; Rod Trent; Matthew Zorich · Microsoft Press · 14 may 2024. Libro de 480 páginas de Microsoft Press que cubre KQL desde fundamentos hasta casos avanzados de ciberseguridad, hunting y operaciones.
- [The KQL Grimoire - PART 1](https://www.linkedin.com/pulse/slims-elite-kql-detection-cyber-defense-tips-steven-lim-wujbc?tl=en) · Blog · MVP · Steven Lim · LinkedIn. Recopilación de consejos y consultas KQL de detección y defensa para Defender XDR y Sentinel.

**Manos a la obra**

1. `Laboratorio` Optimiza una consulta lenta aplicando las [buenas prácticas](https://learn.microsoft.com/en-us/kusto/query/best-practices?view=microsoft-fabric) y mide el antes y el después con las estadísticas de consulta.
2. `Laboratorio` Construye una detección de anomalías por hora en fallos de inicio de sesión con `make-series` y `series_decompose_anomalies`.
3. `Laboratorio` Modela rutas de movimiento lateral con `make-graph` y `graph-match` sobre eventos de inicio de sesión en dispositivos.
4. `Laboratorio` Convierte una consulta repetida en una función reutilizable con parámetros.

**¿Quieres profundizar?**

- [The Definitive Guide to KQL: Using Kusto Query Language for operations, defending, and threat hunting](https://www.microsoftpressstore.com/store/definitive-guide-to-kql-using-kusto-query-language-9780138293383) · Libro
- [reprise99/Sentinel-Queries](https://github.com/reprise99/Sentinel-Queries) · GitHub
- [The KQL Grimoire - PART 1](https://www.linkedin.com/pulse/slims-elite-kql-detection-cyber-defense-tips-steven-lim-wujbc?tl=en) · Blog
- [Accelerating Innovation with KQL - Henning Rauch](https://www.youtube.com/watch?v=Lc-TgF9Oklg) · Video

<a id="a3"></a>

## A3 · Casos de uso y soluciones

*L400 · ~5 h · Origen: Módulo 15 · Use cases and solutions*

Con conectores, reglas, playbooks y libros implementas **casos de uso**: el término SIEM para un paquete de contenido que detecta y responde a una amenaza concreta. Una **solución** agrupa casos de uso de un dominio —identidad, aplicaciones de negocio como SAP, Dynamics 365 o Power Platform, OT/IoT, Zero Trust, cumplimiento normativo— y se instala desde el Content hub en un solo paso.

Diseñar buenos casos de uso exige partir del riesgo del negocio y no de los datos disponibles. Este módulo enseña a diseñar, documentar y medir casos de uso, y a aprovechar las soluciones de Microsoft y de partners, con especial atención a escenarios críticos para organizaciones de la región como aplicaciones financieras y ERP.

**Qué vas a lograr**

- Diseñar un caso de uso a partir de un riesgo de negocio.
- Evaluar e instalar soluciones de dominio del Content hub.
- Conocer la solución de Sentinel para aplicaciones SAP y otras de negocio.

> **Atención.** Solución para SAP: el agente en contenedor se retiró el 14 de septiembre de 2026 y sus imágenes se eliminaron el 14 de octubre de 2026; la ruta es el conector sin agente basado en SAP Integration Suite ([migrar el agente SAP](https://learn.microsoft.com/en-us/azure/sentinel/sap/sap-agent-migrate)).

> **Novedad.** Aplicaciones de negocio (Power Platform, Dynamics 365 CE y F&O): el conector heredado de Dynamics 365 debe migrarse al de Dataverse ([soluciones de Business Apps](https://learn.microsoft.com/en-us/azure/sentinel/business-applications/solution-overview)). El [catálogo de soluciones](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-catalog) incluye paquetes de cumplimiento (NIST SP 800-53, PCI DSS, CMMC 2.0), Zero Trust y Defender for IoT.

**¿Tienes poco tiempo?**

- [Migrate to the Microsoft Sentinel agentless SAP data connector](https://learn.microsoft.com/en-us/azure/sentinel/sap/sap-agent-migrate) · Documentación

### Documentación, cursos y credenciales

- [Migrate to the Microsoft Sentinel agentless SAP data connector](https://learn.microsoft.com/en-us/azure/sentinel/sap/sap-agent-migrate) · Documentación · Oficial · Nuevo · Microsoft Learn · 17 sep 2026. Guía para migrar del agente SAP en contenedor al conector sin agente (SAP Integration Suite + Cloud Connector), con validación KQL y paridad de contenido.
- [Microsoft Sentinel solution for SAP applications: Deployment overview](https://learn.microsoft.com/en-us/azure/sentinel/sap/deployment-overview) · Documentación · Oficial · Microsoft Learn. Componentes (conector sin agente y contenido de seguridad) y flujo de despliegue con roles del equipo de seguridad y SAP BASIS.
- [What is the Microsoft Sentinel solution for Microsoft Business Apps?](https://learn.microsoft.com/en-us/azure/sentinel/business-applications/solution-overview) · Documentación · Oficial · Microsoft Learn. Solución para Power Platform, Dynamics 365 CE y Finance & Operations: conectores (PowerPlatformAdminActivity, DataverseActivity, FinanceOperationsActivity_CL), reglas, hunting y playbooks.
- [Microsoft Sentinel content hub catalog](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-catalog) · Documentación · Oficial · Microsoft Learn. Catálogo de soluciones de dominio del Content hub (Essentials de identidad, endpoint, red, DNS, UEBA, CMMC 2.0, NIST SP 800-53, PCI DSS, Defender for IoT, SOC Process Framework, etc.).
- [Connect Microsoft Power Platform and Microsoft Dynamics 365 Customer Engagement to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/business-applications/deploy-power-platform-solution) · Documentación · Oficial · Microsoft Learn. Despliegue de la solución Business Apps: prerrequisitos (auditoría Purview, DCR), conectores de Dataverse/Power Platform/Power Automate y validación con KQL.
- [Monitor Zero Trust (TIC 3.0) security architectures with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solution) · Documentación · Oficial · Microsoft Learn. Uso de la solución Zero Trust (TIC 3.0) con workbook, reglas y playbook que cruzan principios Zero Trust con el marco TIC 3.0 usando datos de Defender for Cloud.
- [Identifying and managing the lifecycle of deprecated solutions in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solution-deprecation) · Documentación · Oficial · Microsoft Learn · 28 abr 2026. Cómo identificar soluciones del Content hub marcadas como DEPRECATED, migrar a alternativas y desinstalar contenido para evitar duplicados.
- [Monitoring Azure Virtual Desktop with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/virtual-desktop/diagnostics-log-analytics) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: doc «Monitoring Azure Virtual Desktop with Microsoft Sentinel».

### Anuncios y blogs oficiales

- [Microsoft Teams hunting use cases](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/protecting-your-teams-with-azure-sentinel/ba-p/1265761) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: blog-oficial «Microsoft Teams hunting use cases».
- [Monitoring Zoom with Microsoft Sentinel](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/monitoring-zoom-with-azure-sentinel/ba-p/1341516) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: blog-oficial «Monitoring Zoom with Microsoft Sentinel».
- [Monitor Microsoft Intune](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/secure-working-from-home-deep-insights-at-enrolled-mem-assets/ba-p/1424255) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: blog-oficial «Monitor Microsoft Intune».
- [Monitor the software supply chain with Microsoft Sentinel](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/monitoring-the-software-supply-chain-with-azure-sentinel/ba-p/2176463) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: blog-oficial «Monitor the software supply chain with Microsoft Sentinel».

### Laboratorios, GitHub y herramientas

- [Monitoring AI Agents (paquetes de detección)](https://github.com/davidalonsod/Dalonso-Security-Repo/tree/main/Use%20Cases%20Threat%20Hunting/Monitoring%20AI%20Agents) · GitHub · Comunidad · Nuevo · David Alonso Domínguez · GitHub · oct 2026. Paquetes de reglas analíticas y consultas de caza para detectar amenazas a agentes de IA (prompt injection, secretos en herramientas, servidores MCP no aprobados).
- [Tutorial: Investigate and detect threats for IoT devices (Defender for IoT + Microsoft Sentinel)](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/iot-advanced-threat-monitoring) · Laboratorio · Oficial · Legado aún útil · Microsoft Learn. Tutorial para instalar la solución Defender for IoT en Sentinel, usar reglas OT/ICS (códigos ilegales, firmware, cambios en PLC), workbooks y playbooks. *Nota:* Escrito con navegación del portal de Azure y con la nota de preview del Content hub ya superada; validar pasos en Defender

### Comunidad: blogs, libros, newsletters y eventos

- [cloud-architekt.net (etiquetas)](https://www.cloud-architekt.net/tags) · Blog · MVP · Thomas Naunheim · cloud-architekt.net. Blog de referencia sobre seguridad de identidades (Entra, workload identities) y su detección, caza y automatización con Sentinel y Defender XDR.

**Manos a la obra**

1. `Laboratorio` Elige un riesgo de negocio de tu organización y diseña el caso de uso completo: fuentes, detecciones, respuesta, métricas y responsable.
2. `Laboratorio` Instala una solución de dominio del Content hub y documenta qué cubre y qué falta para tu caso.
3. `Solo producción` Si operas SAP, planifica la migración al conector sin agente ([migración SAP](https://learn.microsoft.com/en-us/azure/sentinel/sap/sap-agent-migrate)).

**¿Quieres profundizar?**

- [cloud-architekt.net (etiquetas)](https://www.cloud-architekt.net/tags) · Blog
- [Monitoring AI Agents (paquetes de detección)](https://github.com/davidalonsod/Dalonso-Security-Repo/tree/main/Use%20Cases%20Threat%20Hunting/Monitoring%20AI%20Agents) · GitHub
- [Tutorial: Investigate and detect threats for IoT devices (Defender for IoT + Microsoft Sentinel)](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/iot-advanced-threat-monitoring) · Laboratorio

<a id="a4"></a>

## A4 · Contenido como código y CI/CD

*L400 · ~8 h · Origen: Módulo 3 (CI/CD) y "Enable continuous deployment natively with Microsoft Sentinel repositories"*

Cuando administras muchas reglas, varios workspaces o varios clientes, la consola deja de escalar. Gestionar Sentinel **como código** —reglas, búsquedas, libros, playbooks y parsers en un repositorio, desplegados con pipelines— aporta control de versiones, revisión por pares, pruebas automáticas y despliegues repetibles.

Sentinel ofrece **repositorios** nativos conectados a GitHub y Azure DevOps, y la comunidad desarrolló marcos con ARM, Bicep, Terraform y PowerShell. Aquí aprenderás a elegir el enfoque, a estructurar un repositorio de detecciones, a probar reglas con simulaciones de ataque y a construir un ciclo de ingeniería de detecciones sostenible.

**Qué vas a lograr**

- Conectar un repositorio a Sentinel y desplegar contenido de forma continua.
- Desplegar Sentinel y su contenido con infraestructura como código.
- Diseñar un pipeline de ingeniería de detecciones con pruebas.

> **Novedad.** Sentinel Repositories llegó a disponibilidad general en marzo de 2026 y despliega reglas de analítica, reglas de automatización, búsquedas, parsers, playbooks, libros y, en vista previa desde julio de 2026, detecciones personalizadas con el recurso `Microsoft.Security/detectionRules` y la extensión Bicep MicrosoftSecurity ([contenido personalizado](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content)).

> **Atención.** Límites y requisitos: 5 conexiones de repositorio por workspace, rol Owner en el grupo de recursos del workspace y una cuenta del propio tenant (no se admiten invitados B2B ni acceso delegado). Lo editado en el portal se sobrescribe en el siguiente despliegue y borrar algo del repositorio no lo borra del workspace ([CI/CD](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd)).

> **Consejo Ninja.** Bicep es el formato recomendado; *smart deployments* despliega solo lo modificado. Parte del [repositorio de ejemplo oficial](https://github.com/SentinelCICD/RepositoriesSampleContent) y, si prefieres Terraform, del recurso `azurerm_sentinel_alert_rule_scheduled` ([Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/sentinel_alert_rule_scheduled)).

**¿Tienes poco tiempo?**

- [Deploy custom content from your repository](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd) · Documentación
- [Manage content as code with Microsoft Sentinel repositories](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación
- [Microsoft Sentinel Repositories: Manage Your SIEM Content Like a Pro (webinar)](https://www.youtube.com/watch?v=ffOg0mMgNLI) · Webinar

### Documentación, cursos y credenciales

- [Deploy custom content from your repository](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 ago 2026. Guía paso a paso para crear la conexión entre un workspace de Sentinel y un repositorio GitHub o Azure DevOps desde Content management > Repositories (Defender o Azure portal).
- [Manage content as code with Microsoft Sentinel repositories](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Documentación · Oficial · Nuevo · Microsoft Learn · 6 jul 2026. Explica cómo Sentinel Repositories convierte un repositorio GitHub/Azure DevOps en la fuente única de verdad (Bicep/ARM) para reglas, automatizaciones, hunting, parsers, playbooks, workbooks y reglas de detección personalizadas.
- [Customize repository deployments](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-deploy) · Documentación · Oficial · Microsoft Learn. Muestra cómo personalizar el workflow de GitHub Actions o el pipeline de Azure DevOps generado (triggers, carpeta raíz, smart deployments, orden de despliegue, exclusiones y archivos de parámetros por workspace).

### Webinars, videos y podcasts

- [Microsoft Sentinel Repositories: Manage Your SIEM Content Like a Pro (webinar)](https://www.youtube.com/watch?v=ffOg0mMgNLI) · Webinar · Empleado de Microsoft · Ofer Shezaf · Microsoft Security Community (YouTube) · 19 feb 2025. Webinar oficial sobre infraestructura y contenido SIEM como código, CI/CD con Repositories, demo de conexión y actualización de una detección, y anuncio del soporte Bicep.

### Laboratorios, GitHub y herramientas

- [SentinelCICD/RepositoriesSampleContent](https://github.com/SentinelCICD/RepositoriesSampleContent) · GitHub · Oficial · Equipo Microsoft Sentinel (SentinelEcoDevs) · GitHub (SentinelCICD). Repositorio de ejemplo oficial de Sentinel Repositories con contenido ARM/Bicep por tipo, scripts de conversión YAML/JSON a ARM y el archivo sentinel-deployment.config (prioridades, exclusiones y mapeo de parámetros por workspace).
- [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · Herramienta · Comunidad · Nuevo · Red Canary y comunidad · GitHub (Red Canary) · nov 2026. Biblioteca open source de pruebas atómicas mapeadas a MITRE ATT&CK para generar telemetría controlada y validar que las reglas de Sentinel/Defender disparan (pruebas de regresión de detecciones).
- [azurerm_sentinel_alert_rule_scheduled (Terraform AzureRM provider)](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/sentinel_alert_rule_scheduled) · Herramienta · Comunidad · Nuevo · HashiCorp / equipo Azure de Microsoft · HashiCorp Terraform Registry · oct 2026. Referencia del recurso Terraform para gestionar reglas analíticas programadas de Sentinel (consulta, severidad, entidades, agrupación, incidentes) junto con azurerm_sentinel_log_analytics_workspace_onboarding.
- [noodlemctwoodle/Sentinel-As-Code](https://github.com/noodlemctwoodle/Sentinel-As-Code) · GitHub · Comunidad · Nuevo · TobyG (noodlemctwoodle) · GitHub · oct 2026. Repositorio del framework Sentinel-As-Code con pipelines de despliegue, validación de PR (Pester, bicep-build, kql-validate), detección de drift, documentador y despliegue de custom detections a Defender XDR con OIDC.
- [f-bader/SentinelARConverter](https://github.com/f-bader/SentinelARConverter) · Herramienta · Comunidad · Fabian Bader (glueckkanja AG) · GitHub. Módulo PowerShell que convierte reglas analíticas de Sentinel entre YAML (formato del repo Azure-Sentinel) y plantillas ARM, con archivos de parámetros para sobrescribir propiedades y variables de consulta.

### Comunidad: blogs, libros, newsletters y eventos

- [Sentinel-As-Code: The 2026 Update](https://sentinel.blog/sentinel-as-code-the-2026-update/) · Blog · Comunidad · TobyG · sentinel.blog · 20 mar 2026. Describe un framework open source de cinco etapas (infra Bicep, Content Hub con control de versiones, siete tipos de contenido personalizado y reglas de detección de Defender XDR vía Graph) para GitHub Actions y Azure DevOps.
- ["Detection as code" out; "SIEM as code" in](https://www.linkedin.com/pulse/detection-code-out-siem-ofer-shezaf-05rwf/) · Blog · Empleado de Microsoft · Ofer Shezaf · LinkedIn · 21 feb 2025. Argumenta que en Sentinel se gestiona 'SIEM as code' (detecciones, workbooks, playbooks y despliegue) mediante CI/CD, desde Sentinel All-in-One hasta Sentinel Repositories.
- [Manage Security Content as Code with Microsoft Sentinel](https://charbelnemnom.com/manage-security-content-code-microsoft-sentinel/) · Blog · MVP · Legado aún útil · Charbel Nemnom · charbelnemnom.com · 21 mar 2025. Tutorial práctico que conecta Sentinel Repositories con Azure DevOps, despliega reglas analíticas, personaliza el pipeline y explica cómo actualizar reglas a versiones superiores, incluyendo soporte Bicep. *Nota:* Capturas en Azure portal; hoy la misma opción está en Defender > Microsoft Sentinel > Content management > Repositories (GA desde mar-2026)

**Manos a la obra**

1. `Laboratorio` Conecta un repositorio de GitHub a un workspace de laboratorio y despliega dos reglas en Bicep desde el [repositorio de ejemplo](https://github.com/SentinelCICD/RepositoriesSampleContent).
2. `Laboratorio` Modifica una regla en el repositorio, observa el despliegue inteligente y verifica el historial.
3. `Laboratorio` Despliega una detección personalizada como código con `Microsoft.Security/detectionRules` ([guía](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content)).
4. `Laboratorio` Agrega una prueba: ejecuta una simulación de ataque controlada en una VM de laboratorio y valida que la regla genere la alerta esperada.

**¿Quieres profundizar?**

- ["Detection as code" out; "SIEM as code" in](https://www.linkedin.com/pulse/detection-code-out-siem-ofer-shezaf-05rwf/) · Blog
- [Manage Security Content as Code with Microsoft Sentinel](https://charbelnemnom.com/manage-security-content-code-microsoft-sentinel/) · Blog
- [SentinelCICD/RepositoriesSampleContent](https://github.com/SentinelCICD/RepositoriesSampleContent) · GitHub
- [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · Herramienta

<a id="a5"></a>

## A5 · Conectores personalizados (CCF) y desarrollo de soluciones

*L400 · ~6 h · Origen: Módulo 4 (custom connectors) — ampliado*

Cuando tu fuente no tiene conector, lo construyes. El **Codeless Connector Framework (CCF)** permite crear conectores que consultan APIs REST, con paginación y autenticación, o que reciben datos, sin mantener código ni infraestructura propia, y es el camino recomendado por Microsoft frente a los conectores basados en Azure Functions. Cada conector CCF combina una definición de interfaz, reglas de recolección de datos, tablas y la configuración de sondeo.

Con la herramienta de empaquetado de soluciones puedes publicar conectores, reglas, libros y playbooks en el Content hub, ya sea para tu organización o como partner. Este módulo cubre el diseño, la construcción, la prueba y la publicación de conectores y soluciones.

**Qué vas a lograr**

- Construir un conector CCF de sondeo para una API REST.
- Planificar la migración de conectores basados en Azure Functions.
- Empaquetar y publicar una solución en el Content hub.

> **Qué cambió.** Codeless Connector Platform pasó a llamarse **Codeless Connector Framework (CCF)** en junio de 2025. Ofrece conectores de sondeo (pull) y de envío (push), totalmente SaaS, con monitoreo de salud; un conector de sondeo combina tabla, DCR, definición de interfaz y reglas de conexión ([crear un conector sin código](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-codeless-connector)).

> **Novedad.** CCF Push (vista previa) aprovisiona automáticamente la app de Entra, la DCR, el DCE y la tabla personalizada, aunque por ahora su despliegue requiere la experiencia del portal de Azure ([CCF Push](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-push-codeless-connector)). En abril de 2026 llegó el **agente constructor de conectores** para GitHub Copilot en VS Code ([connector builder agent](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-custom-connector-builder-agent)).

> **Novedad.** Las soluciones de plataforma (notebooks y jobs del lago, grafos personalizados, agentes) se empaquetan y publican como oferta en Microsoft Security Store ([soluciones de plataforma](https://learn.microsoft.com/en-us/azure/sentinel/isv/develop-notebook-platform-solutions)); las soluciones clásicas se empaquetan con la herramienta V3 ([empaquetado](https://learn.microsoft.com/en-us/azure/sentinel/isv/package-siem-solutions-overview)).

**¿Tienes poco tiempo?**

- [Build and publish Microsoft Sentinel SIEM solutions (integration guide)](https://learn.microsoft.com/en-us/azure/sentinel/isv/sentinel-integration-guide) · Documentación
- [Building Microsoft Sentinel Connectors in Minutes with the Sentinel Connector Builder Agent](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/building-microsoft-sentinel-connectors-in-minutes-with-the-sentinel-connector-bu/4544378) · Blog oficial
- [Azure-Sentinel/Tools/Create-Azure-Sentinel-Solution/V3 (README)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Create-Azure-Sentinel-Solution/V3/README.md) · GitHub

### Documentación, cursos y credenciales

- [Build and publish Microsoft Sentinel SIEM solutions (integration guide)](https://learn.microsoft.com/en-us/azure/sentinel/isv/sentinel-integration-guide) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Ciclo de vida completo para ISV: Partner Center, laboratorio de entrenamiento, construcción de conectores y contenido, validación local, PR al repositorio Azure-Sentinel, preview de al menos cuatro semanas y publicación en Content hub.
- [Create a pull codeless connector for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-codeless-connector) · Documentación · Oficial · Microsoft Learn. Introducción práctica al Codeless Connector Framework (CCF) para conectores pull: tabla de salida, DCR, interfaz y reglas de conexión empaquetadas en una plantilla ARM.
- [Package a SIEM solution for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/isv/package-siem-solutions-overview) · Documentación · Oficial · Microsoft Learn. Explica cómo usar la herramienta de empaquetado V3 (createSolutionV3.ps1) para generar mainTemplate.json, createUIDefinition.json y el .zip versionado, desplegarlo en un workspace de prueba y validar cada tipo de contenido.
- [Develop a notebook solution for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/isv/develop-notebook-platform-solutions) · Documentación · Oficial · Microsoft Learn. Guía ISV para construir, probar, programar como job, empaquetar (tipo SentinelLake) y publicar notebooks del data lake como oferta SaaS en Microsoft Security Store.
- [Microsoft Sentinel CCF push connectors (preview) - Getting started guide](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-push-codeless-connector) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 jun 2026. Guía de CCF Push: conectores dirigidos por eventos donde la aplicación del proveedor envía datos vía Logs Ingestion API y el despliegue crea automáticamente app de Entra, DCR, DCE, tabla _CL y roles. *Nota:* Cuatro artefactos (tabla, DCR, connectorDefinition, dataConnector kind=Push) empaquetados con createSolutionV3.ps1; el despliegue requiere por ahora la experiencia de Sentinel en el Azure portal
- [Build custom connectors with AI in Microsoft Sentinel (connector builder agent)](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-custom-connector-builder-agent) · Documentación · Oficial · Vista previa · Microsoft Learn. Uso del agente @sentinel /create-connector en GitHub Copilot (VS Code) para generar la configuración de polling, DCR, definición de conector y esquema de tabla de un conector CCF, validarlo y desplegarlo. *Nota:* Anunciado en abril 2026 (preview); requiere rol Microsoft Sentinel Contributor y modelo Claude Sonnet 4.5 o superior en Copilot
- [Package a Microsoft Sentinel graph and notebook solution](https://learn.microsoft.com/en-us/azure/sentinel/isv/package-publish-notebook-graph-solutions) · Documentación · Oficial · Microsoft Learn. Cómo estructurar el .zip SentinelLake (PackageManifest.yaml + carpeta de solución), verificarlo y crear la oferta SaaS en Partner Center para publicar en Security Store.
- [Publish a Microsoft Security Copilot agent or Microsoft Sentinel Data Lake Notebook Job in Security Store](https://learn.microsoft.com/en-us/security/store/partners/publish-a-security-copilot-agent-or-analytics-solution-in-security-store) · Documentación · Oficial · Microsoft Learn. Define la estructura del paquete (PackageManifest.yaml con tipos CopilotAgent, SentinelLake y AzureArmDeployment) para publicar agentes y notebooks como oferta SaaS en Security Store.
- [Develop custom graph platform solutions](https://learn.microsoft.com/en-us/azure/sentinel/isv/develop-custom-graph-platform-solutions) · Documentación · Oficial · Vista previa · Microsoft Learn. Guía para ISV/partners que construye, prueba, materializa (graph job), empaqueta y publica un grafo personalizado como oferta SaaS en Partner Center para el Microsoft Security Store. *Nota:* Un data lake por tenant; requiere extensión de Sentinel para VS Code, Jupyter, GitHub Copilot Business/Enterprise y Python 3.10+

### Anuncios y blogs oficiales

- [Building Microsoft Sentinel Connectors in Minutes with the Sentinel Connector Builder Agent](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/building-microsoft-sentinel-connectors-in-minutes-with-the-sentinel-connector-bu/4544378) · Blog oficial · Empleado de Microsoft · Nuevo · Robert_Moriarty · Microsoft Tech Community · 11 ago 2026. Laboratorio práctico que despliega una API mock de logs de red en Azure Functions y usa el agente constructor para generar, probar y desplegar un conector CCF pull hacia una tabla _CL.

### Laboratorios, GitHub y herramientas

- [Azure-Sentinel/Tools/Create-Azure-Sentinel-Solution/V3 (README)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Create-Azure-Sentinel-Solution/V3/README.md) · GitHub · Oficial · Nuevo · Equipo Microsoft Sentinel · GitHub (Azure) · oct 2026. Guía oficial de la herramienta de empaquetado de soluciones del Content hub: requisitos (PowerShell 7.1+, Node.js, powershell-yaml), archivo de entrada en la carpeta Data y generación del paquete.
- [Create Solution V3.1 (README-V3_1)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Create-Azure-Sentinel-Solution/V3/README-V3_1.md) · GitHub · Oficial · Equipo Microsoft Sentinel · GitHub (Azure). Documenta createSolutionV3_1.ps1: empaquetado de detecciones personalizadas de Defender XDR y workbooks de Defender, parámetros Deploy* por familia de contenido y uso local o en pipeline.

**Manos a la obra**

1. `Laboratorio` Construye un conector CCF de sondeo para una API REST pública de prueba, con paginación y autenticación ([crear conector](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-codeless-connector)).
2. `Laboratorio` Genera el mismo conector con el agente constructor desde Visual Studio Code y compara el resultado.
3. `Laboratorio` Empaqueta el conector, una regla y un libro como solución con la [herramienta V3](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Create-Azure-Sentinel-Solution/V3/README.md).

**¿Quieres profundizar?**

- [Create Solution V3.1 (README-V3_1)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Create-Azure-Sentinel-Solution/V3/README-V3_1.md) · GitHub

<a id="a6"></a>

## A6 · APIs y extensibilidad

*L400 · ~5 h · Origen: Módulo 20 · Extending and integrating using the Microsoft Sentinel APIs*

Como SIEM nativo en la nube, Sentinel es un sistema **API first**: todo lo que haces en el portal puede hacerse por API, y lo que está en la API también está en PowerShell. Si la palabra API te intimida, no te preocupes: la mayoría de los escenarios se resuelven con ejemplos listos.

La **API REST de Microsoft Sentinel** administra reglas, incidentes, watchlists y contenido; **Microsoft Graph Security** unifica incidentes, alertas, búsqueda avanzada y reglas de detección personalizadas de la plataforma; y las APIs de **Azure Monitor** consultan e ingieren datos. Con ellas integras Sentinel con tu ITSM, automatizas la administración y construyes tus propias herramientas.

**Qué vas a lograr**

- Elegir la API adecuada para cada tarea: Sentinel REST, Graph Security o Azure Monitor.
- Automatizar la administración con PowerShell y la CLI.
- Integrar incidentes y búsquedas con sistemas externos.

> **Atención.** Microsoft Graph retiró `/security/alerts` el 15 de octubre de 2026: migra a `alerts_v2` e `incidents` ([migración de alertas](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration)). Las APIs antiguas de búsqueda avanzada dejan de devolver datos el 1 de febrero de 2027: usa `runHuntingQuery`, que admite apuntar a un workspace ([runHuntingQuery](https://learn.microsoft.com/en-us/graph/api/security-security-runhuntingquery?view=graph-rest-1.0)).

> **Novedad.** La versión estable vigente de la API REST de Sentinel es 2025-09-01 ([API de incidentes](https://learn.microsoft.com/en-us/rest/api/securityinsights/incidents?view=rest-securityinsights-2025-09-01)); el módulo Az.SecurityInsights 4.0.0 (junio de 2026) trae cambios incompatibles ([PowerShell Gallery](https://www.powershellgallery.com/packages/Az.SecurityInsights/4.0.0)). Las detecciones personalizadas ya tienen API en Graph v1.0 ([detectionRule](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-1.0)).

**¿Tienes poco tiempo?**

- [detectionRule resource type - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-1.0) · Documentación

### Documentación, cursos y credenciales

- [detectionRule resource type - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-1.0) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Recurso de Microsoft Graph (security/rules/detectionRules) para gestionar por API las reglas de detección personalizadas de Defender XDR/Sentinel: consulta KQL, frecuencia, plantilla de alerta, entidades y acciones automáticas.
- [Migrate from the HTTP Data Collector API to the Logs ingestion API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Guía para migrar integraciones y tablas 'Custom table (classic)' del HTTP Data Collector API a la Logs ingestion API con DCE/DCR, transformaciones y RBAC por DCR, incluyendo el impacto en conectores de Sentinel que pasan a CCF.
- [Incidents - REST API (Azure Sentinel) 2025-09-01](https://learn.microsoft.com/en-us/rest/api/securityinsights/incidents?view=rest-securityinsights-2025-09-01) · Documentación · Oficial · Microsoft Learn. Referencia de la API REST de Sentinel (proveedor Microsoft.SecurityInsights) para incidentes: crear/actualizar, listar alertas, entidades y bookmarks, y ejecutar playbooks sobre un incidente.
- [Use the Microsoft Graph security API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn. Panorama de la API de seguridad de Microsoft Graph: advanced hunting (runHuntingQuery), custom detections, alertas e incidentes, TI, eDiscovery y cuotas de consulta (30 días, 100.000 filas, 45 llamadas/min, 50 MB).
- [security: runHuntingQuery - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/security-security-runhuntingquery?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn. Referencia de POST /security/runHuntingQuery para ejecutar KQL de advanced hunting por API, con parámetros Query, Timespan (ISO 8601) y workspaceId para apuntar a un workspace de Log Analytics concreto.
- [Migrate from legacy alerts to the alerts and incidents API](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Documentación · Oficial · Microsoft Learn. Guía de migración de /security/alerts (legado) a /security/alerts_v2 e /security/incidents con mapeo de campos, nuevos permisos (SecurityAlert.*, SecurityIncident.*) y más de 40 tipos de evidencia.
- [List detectionRule objects - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/security-rulesroot-list-detectionrules?view=graph-rest-1.0) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 nov 2026. Operación GET /security/rules/detectionRules en v1.0 con soporte de $filter/$orderby y ejemplo de regla con mapeo de entidades, tácticas MITRE y aislamiento automático de dispositivos.

### Anuncios y blogs oficiales

- [Also available by using PowerShell](https://techcommunity.microsoft.com/t5/azure-sentinel/new-year-new-official-azure-sentinel-powershell-module/ba-p/2025041) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 20 ('APIs y extensibilidad') del skill-up de Learn: blog-oficial «Also available by using PowerShell».
- [Microsoft Sentinel API 101](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/microsoft-sentinel-api-101/ba-p/1438928) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 20 ('APIs y extensibilidad') del skill-up de Learn: blog-oficial «Blog post».
- [Extending Microsoft Sentinel: APIs, integration, and management automation](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/extending-azure-sentinel-apis-integration-and-management/ba-p/1116885) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 20 ('APIs y extensibilidad') del skill-up de Learn: blog-oficial «Extending Microsoft Sentinel: APIs, integration, and management automation».

### Laboratorios, GitHub y herramientas

- [Az.SecurityInsights 4.0.0 (PowerShell Gallery)](https://www.powershellgallery.com/packages/Az.SecurityInsights/4.0.0) · Herramienta · Oficial · Nuevo · PowerShell Gallery · 2 jun 2026. Módulo oficial de Azure PowerShell con cmdlets *-AzSentinel* para reglas, automatizaciones, incidentes, bookmarks, conectores, entidades, TI y configuración de Sentinel.

**Manos a la obra**

1. `Laboratorio` Lista incidentes y actualiza uno con la API de Graph (`/security/incidents`) usando una app con permisos mínimos.
2. `Laboratorio` Ejecuta una consulta de búsqueda avanzada por API con `runHuntingQuery` apuntando a tu workspace.
3. `Solo producción` Inventaría integraciones que todavía usen `/security/alerts` o las APIs antiguas de búsqueda avanzada y planifica su migración.

**¿Quieres profundizar?**

- [Az.SecurityInsights 4.0.0 (PowerShell Gallery)](https://www.powershellgallery.com/packages/Az.SecurityInsights/4.0.0) · Herramienta

<a id="a7"></a>

## A7 · Notebooks, MSTICPy y machine learning

*L400 · ~8 h · Origen: Módulo 14 · Notebooks y Módulo 21 · Bring your own ML*

Los notebooks son la navaja suiza del analista avanzado: sirven para cazar, visualizar, investigar y automatizar análisis que KQL no expresa con comodidad, y funcionan como guías de investigación reproducibles. **MSTICPy**, la librería de Python del equipo de investigación de Microsoft, aporta conectores a Sentinel, enriquecimiento con inteligencia de amenazas, visualizaciones de línea de tiempo y análisis de anomalías.

Con el data lake de Sentinel, los **notebooks Spark** ejecutados desde Visual Studio Code abren una nueva etapa: análisis y machine learning sobre meses o años de datos, programables como trabajos que devuelven resultados al SIEM. El antiguo enfoque de traer tu propio modelo sobre Azure Machine Learning sigue siendo válido para casos específicos, pero ya no es el punto de entrada.

**Qué vas a lograr**

- Ejecutar notebooks de investigación y caza con MSTICPy.
- Analizar datos del data lake con notebooks Spark desde Visual Studio Code.
- Diseñar una detección basada en machine learning y programarla como trabajo.

> **Qué cambió.** El camino moderno son los notebooks Jupyter/PySpark de la extensión de Microsoft Sentinel para Visual Studio Code sobre el data lake, con trabajos programados ([notebooks del lago](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks)). Para clientes incorporados después del 23 de septiembre de 2026, Microsoft orienta notebooks, trabajos y grafos personalizados hacia Microsoft Fabric ([novedades](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)). Los notebooks en Azure Machine Learning y BYO-ML siguen documentados como enfoques heredados.

> **Atención.** MSTICPy sigue activo (versión 3.1.0 de septiembre de 2026), pero msticnb (notebooklets) fue archivado el 8 de julio de 2026 ([MSTICPy](https://github.com/microsoft/msticpy), [msticnb](https://github.com/microsoft/msticnb)).

> **Consejo Ninja.** Ejemplo canónico de detección con machine learning sobre el lago: el pipeline de password spray del repositorio oficial ([notebooks de ejemplo](https://github.com/microsoft/Sentinel/blob/main/data%20lake/notebooks/README.md)).

**¿Tienes poco tiempo?**

- [Run notebooks on the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks) · Documentación
- [microsoft/msticpy](https://github.com/microsoft/msticpy) · GitHub
- [microsoft/Sentinel - data lake notebooks (PasswordSpray, Graphs, Tutorials)](https://github.com/microsoft/Sentinel/blob/main/data%20lake/notebooks/README.md) · GitHub

### Documentación, cursos y credenciales

- [Run notebooks on the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks) · Documentación · Oficial · Microsoft Learn. Paso a paso para instalar la extensión Microsoft Sentinel en VS Code, explorar tablas del lake, crear notebooks con MicrosoftSentinelProvider (read_table/save_as_table), usar GitHub Copilot y programar notebook jobs.
- [MSTIC Jupyter and Python Security Tools (msticpy documentation)](https://msticpy.readthedocs.io/en/latest/) · Documentación · Empleado de Microsoft · Equipo MSTIC (Microsoft) · Read the Docs. Documentación oficial de MSTICPy: configuración msticpyconfig.yaml, proveedores de datos (Sentinel, Defender, Graph, Kusto), TI lookup, pivotes, análisis de series temporales, timelines y árboles de procesos.
- [Jupyter notebooks in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/notebooks) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 14 ('Notebooks') del skill-up de Learn: doc «Documentation».
- [Get started with Jupyter notebooks and MSTICPy in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/notebook-get-started) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 14 ago 2026. Tutorial del notebook 'Getting Started Guide For Microsoft Sentinel ML Notebooks' en Azure Machine Learning: configuración de MSTICPy, consultas a Sentinel y proveedores externos (VirusTotal, GeoLite2). *Nota:* Modelo clásico basado en Azure ML (Threat management > Notebooks); para análisis a gran escala Microsoft orienta a notebooks Spark del data lake/VS Code o Fabric

### Anuncios y blogs oficiales

- [Becoming a Microsoft Sentinel Notebooks Ninja - The Series!](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/becoming-a-microsoft-sentinel-notebooks-ninja---the-series/2693491) · Blog oficial · Empleado de Microsoft · Legado aún útil · Ninja original · Chi Nguyen (con Rod Trent) · Microsoft Tech Community – Microsoft Sentinel Blog · 27 ago 2021. Serie Ninja de notebooks (Partes 1, 2, 3, 3.5 y 4) que explica qué son los notebooks Jupyter en Sentinel, cuándo usarlos frente a playbooks y workbooks, y cierra con knowledge check y certificado (≥80%). *Nota:* Actualizado 28-oct-2022. Los notebooks pasaron de Azure ML a también Sentinel data lake (VS Code) en 2025; ver A7/A8. Registro de webinars vía aka.ms/SecurityWebinars. Mapa: -> A7
- [MSTICPy: Python defender tools](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/msticpy-python-defender-tools/ba-p/648929) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 14 ('Notebooks') del skill-up de Learn: blog-oficial «MSTICPy».
- [Build-your-own machine learning model detections in the AI-immersed Azure Sentinel SIEM](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/build-your-own-machine-learning-detections-in-the-ai-immersed/ba-p/1750920) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 21 ('Machine learning propio (BYO ML)') del skill-up de Learn: blog-oficial «Build-your-own machine learning model detections in the AI-immersed Azure Sentinel SIEM».
- [Creating your first Microsoft Sentinel Notebook](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/creating-your-first-microsoft-sentinel-notebook/2977745) · Blog oficial · Empleado de Microsoft · Legado aún útil · Pete Bryan · Microsoft Tech Community · 17 nov 2021. Parte 4 de la serie Notebooks Ninja: instalar paquetes, configurar MSTICPy, consultar Sentinel, enriquecer con fuentes externas y visualizar. *Nota:* Revisar versiones: MSTICPy actual es 3.x y requiere Python 3.10+

### Webinars, videos y podcasts

- [Build-your-own machine learning model](https://www.youtube.com/watch?v=QDIuvZbmUmc) · Video · Oficial · Legado aún útil · Ninja original · YouTube. Enlace del Módulo 21 ('Machine learning propio (BYO ML)') del skill-up de Learn: video «Build-your-own machine learning model».
- [Episode 05 - Building your Security Data Lake with Sentinel and Azure Data Explorer!](https://www.youtube.com/watch?v=QV1jFi7mbmo) · Video · MVP · Legado aún útil · Koos Goossens · AzSecurity - Learn by doing (YouTube). Sesión práctica sobre arquitectura multinivel de logs con Sentinel y Azure Data Explorer, parse-on-ingest vs parse-on-query y consulta de ADX desde Defender XDR. *Nota:* Patrón previo al data lake de Sentinel; hoy evaluar data lake tier, federación y Fabric antes de proponer ADX

### Laboratorios, GitHub y herramientas

- [microsoft/msticpy](https://github.com/microsoft/msticpy) · GitHub · Empleado de Microsoft · Nuevo · Ian Hellen y equipo MSTIC · GitHub (microsoft) · oct 2026. Repositorio de MSTICPy, librería Python para investigación y hunting en notebooks: proveedores de consulta (Sentinel, Defender XDR, Graph, Splunk), TI lookup, pivotes, análisis de anomalías y visualizaciones.
- [microsoft/Sentinel - data lake notebooks (PasswordSpray, Graphs, Tutorials)](https://github.com/microsoft/Sentinel/blob/main/data%20lake/notebooks/README.md) · GitHub · Oficial · Equipo Microsoft Sentinel · GitHub (microsoft). Colección modular de notebooks Spark para el data lake: pipeline de detección de password spray (backfill, rollups diarios, feature engineering), grafos y tutorial de inicio.
- [Azure/Azure-Sentinel-Notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub (Azure). Repositorio oficial de notebooks de Sentinel: guías de inicio, Entity Explorers, guided hunting/investigation, notebooks de ML y la carpeta sentinel-lake-notebooks para el data lake. *Nota:* La mayoría de notebooks están pensados para Azure ML + MSTICPy (actualizados a Python 3.10 en 2024); para el data lake usar la carpeta sentinel-lake-notebooks y la extensión de VS Code
- [Releases · microsoft/msticpy](https://github.com/microsoft/msticpy/releases) · GitHub · Empleado de Microsoft · Nuevo · Ian Hellen · GitHub (microsoft) · 21 sep 2026. Notas de versión de MSTICPy (3.0.x y 3.1.0) con cambios de compatibilidad, proveedores nuevos y correcciones de autenticación.
- [msticpy (README)](https://github.com/microsoft/msticpy/blob/main/README.md) · GitHub · Oficial · Microsoft MSTIC y contribuidores · GitHub - microsoft/msticpy. Librería Python de Microsoft para investigaciones y caza de amenazas en Jupyter (consultas a Sentinel, enriquecimiento con TI, visualizaciones).
- [Azure-Sentinel-Notebooks/sentinel-lake-notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks/tree/master/sentinel-lake-notebooks) · GitHub · Oficial · GitHub (Azure). Notebooks para el entorno de notebooks del data lake (MicrosoftSentinelProvider), incluido el notebook de hunting retroactivo (RetroHunting) contra IOCs históricos.
- [ashwin-patil (repositorios: blue-teaming-with-kql, threat-hunting-with-notebooks)](https://github.com/ashwin-patil?tab=repositories) · GitHub · Empleado de Microsoft · Ashwin Patil · GitHub. Repositorios de un investigador de MSTIC con consultas KQL de blue team y notebooks de caza de amenazas.

**Manos a la obra**

1. `Laboratorio` Instala la extensión de Microsoft Sentinel en Visual Studio Code y ejecuta un notebook PySpark sobre una tabla del lago ([notebooks](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks)).
2. `Laboratorio` Programa el notebook como trabajo y escribe su resultado en una tabla consumible por una regla.
3. `Laboratorio` Ejecuta un notebook de investigación con MSTICPy para enriquecer IP con inteligencia de amenazas.

**¿Quieres profundizar?**

- [Releases · microsoft/msticpy](https://github.com/microsoft/msticpy/releases) · GitHub
- [Azure/Azure-Sentinel-Notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks) · GitHub
- [msticpy (README)](https://github.com/microsoft/msticpy/blob/main/README.md) · GitHub
- [Azure-Sentinel-Notebooks/sentinel-lake-notebooks](https://github.com/Azure/Azure-Sentinel-Notebooks/tree/master/sentinel-lake-notebooks) · GitHub

<a id="a8"></a>

## A8 · Data lake, graph y trabajos de Sentinel

*L400 · ~8 h · Origen: Nuevo (sucede a Basic/Archive logs, ADX para retención y BYO-ML)*

El **data lake de Sentinel** cambia la economía del SIEM: separa almacenamiento y cómputo, conserva datos durante años a bajo costo en un formato abierto y los expone a KQL, a notebooks Spark y a agentes de IA. Los datos del nivel de analítica se replican al lago, y los **trabajos** programados devuelven resultados al nivel de analítica cuando una detección o una investigación los necesita.

**Sentinel graph** modela relaciones entre usuarios, dispositivos, recursos, permisos y actividad para responder preguntas de alcance, caminos de ataque y radio de impacto que las tablas por sí solas no responden. Este módulo cubre arquitectura, onboarding, consultas, trabajos, costos y casos de uso del lago y del graph, que son además el contexto sobre el que trabajan los agentes del nivel experto.

**Qué vas a lograr**

- Explicar la arquitectura del data lake y su relación con el nivel de analítica.
- Consultar el lago con KQL y programar trabajos que alimenten detecciones.
- Comprender el modelo de costos del lago.
- Usar Sentinel graph para análisis de alcance y caminos de ataque.

> **Novedad.** Los **KQL jobs** sobre el lago escriben en tablas `_KQL_CL` del nivel de analítica y requieren Log Analytics Contributor para la identidad administrada del lago; la latencia típica ronda los 15 minutos ([KQL jobs](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs)).

> **Novedad.** **Sentinel graph** alimenta el radio de impacto en el gráfico de incidentes, el hunting graph de Defender y grafos de riesgo de datos en Purview; si ya tienes el lago, hunting graph y blast radius se aprovisionan al entrar al portal ([Sentinel graph](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview)). Los grafos personalizados (vista previa desde abril de 2026) se crean en notebooks, se consultan con GQL y se materializan con graph jobs: bajo demanda duran 30 días y los programados se reconstruyen ([grafos personalizados](https://learn.microsoft.com/en-us/azure/sentinel/datalake/custom-graphs-overview)).

> **Novedad.** La federación de datos (vista previa) consulta Databricks, ADLS Gen2 y Fabric en formato Delta Parquet sin copiar los datos ([federación](https://learn.microsoft.com/en-us/azure/sentinel/datalake/data-federation-overview)).

> **Atención.** Medidores del lago y del graph en la [página de precios](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/): ingesta, procesamiento, consulta por GB analizado, almacenamiento, cómputo de notebooks y cómputo de graph por hora. Define límites y alertas de consumo antes de abrir notebooks a todo el equipo.

**¿Tienes poco tiempo?**

- [What is Microsoft Sentinel data lake?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview) · Documentación
- [What is Microsoft Sentinel graph?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview) · Documentación
- [Microsoft Sentinel graph | Unlocking Graph-based Security and Analysis](https://www.youtube.com/watch?v=U6rh0UnXZvg) · Webinar

### Documentación, cursos y credenciales

- [What is Microsoft Sentinel graph?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Explica Sentinel graph como capacidad unificada de análisis de grafos que alimenta blast radius en el incident graph, hunting graph en Defender y grafos de riesgo de datos en Purview, además de grafos personalizados.
- [Set up connectors for the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-connectors) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Configuración de retención y tiering por conector (analytics + espejo o solo lake), datos XDR, tablas personalizadas, tablas Auxiliary e ingesta directa al lake.
- [What is Microsoft Sentinel data lake?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview) · Documentación · Oficial · Microsoft Learn. Describe el data lake de Sentinel: almacenamiento Parquet de copia única, separación de cómputo y almacenamiento, niveles analytics y data lake, retención hasta 12 años, exploración KQL, jobs de promoción y notebooks.
- [Manage data tiers and retention in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview) · Documentación · Oficial · Microsoft Learn. Explica la gestión de tablas en el portal de Defender: retención analítica (30 días por defecto, hasta 2 años), retención total en el lake (hasta 12 años), nivel solo-lake y tratamiento de tablas XDR.
- [Create KQL jobs in the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs) · Documentación · Oficial · Microsoft Learn. Cómo crear jobs KQL únicos o programados sobre el lake y tablas federadas para promover resultados al nivel analytics (_KQL_CL) o a tablas del lake (_KQL), con plantillas integradas de baselining y hunting.
- [Jupyter notebooks and the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks-overview) · Documentación · Oficial · Microsoft Learn. Visión general de los notebooks PySpark de la extensión de Sentinel para VS Code: escenarios (baselines de sign-in fallidos, rutas a datos sensibles, scoring de riesgo), escritura al lake/analytics con save_as_table y jobs programados.
- [What is Microsoft Sentinel's support for Model Context Protocol (MCP)?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-overview) · Documentación · Oficial · Microsoft Learn. Introduce el servidor MCP alojado de Sentinel y sus colecciones de herramientas para explorar el data lake, analizar entidades, triage y crear agentes en lenguaje natural.
- [Microsoft Sentinel Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) · Documentación · Oficial · Microsoft Security. Página oficial de precios con niveles de análisis (PAYG y compromisos), medidores del data lake y del graph, nivel promocional de 50 GB y el beneficio de hasta 5 MB/usuario/día de ingesta gratuita.
- [Custom Graph overview (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/custom-graphs-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 7 ago 2026. Describe los grafos personalizados (potenciados por Fabric) construidos con notebooks PySpark y la librería sentinel_graph, consultados con GQL y materializados con graph jobs bajo demanda (30 días) o programados. *Nota:* Anunciado en abril 2026; escenarios de ejemplo: kill chain de phishing, beaconing DNS C2, cadenas de comportamientos MITRE y escalamiento OAuth; facturado con el medidor de Sentinel graph
- [Explore Microsoft Sentinel data lake with data exploration collection (MCP)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-data-exploration-tool) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 jul 2026. Herramientas MCP search_tables, ejecución de KQL sobre el lake, listado de workspaces, entity analyzer y herramientas de grafo (preview) sobre grafos de exposición, hunting y riesgo de datos. *Nota:* Endpoint roles mínimos Security Reader/Operator/Administrator; el entity analyzer consume SCU (Security Copilot Contributor) y las herramientas de grafo usan el medidor de graph
- [Get started with custom graphs in Microsoft Sentinel (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/create-custom-graphs) · Documentación · Oficial · Vista previa · Microsoft Learn. Tutorial para modelar un grafo de pertenencias anidadas de grupos de Entra en un notebook de la extensión de Sentinel para VS Code, persistirlo con un graph job y gestionarlo. *Nota:* Usuarios restringidos por Sentinel scoping no pueden crear grafos; la sesión Spark tarda ~5 min en iniciar
- [Visualize graphs in Microsoft Sentinel (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/graph-visualization) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo consultar y visualizar grafos personalizados materializados en Microsoft Sentinel > Graphs del portal de Defender usando GQL, vista de esquema, tabla y recorrido interactivo. *Nota:* Las consultas se facturan con el medidor de Sentinel graph
- [AI-assisted custom graph authoring in Microsoft Sentinel (preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/create-graphs-with-ai) · Documentación · Oficial · Vista previa · Microsoft Learn. Muestra cómo usar GitHub Copilot en VS Code con el ayudante @sentinel /graph-authoring para generar, depurar y explicar notebooks de grafos personalizados. *Nota:* Requiere plan GitHub Copilot Business o Enterprise
- [Data federation overview in Microsoft Sentinel data lake (Preview)](https://learn.microsoft.com/en-us/azure/sentinel/datalake/data-federation-overview) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe cómo federar tablas Delta Parquet de Azure Databricks, ADLS Gen2 y Microsoft Fabric para consultarlas con KQL, notebooks o MCP sin moverlas al lake. *Nota:* Federación unidireccional; requiere origen público (sin private endpoints), service principal y Key Vault

### Anuncios y blogs oficiales

- [Microsoft Sentinel data lake is now generally available](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342) · Blog oficial · Empleado de Microsoft · vkokkengada · Microsoft Tech Community - Microsoft Security Community Blog · 30 sep 2025. Anuncia la disponibilidad general del data lake de Sentinel y presenta casos de uso (investigaciones de largo plazo, líneas base de comportamiento, enriquecimiento, hunting retrospectivo).
- [Empowering defenders in the era of agentic AI with Microsoft Sentinel](https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 30 sep 2025. Anuncio ejecutivo de Sentinel como plataforma agéntica: GA del data lake y vista previa pública de Sentinel graph y del servidor MCP, más el constructor de agentes sin código de Security Copilot.
- [What's new in Microsoft Sentinel: June 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-june-2026/4531902) · Blog oficial · Empleado de Microsoft · Nuevo · TomerBrand · Microsoft Tech Community - Microsoft Sentinel Blog · 30 jun 2026. Resumen mensual que anuncia la serie de seis blogs sobre la transición de Sentinel al portal de Defender, ampliaciones de ASIM y herramientas de grafo en el servidor MCP.

### Webinars, videos y podcasts

- [Microsoft Sentinel data lake (playlist)](https://www.youtube.com/playlist?list=PL3ZTgFEc7LyvM-OlDTB8BDV_aARfmBMG9) · Video · Oficial · Microsoft Security (YouTube). Serie de 8 videos cortos con demos: introducción al lake, consultas KQL, KQL jobs, notebooks, gestión de costos, Sentinel graph y servidor MCP.
- [Microsoft Sentinel graph | Unlocking Graph-based Security and Analysis](https://www.youtube.com/watch?v=U6rh0UnXZvg) · Webinar · Oficial · Sourin Paul, Shirley Kochavi · YouTube – Microsoft Security Community · 11 feb 2026. Webinar sobre hunting graph, blast radius y grafos personalizados (efímeros vs. materializados) creados desde VS Code y notebooks, con demo de gestión de acceso privilegiado.
- [Unlocking Security Context with Microsoft Sentinel Graph](https://www.youtube.com/watch?v=MVyHJR6TJjU) · Video · Oficial · Yaniv Shasha · YouTube – Microsoft Security Community. Explica cómo Sentinel graph convierte tablas fragmentadas en un grafo de conocimiento de seguridad y cómo extenderlo con grafos propios (empleados, activos, CVE, tickets).
- [New data lake in Microsoft Sentinel (Microsoft Mechanics)](https://www.youtube.com/watch?v=4CUK-eJBNI0) · Video · Empleado de Microsoft · Vandana Mahtani · Microsoft Mechanics (YouTube). Demo de ~9 minutos del data lake de Sentinel: gestión de tablas, niveles analytics/data lake, exploración, hunting avanzado, jobs programados y notebooks para ML.
- [Inside Microsoft Sentinel: Data Lake, Graph, and AI with Javier Soriano (Talking Security S6E7)](https://rss.com/podcasts/talking-security/2354020/) · Podcast · Empleado de Microsoft · Frans Oudendorp y Pouyan Khabazi con Javier Soriano · Talking Security (RSS.com) · 11 dic 2025. Entrevista con el PM principal de Sentinel sobre la evolución del producto, el data lake, Sentinel graph, MCP y el futuro de la seguridad agéntica.

### Comunidad: blogs, libros, newsletters y eventos

- [A Little Slice of KQL Jobs in the Sentinel data lake](https://www.linkedin.com/pulse/little-slice-kql-jobs-sentinel-data-lake-jon-shectman-xuomc/) · Blog · Empleado de Microsoft · Jon Shectman (con Clive Watson) · LinkedIn · 30 oct 2025. Compara KQL jobs, summary rules y search jobs y muestra dos casos (IPs de password spray y línea base geográfica por usuario) que promueven resultados del data lake al nivel de análisis.
- [Microsoft Sentinel Data Lake: Nine Tips to Help You Swim Faster](https://www.quorumcyber.com/insights/microsoft-sentinel-data-lake-nine-tips-to-help-you-swim-faster/) · Blog · MVP · Legado aún útil · Clive Watson · Quorum Cyber. Nueve consejos prácticos sobre el data lake: workspace por defecto, retención con datos espejados, permisos para jobs, costos de promoción, cambios de nivel y facturación. *Nota:* Escrito durante la preview; desde sep-2026 el data lake viene integrado en el onboarding de Sentinel
- [Thinking in Graphs: Why Microsoft Sentinel Graph Changes the Security Game](https://cyclotron.com/post/thinking-in-graphs-why-microsoft-sentinel-graph-changes-the-security-game/) · Blog · Comunidad · Gary Bushey (Cyclotron) · Cyclotron. Explica el cambio de pensar en tablas a pensar en grafos con Sentinel graph para análisis de rutas de ataque y radio de impacto.
- [Reinvent the SIEM with Microsoft Sentinel data lake (WPNinja Summit 2025)](https://wpninjas25.sched.com/event/28dDP/reinvent-the-siem-with-microsoft-sentinel-data-lake) · Evento · Empleado de Microsoft · Legado aún útil · Javier Soriano · WPNinja Summit. Sesión de conferencia del PM de Sentinel sobre cómo el data lake redefine el SIEM. *Nota:* Ficha del evento; verificar si hay grabación disponible

**Manos a la obra**

1. `Laboratorio parcial` Consulta 90 días de una tabla del lago desde la búsqueda avanzada y estima su costo con el medidor de consulta.
2. `Laboratorio` Crea un KQL job programado que resuma conexiones raras y alimente una regla de detección ([KQL jobs](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs)).
3. `Laboratorio parcial` Explora el radio de impacto de un usuario comprometido en el gráfico de incidentes y en el hunting graph.
4. `Laboratorio parcial` Opcional: crea un grafo personalizado en un notebook y materialízalo con un graph job.

**¿Quieres profundizar?**

- [A Little Slice of KQL Jobs in the Sentinel data lake](https://www.linkedin.com/pulse/little-slice-kql-jobs-sentinel-data-lake-jon-shectman-xuomc/) · Blog
- [New data lake in Microsoft Sentinel (Microsoft Mechanics)](https://www.youtube.com/watch?v=4CUK-eJBNI0) · Video
- [Inside Microsoft Sentinel: Data Lake, Graph, and AI with Javier Soriano (Talking Security S6E7)](https://rss.com/podcasts/talking-security/2354020/) · Podcast
- [Microsoft Sentinel Data Lake: Nine Tips to Help You Swim Faster](https://www.quorumcyber.com/insights/microsoft-sentinel-data-lake-nine-tips-to-help-you-swim-faster/) · Blog

<a id="a9"></a>

## A9 · Multi-inquilino y MSSP

*L400 · ~5 h · Origen: Módulos 2 y 3 (MSSP) y Microsoft Sentinel Technical Playbook for MSSPs*

Un SOC global o un proveedor de servicios gestionados (MSSP) opera muchos workspaces y tenants como si fueran uno. **Azure Lighthouse** delega acceso entre tenants; la **gestión multi-inquilino** del portal de Defender unifica incidentes y búsquedas; el **workspace manager** y la gestión de contenido distribuido replican contenido de forma controlada; y las consultas y reglas entre workspaces correlacionan datos.

Este módulo cubre los patrones técnicos y de gobierno del modelo de servicio: incorporación de clientes, delegación con mínimo privilegio (incluido GDAP), segmentación de acceso, distribución de contenido, facturación y protección de la propiedad intelectual del proveedor.

**Qué vas a lograr**

- Diseñar el acceso entre tenants con Azure Lighthouse, GDAP y la gestión multi-inquilino de Defender.
- Distribuir contenido entre workspaces y tenants de forma controlada.
- Proteger la propiedad intelectual del MSSP.

> **Qué cambió.** El antiguo Technical Playbook for MSSPs queda reemplazado en la práctica por la guía de implementación para MSSP del portal de Defender (actualizada en septiembre de 2026): delegación con B2B, GDAP y Lighthouse, distribución de contenido, patrones de CI/CD y operación multi-inquilino ([guía MSSP](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security)).

> **Atención.** Sin Azure Lighthouse, la gestión multi-inquilino solo consulta el workspace principal de cada tenant ([MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-overview)); con Lighthouse solo no se pueden desplegar conectores en un workspace gestionado: también hace falta GDAP ([proveedores de servicios](https://learn.microsoft.com/en-us/azure/sentinel/multiple-tenants-service-providers)).

> **Consejo Ninja.** Las reglas que consultan varios workspaces admiten hasta 20 por consulta, aunque se recomiendan 5 o menos ([extender entre workspaces](https://learn.microsoft.com/en-us/azure/sentinel/extend-sentinel-across-workspaces-tenants)). Los perfiles de distribución copian detecciones, reglas, libros y funciones, con hasta 9.500 elementos por publicación ([distribución de contenido](https://learn.microsoft.com/en-us/defender-xdr/mto-distribution-profiles)). Para proteger tu propiedad intelectual, revisa [este artículo](https://learn.microsoft.com/en-us/azure/sentinel/mssp-protect-intellectual-property).

> **Novedad.** Según el blog de Sentinel de octubre de 2026 citado por la comunidad, el acceso delegado entre tenants pasó a disponibilidad general; confirma el estado vigente en el [blog de Sentinel](https://techcommunity.microsoft.com/category/microsoft-sentinel/blog/microsoftsentinelblog) antes de diseñar.

**¿Tienes poco tiempo?**

- [Microsoft Defender portal implementation guide for Managed Security Service Providers (MSSPs)](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security) · Documentación
- [What's new in Microsoft Sentinel: September 2026](https://techcommunity.microsoft.com/blog/MicrosoftSentinelBlog/what%E2%80%99s-new-in-microsoft-sentinel-september-2026/4560902) · Blog oficial

### Documentación, cursos y credenciales

- [Microsoft Defender portal implementation guide for Managed Security Service Providers (MSSPs)](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Guía oficial para MSSP en el portal de Defender: preparar el entorno y la delegación multitenant, gestionar contenido una vez y distribuirlo, y operar incidentes y hunting entre clientes.
- [Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Vista unificada multi-tenant del portal de Defender para incidentes, alertas, casos, hunting avanzado y reglas de detección personalizadas, incluyendo workspaces de Sentinel incorporados.
- [Microsoft Defender unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac) · Documentación · Oficial · Microsoft Learn. Explica el modelo URBAC del portal de Defender, que ya admite Sentinel para workspaces incorporados: las asignaciones se sincronizan con Azure RBAC y URBAC pasa a ser la fuente de permisos al activarse.
- [Manage Microsoft Sentinel workspaces at scale (Azure Lighthouse)](https://learn.microsoft.com/en-us/azure/lighthouse/how-to/manage-sentinel-workspaces) · Documentación · Oficial · Microsoft Learn (Azure Lighthouse). Modelo MSSP con Azure Lighthouse: workspaces en cada tenant cliente gestionados desde el tenant del proveedor, roles delegados, consultas y workbooks entre tenants y protección de propiedad intelectual.
- [Content distribution in multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-distribution-profiles) · Documentación · Oficial · Microsoft Learn. Explica cómo crear perfiles de distribución para copiar desde un tenant fuente a tenants destino reglas de detección personalizadas, políticas de endpoint, reglas analíticas, reglas de automatización, workbooks y parsers/funciones de Sentinel.
- [Create custom roles with Microsoft Defender unified RBAC](https://learn.microsoft.com/en-us/defender-xdr/create-custom-rbac-roles) · Documentación · Oficial · Microsoft Learn. Cómo crear roles personalizados de unified RBAC (operaciones, postura, autorización y Data operations para el data lake) y asignarlos a usuarios, grupos o grupos de tenants remotos GDAP con alcance por fuente y colección de datos.
- [Fetch Microsoft Defender alerts from an MSSP customer tenant](https://learn.microsoft.com/en-us/defender-endpoint/api/fetch-alerts-mssp) · Documentación · Oficial · Microsoft Learn. Cómo un MSSP obtiene alertas de cada tenant cliente mediante una app multitenant con SecurityAlert.Read.All y consentimiento de administrador por tenant, o vía integraciones SIEM soportadas.
- [Centrally manage multiple Microsoft Sentinel workspaces with workspace manager (Preview)](https://learn.microsoft.com/en-us/azure/sentinel/workspace-manager) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 jul 2026. Publica contenido (reglas, automatizaciones, parsers, hunting, workbooks) desde un workspace central a workspaces miembro con topologías direct-link, co-gestión y N-tier. *Nota:* Aplica solo a Sentinel en el portal de Azure; en el portal de Defender usar gestión multi-tenant y distribución de contenido. Con fin de soporte del portal de Azure (31-mar-2027) tiene vida limitada
- [Manage multiple tenants in Microsoft Sentinel as an MSSP](https://learn.microsoft.com/en-us/azure/sentinel/multiple-tenants-service-providers) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 8 ago 2026. Explica cómo un MSSP gestiona workspaces de clientes con Azure Lighthouse y remite a la guía del portal de Defender para MSSP. *Nota:* Incluye aviso de retiro del Azure portal (31-mar-2027) y que no se pueden desplegar conectores desde un workspace gestionado solo con Lighthouse: también se requiere GDAP

### Anuncios y blogs oficiales

- [What's new in Microsoft Sentinel: September 2026](https://techcommunity.microsoft.com/blog/MicrosoftSentinelBlog/what%E2%80%99s-new-in-microsoft-sentinel-september-2026/4560902) · Blog oficial · Empleado de Microsoft · Nuevo · vkokkengada · Microsoft Tech Community - Microsoft Sentinel Blog · 30 sep 2026. Resumen mensual oficial: Case Management en Defender (preview pública desde el 23-sep-2026), roles personalizados URBAC para GDAP, conectores CCF multi-cuenta y más de 500 conectores de datos.
- [How Granular Delegated Admin Privileges (GDAP) allows Sentinel customers to delegate access](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/how-granular-delegated-admin-privileges-gdap-allows-sentinel-customers-to-delega/4503123) · Blog oficial · Empleado de Microsoft · Vista previa · Yossi Basha · Microsoft Tech Community - Microsoft Sentinel Blog · 20 mar 2026. Explica la extensión de GDAP a clientes no-CSP para delegar acceso a Sentinel y Defender desde el portal de Defender mediante un handshake de tres pasos entre tenant gobernante y gobernado. *Nota:* Vista previa pública desde el 16-abr-2026 (actualizado esa fecha). Alternativa/complemento a Azure Lighthouse para MSSP y organizaciones multi-tenant

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Sentinel Central Workbook v2.0](https://www.linkedin.com/pulse/microsoft-sentinel-central-workbook-v20-clive-watson/) · Blog · MVP · Legado aún útil · Clive Watson · LinkedIn · 16 nov 2021. Workbook para MSSP y organizaciones multi-tenant que centraliza incidentes, hunting entre workspaces, query packs y búsquedas guardadas. *Nota:* Existe una versión posterior (v2.1.2, oct-2023); hoy complementar con multi-tenant en el portal Defender y acceso delegado GA (oct-2026)

**Manos a la obra**

1. `Laboratorio parcial` Configura la gestión multi-inquilino de Defender con dos tenants de laboratorio y revisa la cola de incidentes unificada ([MTO](https://learn.microsoft.com/en-us/defender-xdr/mto-overview)).
2. `Laboratorio parcial` Crea un perfil de distribución de contenido y publica dos reglas en ambos tenants.
3. `Laboratorio` Diseña la matriz de delegación (B2B, GDAP, Lighthouse) para un MSSP con tres clientes y justifica cada elección.

<a id="reto-avanzado"></a>

## Reto del nivel

**Contenido como código sobre el lago.** Publica en un repositorio tres reglas, un parser ASIM y un libro con despliegue automático; crea un KQL job sobre una tabla del lago que alimente una de las reglas, un notebook que genere una tabla de enriquecimiento y una automatización por API que actualice incidentes. Documenta pruebas, dueños y criterios de retiro de cada pieza.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué capacidad tienen las detecciones personalizadas y NO las reglas de analítica?
   - a) Supresión de alertas
   - b) Acciones de respuesta nativas de Defender XDR
   - c) Alertas sin incidente
   - d) Agrupación personalizada de alertas

2. ¿Qué parámetro de un parser ASIM agrupa los campos no normalizados en AdditionalFields?
   - a) extra
   - b) pack
   - c) raw
   - d) bag

3. Según la guía actual para desarrollar parsers ASIM, ¿qué operador está prohibido?
   - a) where
   - b) project-rename
   - c) mv-expand
   - d) extend

4. En series_decompose_anomalies, ¿cuáles son el umbral y la estacionalidad por defecto?
   - a) 3,0 y 0
   - b) 1,5 y autodetección
   - c) 2,5 y 24
   - d) 1,0 y 168

5. ¿Qué recurso usa Sentinel Repositories para desplegar detecciones personalizadas como código?
   - a) Microsoft.SecurityInsights/alertRules con ARM
   - b) Microsoft.Security/detectionRules con la extensión Bicep MicrosoftSecurity
   - c) Microsoft.Insights/scheduledQueryRules con Terraform
   - d) Microsoft.OperationalInsights/savedSearches

6. ¿Cuántas conexiones de repositorio admite un workspace de Sentinel?
   - a) 1
   - b) 3
   - c) 5
   - d) 10

7. Un ISV quiere enviar eventos en tiempo casi real sin exponer una API para sondeo. ¿Qué modelo conviene?
   - a) CCF de sondeo
   - b) CCF Push sobre la API de ingesta de logs
   - c) HTTP Data Collector API desde una Azure Function
   - d) Conector Logstash

8. Una integración de tickets usa GET /security/alerts de Microsoft Graph. ¿Qué corresponde hacer?
   - a) Nada, la API es estable
   - b) Migrar a /security/alerts_v2 e /security/incidents
   - c) Migrar a la API de Defender for Endpoint
   - d) Volver a Az.SecurityInsights 1.x

9. Un KQL job crea una tabla en el nivel de analítica. ¿Qué sufijo recibe y qué permiso adicional requiere?
   - a) _CL; Sentinel Contributor para el usuario
   - b) _KQL_CL; Log Analytics Contributor para la identidad administrada del lago
   - c) _SRCH; Owner de la suscripción
   - d) _KQL; Monitoring Metrics Publisher

10. Sobre los grafos personalizados de Sentinel, ¿qué afirmación es correcta?
   - a) Un graph job bajo demanda materializa el grafo 30 días y uno programado lo reconstruye
   - b) Los grafos de una sesión interactiva se guardan solos
   - c) Se consultan con SQL estándar
   - d) No generan costos

11. En la gestión multi-inquilino de Defender sin Azure Lighthouse, ¿qué workspaces se pueden consultar?
   - a) Todos los de todos los tenants
   - b) Solo el workspace principal de cada tenant
   - c) Ninguno
   - d) Solo los de la suscripción del MSSP

12. ¿En qué fechas se retiró el agente SAP en contenedor y se eliminaron sus imágenes?
   - a) 31 de marzo de 2027 y 30 de junio de 2027
   - b) 14 de septiembre de 2026 y 14 de octubre de 2026
   - c) 1 de julio de 2025 y 1 de julio de 2026
   - d) 18 de agosto de 2026 y 31 de diciembre de 2026

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

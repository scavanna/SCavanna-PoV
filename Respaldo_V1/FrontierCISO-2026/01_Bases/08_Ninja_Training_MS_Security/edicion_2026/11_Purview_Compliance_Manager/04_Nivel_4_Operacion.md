# Nivel 4 · Operación · Modelo operativo, métricas y gobierno

*Microsoft Purview Compliance Manager Ninja Training · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="operacion"></a>

Cómo se organiza el equipo de GRC que opera Compliance Manager con dueños de controles, auditoría interna, privacidad y el comité de riesgos: responsabilidades, indicadores que no confunden puntuación con cumplimiento y gobierno normativo en MCSA, sin interpretar la ley.

*L300–L400 · 3 módulos · ~10 horas · 10 recursos*

**Módulos de este nivel:** [O1 Modelo operativo](#o1) · [O2 Métricas y mejora continua](#o2) · [O3 Gobierno y normativa MCSA](#o3)

<a id="o1"></a>

## O1 · Modelo operativo del equipo de GRC y responsabilidades

*L300–L400 · ~3 h · Origen: Nuevo en esta edición*

Compliance Manager pasa por muchas manos: el gestor de GRC administra evaluaciones y plantillas, los dueños de controles de TI, seguridad y nube implementan acciones, auditoría interna prueba, privacidad valida lo que toca datos personales y el comité de riesgos decide. La herramienta ofrece cuatro roles —**Reader, Contribution, Assessor y Administration**— mapeados a roles de Entra ID como Global reader, Compliance Administrator o Security Administrator; un usuario solo tiene un rol de Compliance Manager a la vez, y el acceso se puede restringir por evaluación o por regulación.

Alrededor hay otros permisos que el modelo debe prever: Security reader en Entra ID para ver alertas, Data Connector Admin para los conectores, Owner o Policy Contributor en Azure para asignar estándares en Defender for Cloud y los roles de Azure AI para las evaluaciones de Foundry. Desde julio de 2026, las asignaciones de grupos de roles de Purview pueden tener fecha de expiración —de un día a dos años—, ideal para auditores externos. Este módulo arma la matriz RACI y la segregación entre quien implementa y quien prueba.

**Por qué importa**

Sin un modelo claro, todos terminan como administradores o nadie actualiza nada, y el auditor no puede confiar en una prueba hecha por quien implementó el control. Roles definidos, accesos que vencen y una RACI acordada hacen defendible la evidencia y reducen el riesgo de cambios no autorizados.

**Qué vas a lograr**

- Diseñar la asignación de roles de Compliance Manager con mínimo privilegio y segregación de funciones.
- Construir una matriz RACI para evaluaciones, acciones, pruebas, plantillas y reportes.
- Gestionar accesos temporales de auditores externos con fecha de expiración.
- Integrar a privacidad y a los oficiales de datos que exige la normativa local.

> **Novedad.** Desde julio de 2026, las asignaciones de grupos de roles de Purview admiten fecha de expiración, de un día a dos años: úsala para auditores externos, consultores y accesos de proyecto ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** Un usuario tiene un solo rol de Compliance Manager a la vez y el acceso se puede restringir por evaluación o por regulación; en GCC High y DoD los roles se asignan solo en Entra ID ([configuración](https://learn.microsoft.com/en-us/purview/compliance-manager-setup)). Para visualizar el mapa de roles puedes usar [RBACMap](https://rbacmap.com/roles/comp-mgr-admin/), una herramienta comunitaria que conviene contrastar con Learn.

> **Atención.** La documentación usa nombres distintos para el mismo rol: la página de configuración habla de «Compliance Manager Contribution», la de alertas de «Compliance Manager Contributor» ([alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies)) y los grupos de roles aparecen en plural, como Compliance Manager Administrators ([RBACMap](https://rbacmap.com/roles/comp-mgr-admin/)). En tus procedimientos usa el nombre que ves en tu inquilino.

> **Consejo Ninja.** La normativa local crea roles que el modelo debe integrar: el Decreto 64/020 de Uruguay regula la designación de delegado de protección de datos ([URCDP](https://www.gub.uy/unidad-reguladora-control-datos-personales/comunicacion/noticias/se-promulgo-decreto-64020-reglamentario-nuevas-disposiciones-sobre)) y el nuevo reglamento peruano introduce de forma progresiva el oficial de datos personales ([DS 016-2024-JUS](https://www.gob.pe/institucion/anpd/normas-legales/6554453-16-2024-jus)). Define con Legal su lugar en la RACI.

**¿Tienes poco tiempo?**

- [Get started with Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) · Documentación
- [Compliance Manager Administrators – Microsoft Purview Role (RBACMap)](https://rbacmap.com/roles/comp-mgr-admin/) · Herramienta
- [Se promulgó el Decreto 64/020 reglamentario de nuevas disposiciones sobre protección de datos personales](https://www.gub.uy/unidad-reguladora-control-datos-personales/comunicacion/noticias/se-promulgo-decreto-64020-reglamentario-nuevas-disposiciones-sobre) · Documentación

**Matriz RACI de Compliance Manager (punto de partida)**

| Actividad | GRC | Dueño de control | Auditoría interna | Privacidad | Legal | CISO o comité | Rol sugerido en Compliance Manager |
|---|---|---|---|---|---|---|---|
| Elegir normas, cupos premium y plantillas propias | R | C | C | C | C | A | Administration para activar plantillas |
| Crear evaluaciones y grupos | A/R | I | C | I | I | I | Contribution o Administration |
| Crear y publicar plantillas propias (en blanco o desde PDF) | R | C | C | C | A | I | Administration o Assessor |
| Implementar acciones y cargar evidencias | C | A/R | I | C | I | I | Contribution |
| Probar acciones de forma independiente | I | C | A/R | C | I | I | Assessor |
| Aceptar o diferir actualizaciones de plantillas | R | I | C | I | I | A | Administration |
| Configurar alertas y destinatarios | A/R | I | I | I | I | I | Contribution, Assessor o Administration, más un rol de Entra ID que permita crear políticas |
| Validar aplicabilidad de normas y plazos | C | I | C | C | A/R | I | Reader (consulta) |
| Revisar evidencias con datos personales | C | C | C | A/R | C | I | Reader o Assessor, según la tarea |
| Reportar a la dirección | R | C | C | C | C | A | Reader (consulta) |
| Revisar accesos y roles cada trimestre | R | I | C | I | I | A | Global Administrator para asignar |

R: responsable · A: aprueba y rinde cuentas · C: consultado · I: informado. Roles según [Learn · configuración de Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) y [alertas](https://learn.microsoft.com/en-us/purview/compliance-manager-alert-policies); ajusta los nombres a los que ves en tu inquilino.

### Documentación, cursos y credenciales

- [Get started with Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-setup) · Documentación · Oficial · Microsoft Learn. Guía inicial: acceso, roles RBAC (Reader, Contribution, Assessor, Administration), prueba de evaluaciones premium, ajustes de pruebas automatizadas y recorrido por las páginas del panel.
- [Se promulgó el Decreto 64/020 reglamentario de nuevas disposiciones sobre protección de datos personales](https://www.gub.uy/unidad-reguladora-control-datos-personales/comunicacion/noticias/se-promulgo-decreto-64020-reglamentario-nuevas-disposiciones-sobre) · Documentación · Comunidad · ES · URCDP · Unidad Reguladora y de Control de Datos Personales (Uruguay) · feb 2020. Noticia oficial de la URCDP sobre el Decreto 64/020, que reglamenta la notificación de vulneraciones y la designación de delegado de protección de datos.

### Laboratorios, GitHub y herramientas

- [Compliance Manager Administrators – Microsoft Purview Role (RBACMap)](https://rbacmap.com/roles/comp-mgr-admin/) · Herramienta · Comunidad · Nuevo · RBACMap · 3 nov 2026. Mapa visual de los roles y grupos de roles de Compliance Manager (Administrators, Assessors, Contributors, Readers) con guía de asignación y buenas prácticas de mínimo privilegio.

**Manos a la obra**

1. `Laboratorio` Asigna Reader, Assessor, Contribution y Administration a cuatro cuentas de prueba y comprueba el acceso restringido por evaluación: la cuenta Reader solo debe ver la evaluación asignada ([configuración](https://learn.microsoft.com/en-us/purview/compliance-manager-setup)). Evidencia: capturas por rol.
2. `Laboratorio` Asigna a una cuenta «auditor externo» un grupo de roles de Compliance Manager con fecha de expiración de siete días y verifica que la asignación vence ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)).
3. `Laboratorio` Completa la matriz RACI de este módulo para tu organización con nombres de puesto (no de personas) y valídala con auditoría interna.
4. `Laboratorio` Diseña el flujo de una acción de mejora —asignación, implementación, evidencia, prueba independiente y cierre— con quién hace cada paso y qué rol necesita, y pruébalo de punta a punta en tu laboratorio.
5. `Solo producción` Despliega el modelo de roles en producción. Motivo: requiere personas, grupos y aprobaciones reales. Cómo hacerlo seguro: grupos de seguridad en lugar de asignaciones individuales, [PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) para Administration (se profundiza en el programa de Entra, módulo M3), expiración para auditores, revisión trimestral de accesos y un Global Administrator fuera del flujo diario.

<a id="o2"></a>

## O2 · Métricas, reportes y mejora continua

*L300–L400 · ~3 h · Origen: Ninja oficial de 2023, nivel Advanced (puntuación de cumplimiento frente a Secure Score), ampliado a un tablero de indicadores*

La métrica más citada —la puntuación de cumplimiento— es necesaria pero no suficiente. **Microsoft Secure Score** mide postura de seguridad (hasta 10 puntos por acción y comparación con organizaciones similares); la puntuación de Compliance Manager mide avance en acciones de cumplimiento. Ninguna de las dos dice si cumples la ley. Un tablero defendible combina avance (acciones implementadas y probadas), calidad (evidencias aceptadas, pruebas independientes), oportunidad (acciones vencidas, tiempo de cierre) y cobertura (normas aplicables con evaluación), siempre con fecha de corte.

La mejora continua cierra el ciclo: revisiones mensuales de métricas, retrospectivas trimestrales y lecciones de auditorías, incidentes y simulacros que vuelven como acciones de mejora con responsable. ISO/IEC 27001 exige seguimiento, medición, análisis y evaluación (cláusula 9.1), y Compliance Manager puede ser el soporte de ese requisito si las métricas están bien definidas. Cuidado con los incentivos: si el equipo se mide solo por puntos, aparecerán acciones marcadas sin evidencia.

**Por qué importa**

Lo que se mide se gestiona, pero una mala métrica distorsiona: un equipo premiado por la puntuación puede inflarla con puntos de Microsoft o con acciones sin evidencia. Indicadores defendibles conectan el esfuerzo con la reducción de riesgo y resisten la revisión de un auditor.

**Qué vas a lograr**

- Definir un tablero de indicadores de cumplimiento defendible ante auditoría y dirección.
- Separar métricas de avance, calidad, oportunidad y cobertura.
- Establecer un ciclo de mejora continua con revisiones y lecciones aprendidas.
- Detectar y evitar incentivos perversos sobre la puntuación.

> **Consejo Ninja.** Secure Score asigna hasta 10 puntos por acción y te compara con organizaciones similares; la puntuación de cumplimiento mide avance en acciones de cumplimiento. El Ninja oficial de 2023 ya pedía distinguirlas y sigue vigente: repórtalas por separado ([Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score)).

> **Atención.** La puntuación puede subir sin trabajo propio: según un análisis comunitario, la regulación AI Baseline que aparece con licencias de Copilot trae 179 acciones, 99 de ellas de Microsoft ([AI Baseline](https://informasjonsbeskyttelse.no/en/ai-baseline-in-microsoft-purview)). Reporta por separado tus puntos y los de Microsoft, y anota las actualizaciones de plantillas aceptadas.

> **Consejo Ninja.** Para indicadores defendibles ante auditores, combina la puntuación con métricas de etiquetado, DLP y auditoría ([ideas de KPI](https://www.2tolead.com/insights/microsoft-purview-compliance-analytics-reports-dlp-audit)) y apóyate en la cláusula 9.1 de ISO/IEC 27001, que Compliance Manager puede soportar ([SGSI](https://informasjonsbeskyttelse.no/en/how-purview-supports-an-isms)).

**¿Tienes poco tiempo?**

- [Microsoft Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score) · Documentación
- [Microsoft Purview Compliance Analytics: Reports & Real-World Insights](https://www.2tolead.com/insights/microsoft-purview-compliance-analytics-reports-dlp-audit) · Blog
- [What API or PowerShell cmdlet can be used to collect Microsoft compliance manager score data? (Microsoft Q&A)](https://learn.microsoft.com/en-gb/answers/questions/2081811/what-api-or-powershell-cmdlet-can-be-used-to-colle) · Blog

**Tablero de indicadores de cumplimiento**

| Indicador | Cómo se calcula | Fuente del dato | Audiencia | Cuidado |
|---|---|---|---|---|
| Puntuación de cumplimiento por evaluación | Puntos obtenidos sobre puntos alcanzables, con fecha de corte y actualizaciones aceptadas | Panel y exportación de Compliance Manager | Comité y GRC | No equivale a cumplimiento; separa tus puntos de los de Microsoft |
| Acciones propias implementadas y probadas | Porcentaje de acciones gestionadas por tu organización con implementación y prueba aprobadas | Exportación de acciones | GRC y auditoría interna | Cuenta solo las que tienen evidencia aceptada |
| Acciones vencidas por dueño | Cantidad de acciones con fecha comprometida vencida, por responsable | Exportación de acciones | Dueños de controles y CISO | Requiere una fecha comprometida en cada acción |
| Tiempo medio de cierre | Días entre la asignación y la prueba aprobada | Alertas de asignación y de estado, y exportaciones | GRC | Mídelo por separado para acciones técnicas y no técnicas |
| Calidad de la evidencia | Porcentaje de evidencias aceptadas en la primera revisión de auditoría interna | Registro de auditoría interna | Auditoría interna y GRC | Define antes los criterios de evidencia aceptable |
| Pruebas independientes | Porcentaje de acciones manuales probadas por alguien distinto de quien implementó | Exportación (responsables de implementación y de prueba) | Auditoría interna y comité | Es tu indicador de segregación de funciones |
| Cobertura normativa | Normas aplicables con evaluación activa sobre normas aplicables | Inventario de normas (hoja «Normativa MCSA») y Compliance Manager | Comité y Legal | Una norma sin plantilla cuenta cuando su plantilla propia está publicada |
| Uso de cupos premium | Cupos usados frente a normas prioritarias, con fechas de renovación | Página Regulations | GRC y compras | Evita renovar plantillas que ya no aplican |
| Cumplimiento de plazos en simulacros | Tiempo real frente al plazo regulatorio (por ejemplo, 1 h del BCRA o 3 h en Chile) | Informe del simulacro | CISO, Legal y comité | Sin enviar nada al regulador durante el simulacro |
| Microsoft Secure Score (sección aparte) | Puntos de seguridad y comparación con organizaciones similares | Portal de Defender | CISO y SOC | No lo sumes ni lo promedies con la puntuación de cumplimiento |

Fuentes: [puntuación de cumplimiento](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring), [Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score), [ideas de KPI](https://www.2tolead.com/insights/microsoft-purview-compliance-analytics-reports-dlp-audit) y [nota metodológica del BCU](https://www.bcu.gub.uy/Comunicados/Anexo%201%20-%20Nota%20metodologica%20V2.pdf).

### Documentación, cursos y credenciales

- [Microsoft Secure Score](https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score) · Documentación · Oficial · Microsoft Learn. Explica Microsoft Secure Score (puntos por acción, comparación con organizaciones similares, KPIs), métrica que debe diferenciarse y combinarse con la puntuación de cumplimiento en el tablero operativo.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Purview Compliance Analytics: Reports & Real-World Insights](https://www.2tolead.com/insights/microsoft-purview-compliance-analytics-reports-dlp-audit) · Blog · Comunidad · 2toLead. Propone KPIs defendibles ante auditores y dirección combinando la puntuación de Compliance Manager con métricas de etiquetado, DLP y auditoría.
- [What API or PowerShell cmdlet can be used to collect Microsoft compliance manager score data? (Microsoft Q&A)](https://learn.microsoft.com/en-gb/answers/questions/2081811/what-api-or-powershell-cmdlet-can-be-used-to-colle) · Blog · Comunidad · Microsoft Q&A · 19 nov 2024. Hilo de la comunidad sobre cómo obtener datos de la puntuación de Compliance Manager de forma automatizada; ilustra que no hay un cmdlet ni API documentada específica y que hay que recurrir a exportaciones.

**Manos a la obra**

1. `Laboratorio` Construye el tablero de indicadores de este módulo con datos de tu laboratorio (exportaciones de al menos dos fechas) y documenta la fórmula y la fuente de cada indicador.
2. `Laboratorio` Calcula para tu evaluación de práctica qué parte de la puntuación corresponde a acciones de Microsoft y qué parte a las tuyas, y explica en un párrafo por qué esa diferencia cambia la lectura del reporte ([puntuación](https://learn.microsoft.com/en-us/purview/compliance-manager-scoring)).
3. `Laboratorio` Diseña una retrospectiva trimestral: agenda, insumos (alertas, auditorías, incidentes y simulacros), salidas (acciones nuevas, cambios de dueño y decisiones) y registro.
4. `Laboratorio` Revisa tu tablero con la lista de [ideas de KPI](https://www.2tolead.com/insights/microsoft-purview-compliance-analytics-reports-dlp-audit) y agrega un indicador de etiquetado, DLP o auditoría que complemente la puntuación.
5. `Solo producción` Publica el tablero mensual a la dirección. Motivo: requiere datos y responsables reales. Cómo hacerlo seguro: cifras con fecha de corte y actualizaciones aceptadas, revisión de auditoría interna antes de publicar, Secure Score en una sección separada y ningún dato personal.

<a id="o3"></a>

## O3 · Gobierno, privacidad y cumplimiento normativo en MCSA

*L300–L400 · ~4 h · Origen: Nuevo en esta edición*

Gobernar Compliance Manager significa decidir quién aprueba qué: la elección de cupos premium, la publicación de plantillas propias, la aceptación de actualizaciones, la carga de evidencias y los reportes al comité. En MCSA ese gobierno debe seguir una normativa que cambia rápido: nuevas leyes de datos en México (2025), Chile (vigente desde el 1 de diciembre de 2026) y Paraguay (2025), un nuevo reglamento en Perú, leyes de ciberseguridad en Ecuador (vigente desde el 22 de mayo de 2026) y Guatemala (aprobada el 3 de noviembre de 2026, pendiente de publicación) y nuevas reglas del BCRA y del BCU.

Las brechas de la herramienta también son parte del gobierno: la plantilla de México sigue la ley de 2010, la lista de regulaciones no se actualiza desde marzo de 2025 y la mayoría de los países no tiene plantilla. El proceso que propone este módulo encadena vigilancia normativa, decisión de aplicabilidad (Legal), enfoque en la herramienta (GRC), controles (dueños) y evidencia (auditoría), con privacidad en todo el ciclo, porque las evidencias también pueden contener datos personales. Cada programa de Purview tiene su propio O3 con el ángulo de su capacidad; aquí está la vista consolidada.

**Por qué importa**

La velocidad del cambio normativo en la región exige un proceso, no un esfuerzo heroico. Un gobierno con Legal y privacidad asegura que la herramienta refleje la ley vigente y que cada decisión sea trazable, algo que piden tanto los supervisores como el directorio.

**Qué vas a lograr**

- Establecer un proceso de vigilancia normativa con responsables, fuentes y frecuencia.
- Definir quién aprueba plantillas, actualizaciones, evidencias y reportes, y cómo se registra.
- Resumir para el comité el panorama normativo de MCSA y las brechas de plantillas.
- Proteger la privacidad de las evidencias que se cargan en Compliance Manager.

> **Novedad.** Cambios recientes clave: México (nuevas leyes de datos, 20 de marzo de 2025); Chile (Ley 21.719 vigente desde el 1 de diciembre de 2026 y reporte de incidentes a la ANCI obligatorio desde el 1 de marzo de 2025, [ANCI](https://anci.gob.cl/noticias/obligacion-de-reportar/)); Perú (nuevo reglamento desde el 31 de marzo de 2025); Ecuador (ley de ciberseguridad vigente desde el 22 de mayo de 2026 y norma técnica de vulneraciones de septiembre de 2026); Paraguay (Ley 7593/2025, plena vigencia a fines de noviembre de 2027); Argentina (Comunicación «A» 8280, julio de 2025); Uruguay (Decreto 66/025 y régimen de tercerizaciones de 2026), y Guatemala (Ley Marco de Ciberseguridad aprobada el 3 de noviembre de 2026, pendiente de publicación, [diario oficial](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/)).

> **Atención.** Brechas de la herramienta: la plantilla de México sigue la ley de 2010 y la lista de regulaciones no se actualiza desde el 6 de marzo de 2025 ([lista](https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list)); Chile, Ecuador, Uruguay, Costa Rica, Panamá y el resto de Centroamérica no tienen plantilla. El enfoque por norma está en [Plantillas para MCSA](00_Programa.md#plantillas-mcsa).

> **Consejo Ninja.** Perú tiene doble notificación según un artículo del diario oficial: 48 horas a la ANPD por datos personales y 48 horas al Centro Nacional de Seguridad Digital por incidentes digitales críticos (DS 126-2025-PCM); verifícalo en el texto del decreto antes de fijarlo en un procedimiento ([El Peruano](https://elperuano.pe/noticia/292188-incidente-de-seguridad-digital-o-de-datos-personales)).

> **Atención.** Esta guía no interpreta leyes. La iniciativa de Ley General de Ciberseguridad de México (enero de 2026) seguía sin dictaminar al cierre de octubre de 2026 y no es vinculante ([iniciativa](http://sil.gobernacion.gob.mx/Archivos/Documentos/2026/01/asun_5006470_20260126_1767896715.pdf)); cualquier decisión sobre normas en trámite corresponde a Legal, con privacidad y, si toca a las personas trabajadoras, RR. HH.

**¿Tienes poco tiempo?**

- [ANCI – Obligación de reportar incidentes de ciberseguridad (Chile)](https://anci.gob.cl/noticias/obligacion-de-reportar/) · Documentación
- [El Peruano – Incidente de seguridad digital o de datos personales (Ley de Confianza Digital)](https://elperuano.pe/noticia/292188-incidente-de-seguridad-digital-o-de-datos-personales) · Documentación
- [Nueva ley blinda el ciberespacio de Guatemala (Ley Marco de Ciberseguridad)](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/) · Documentación
- [El BCU avanza en la implementación de nuevos estándares de ciberseguridad para la industria financiera](https://www.bcu.gub.uy/Comunicaciones/Paginas/Detalle-Noticia.aspx?noticia=518&title=El-BCU-avanza-en-la-implementaci%C3%B3n-de-nuevos-est%C3%A1ndares-de-ciberseguridad-para-la-industria-financiera-) · Documentación

### Documentación, cursos y credenciales

- [Nueva ley blinda el ciberespacio de Guatemala (Ley Marco de Ciberseguridad)](https://dca.gob.gt/noticias-guatemala-diario-centro-america/nueva-ley-blinda-el-ciberespacio-de-guatemala/) · Documentación · Comunidad · Nuevo · ES · Diario de Centro América · nov 2026. Nota del diario oficial sobre la aprobación de la Ley Marco de Ciberseguridad, que crea una estructura estatal especializada y nuevos delitos informáticos en Guatemala.
- [El BCU avanza en la implementación de nuevos estándares de ciberseguridad para la industria financiera](https://www.bcu.gub.uy/Comunicaciones/Paginas/Detalle-Noticia.aspx?noticia=518&title=El-BCU-avanza-en-la-implementaci%C3%B3n-de-nuevos-est%C3%A1ndares-de-ciberseguridad-para-la-industria-financiera-) · Documentación · Comunidad · Nuevo · ES · BCU · Banco Central del Uruguay · 26 jun 2026. El BCU inicia el reporte periódico de capacidades de ciberseguridad basado en el Marco de Ciberseguridad de AGESIC, comenzando por emisores de dinero electrónico.
- [El Peruano – Incidente de seguridad digital o de datos personales (Ley de Confianza Digital)](https://elperuano.pe/noticia/292188-incidente-de-seguridad-digital-o-de-datos-personales) · Documentación · Comunidad · ES · El Peruano · Diario Oficial El Peruano · 27 mar 2026. Artículo del diario oficial que explica la doble notificación en Perú: 48 horas a la ANPD por datos personales y 48 horas al CNSD por incidentes digitales críticos (DS 126-2025-PCM).
- [ANCI – Obligación de reportar incidentes de ciberseguridad (Chile)](https://anci.gob.cl/noticias/obligacion-de-reportar/) · Documentación · Comunidad · ES · ANCI · Agencia Nacional de Ciberseguridad de Chile · 1 mar 2025. Aviso oficial de que desde el 1 de marzo de 2025 es obligatorio reportar incidentes a la ANCI, con alerta temprana dentro de 3 horas.

**Manos a la obra**

1. `Laboratorio` Redacta el procedimiento de vigilancia normativa: fuentes oficiales por país (de la hoja «Normativa MCSA»), frecuencia, responsable, criterio de impacto y registro de decisiones.
2. `Laboratorio` Prepara un resumen de una página del panorama normativo de tus países para el comité, citando las URL oficiales y marcando qué plazos están confirmados en texto oficial y cuáles no.
3. `Laboratorio` Define la política de evidencias: qué no se sube (datos personales, secretos, contenido de clientes), quién aprueba, cuánto se conserva y quién puede verlas; revísala con privacidad.
4. `Laboratorio` Arma el calendario de entradas en vigor y plazos de adecuación (Chile, 1 de diciembre de 2026; Paraguay, fines de noviembre de 2027; Guatemala, 30 días después de publicarse la ley) y conviértelo en hitos del programa de cumplimiento continuo ([Ley 21.719](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01), [Ley 7593/2025](https://www.bacn.gov.py/leyes-paraguayas/12924/ley-n-75932025--de-proteccin-de-datos-personales-en-la-repblica-del-paraguay)).
5. `Solo producción` Presenta al comité de riesgos la decisión anual de cupos premium y plantillas propias. Motivo: compromete presupuesto y prioridades reales. Cómo hacerlo seguro: propuesta revisada por Legal y privacidad, sin interpretar la ley, con acta, fecha de revisión y responsables.

<a id="reto-operacion"></a>

## Reto del nivel

**Defensa ante el comité de riesgos.** Presenta el modelo operativo de Compliance Manager de tu organización: matriz RACI, roles con expiración y PIM, tablero de diez indicadores con fórmulas, procedimiento de vigilancia normativa y decisiones de cupos y plantillas propias para el próximo año. Incluye las limitaciones conocidas y lo que falta confirmar con Legal y privacidad. Formato: diez minutos de exposición y una página de resumen ejecutivo.

<a id="quiz-operacion"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-operacion). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. Un auditor externo debe revisar solo la evaluación ISO 27001 durante dos semanas. ¿Qué configuración es la más adecuada?
   - a) Global Administrator temporal
   - b) Compliance Manager Administration sin restricciones
   - c) Compliance Manager Reader con acceso restringido a esa evaluación y asignación con fecha de expiración
   - d) Una cuenta de servicio compartida

2. ¿Cuántos roles de Compliance Manager puede tener un usuario a la vez?
   - a) Uno
   - b) Dos, si uno es Reader
   - c) Todos los que necesite
   - d) Ninguno: se usan solo roles de Entra ID

3. ¿Qué rango admite la fecha de expiración de las asignaciones de grupos de roles de Purview introducida en julio de 2026?
   - a) Entre una hora y 30 días
   - b) Entre un día y dos años
   - c) Solo 90 días fijos
   - d) No tiene límite máximo

4. ¿Qué rol de Compliance Manager no puede crear ni editar políticas de alertas?
   - a) Administration
   - b) Assessor
   - c) Contributor
   - d) Reader

5. ¿Cuál es la relación correcta entre Secure Score y la puntuación de cumplimiento?
   - a) Son la misma métrica con distinto nombre
   - b) Secure Score mide postura de seguridad y la puntuación de cumplimiento, avance en acciones de cumplimiento: se reportan por separado
   - c) La puntuación de cumplimiento es el promedio de Secure Score
   - d) Secure Score solo aplica a Azure

6. ¿Qué indicador es más defendible ante auditoría interna?
   - a) La puntuación global sin fecha
   - b) La cantidad de evaluaciones creadas
   - c) El porcentaje de acciones propias implementadas y probadas con evidencia aceptada
   - d) El número de plantillas premium compradas

7. ¿Qué cláusula de ISO/IEC 27001 puede apoyar Compliance Manager al medir el sistema de gestión?
   - a) 9.1 (seguimiento, medición, análisis y evaluación)
   - b) 4.1 (contexto de la organización)
   - c) 7.5 (información documentada)
   - d) 10.2 (no conformidad y acción correctiva)

8. ¿Desde cuándo rige la Ley 21.719 de protección de datos de Chile?
   - a) Desde su publicación en diciembre de 2024
   - b) Desde el 1 de marzo de 2025
   - c) Desde el 1 de diciembre de 2026
   - d) Desde enero de 2028

9. ¿En qué estado está la Ley Marco de Ciberseguridad de Guatemala al 6 de noviembre de 2026?
   - a) Vigente desde 2024
   - b) Rechazada por el Congreso
   - c) Reemplazada por una norma del supervisor bancario
   - d) Aprobada el 3 de noviembre de 2026 y pendiente de publicación; regiría 30 días después de publicarse

10. Según el concepto de la SIC de Colombia, ¿en qué plazo se reportan los incidentes de seguridad de datos personales?
   - a) 15 días hábiles desde la detección
   - b) 72 horas
   - c) De inmediato
   - d) 30 días corridos

11. ¿Cuándo se prevé la plena vigencia de la Ley 7593/2025 de Paraguay?
   - a) De inmediato, desde su promulgación
   - b) A fines de noviembre de 2027, tras 24 meses de adecuación
   - c) En marzo de 2026
   - d) Cuando Microsoft publique una plantilla

12. En el gobierno normativo, ¿qué corresponde a Legal y qué a Compliance Manager?
   - a) Compliance Manager decide qué leyes aplican
   - b) Legal decide la aplicabilidad y Compliance Manager organiza controles, acciones y evidencias de lo decidido
   - c) El proveedor de la plantilla responde por el cumplimiento
   - d) La puntuación reemplaza la opinión legal

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: la normativa citada es material de referencia y las decisiones de aplicabilidad corresponden a tus áreas de Legal, privacidad y, cuando aplique, RR. HH. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

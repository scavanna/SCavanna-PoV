# Operación de controles y formación Microsoft

[Biblioteca](../README.md) · [23 guías de Excelencia Operacional](Guias-Excelencia.md) · [15 planes Ninja por rol](Rutas-Ninja.md)

**Entrada:** una función del [Plan CISO](../01_Gobierno-CISO/README.md), un riesgo y un entorno. **Salida:** un producto-control con titular y suplente, cadencias, prueba y formación. La edición Microsoft v2.1 rev. 3 extiende el Plan v2.0; no lo sustituye.

## 1. Comprobá cobertura antes de elegir tecnología

1. Partí de la función (`GOB-`, `GES-` u `OPE-`) y del resultado deseado. En la matriz Microsoft, distinguí si una capacidad **cubre, cubre en parte, apoya o queda fuera**.
2. Contrastá **cada** entorno del alcance. Azure, AWS, Google Cloud, centro de datos y SaaS pueden tener conectores, derechos y profundidad distintos. «No confirmado» exige demostración; no equivale a «no».
3. Registrá por separado: **derecho contractual**, disponibilidad y región, despliegue, población efectivamente cubierta y prueba. Un estado GA del producto no confirma el estado de cada función ni su inclusión en un tenant.
4. Si el catálogo cruza dominios Gartner con Microsoft y Atlas v5.3, usalo para armar preguntas de comparación. No lo presentes como reseña de Gartner, evaluación independiente ni cruce reconciliado con Frontier.

| Ficha de decisión | Completar |
| --- | --- |
| Función, escenario y entorno | |
| Capacidad y dependencia de licencia o consumo | |
| Cobertura de referencia / despliegue / población medida | |
| Fuente con fecha / prueba real / límite | |
| Brecha, alternativa y responsable de decisión | |

## 2. Operá el control en tres planos

| Plano | Qué tiene que definir el Product Owner | Qué deja evidencia |
| --- | --- | --- |
| Configuración inicial y cambios | Objetivo, prerrequisitos, privilegios, exclusiones, aprobación y reversión. Validar en un piloto de alcance limitado antes de aplicar. | Configuración versionada, población, resultado de pruebas de aceptación y reversión. |
| Rutina periódica | Diaria: salud y cola. Semanal: calidad y desvíos. Mensual: métricas y excepciones. Trimestral o según riesgo: recertificación y prueba independiente. | Registro de ejecución, hallazgos, dueño y plazo. Ajustar frecuencia al riesgo, no a la disponibilidad del equipo. |
| Acción ante un evento | Umbral, evidencia mínima, autoridad, escalamiento y opción de reversión. | Caso, decisión, operador, acción, resultado y restitución. |

El titular responde por el control, no por ejecutar todas las tareas. Plataforma implementa; el SOC observa y responde; el responsable de riesgo acepta el residual. Nombrá suplente y comprobá que pueda sostener el control sin ayuda del titular.

### Elegí la familia de guías

| Necesidad | Módulos de Excelencia Operacional |
| --- | --- |
| Marco común de roles y cadencias | `00` CISO, SOC y NIST |
| Identidades y privilegios | `01` Entra ID; `02` Entra ID Governance |
| Detección, respuesta y observabilidad | `03` Defender XDR; `08` Sentinel; `09` Security Copilot |
| Sensores y cobertura de superficies | `04` Defender for Endpoint; `05` Defender for Office 365; `06` Defender for Identity; `07` Defender for Cloud Apps |
| Dispositivos, configuración y cifrado | `10` Intune Plan 1; `11` Intune Suite; `12` Windows Enterprise Security |
| Gobierno y protección de datos | `13` arquitectura Purview Suite; `14` Information Protection; `15` DLP; `16` Data Lifecycle y Records Management |
| Riesgo interno, cumplimiento e investigación | `17` Insider Risk; `18` Communication Compliance; `19` Audit Premium; `20` eDiscovery Premium |
| Acceso de soporte, claves y agentes | `21` Customer Lockbox, Customer Key y M365 PAM; `22` Agent 365 |

Los 23 módulos son el inventario de procedimientos. En la edición Microsoft, **M05** sirve para programar cadencias, **M06** para formar roles, **M10** para localizar procedimientos en las guías y **M11** para asignar el producto-control y sus indicadores técnicos. No son cuatro copias de una matriz.

## 3. Cerrá el vínculo entre operación, medición y formación

- **Operación:** asigná un procedimiento para cada control en alcance y acordá el umbral que obliga a intervenir.
- **Medición:** en el cruce Microsoft v2.1, 111 de los 224 indicadores del Plan tienen una fuente de plataforma: 12 directos y 99 derivados. Los demás son registros de gestión. Confirmá que la fuente cubre la población y que la fórmula es la del indicador, no solo el nombre de una señal.
- **Formación:** elegí guía, programa Ninja y ejercicio por rol. La cobertura documental describe si hay material **directo**, **parcial** o **sin artefacto específico**; ninguna categoría demuestra competencia ni efectividad del control.
- **Aceptación:** antes de dar el control por operativo, pedí una prueba por entorno, evidencia entregable y un suplente que demuestre la rutina. Si el procedimiento no cubre una variante, abrí una brecha con dueño.

No uses las 130 actividades ni los 70 indicadores del puente Product Owner para numerar el Plan Frontier. El puente aporta el método de vinculación; su correspondencia original se basa en Plan v1.0.

## Anexos de trabajo

- [Libro de implementación Microsoft v2.1](artefactos/Frontier_CISO_Atlas_CISO365_Edicion_Microsoft_v2.1.xlsx): capacidades, licencias, medición, cadencias y formación. Corte de la fuente: 15 de noviembre de 2026; revalidar antes de una decisión.
- [Guías de Excelencia Operacional v2.0](Guias-Excelencia.md): 23 procedimientos para consultar por ID `EO-##`. Los planes editables y recursos de formación están en [Rutas Ninja](Rutas-Ninja.md).
- [Cobertura documental de 43 capacidades](artefactos/cobertura-43-capacidades.csv): Ninja 10 directas, 21 parciales, 12 sin artefacto; Excelencia 14, 9 y 20. Buscá por tecnología y usá los IDs `NT-##` y `EO-##` para ir a los índices locales. Es un universo distinto de las 50 capacidades de la edición Microsoft.
- [Comparativo por dominio y Atlas v5.3](artefactos/AI_CISO_Atlas_Matrices_ABCD_Dominios_Gartner_Microsoft_2026-11-04.xlsx): referencia editorial. No se encontraron las reseñas primarias ni un cruce equivalente validado con Frontier.

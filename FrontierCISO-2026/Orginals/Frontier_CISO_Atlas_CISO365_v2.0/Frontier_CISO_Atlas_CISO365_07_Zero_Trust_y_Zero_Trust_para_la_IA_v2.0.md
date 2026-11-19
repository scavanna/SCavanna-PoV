# Zero Trust y Zero Trust para la IA

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 07 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## 1. Qué se investigó y qué se encontró

Se revisaron las publicaciones de NIST, de The Open Group y de Microsoft sobre Zero Trust y sobre su aplicación a la IA y a los agentes, con fecha de corte al 15 de noviembre de 2026: 34 fuentes, 29 verificadas en su origen.

- **No hay un estándar formal de «Zero Trust para la IA».** Ninguna de las tres organizaciones lo tiene. Solo Microsoft usa esa denominación, desde el 19 de marzo de 2026, con una ampliación el 4 de agosto de 2026.
- **NIST, lo final.** SP 800-207 (11 de agosto de 2020, siete principios), SP 800-207A (13 de septiembre de 2023), SP 1800-35 (10 de junio de 2025) y CSWP 20 (6 de mayo de 2022).
- **NIST, lo que no es final.** Un documento conceptual sobre identidad de agentes (5 de febrero de 2026); diez principios de diseño propuestos en una entrada de blog (27 de octubre de 2026); las superposiciones de control COSIS, antes COSAiS, renombradas el 20 de octubre de 2026, con documento conceptual y esquema anotado pero sin borrador público; y el perfil Cyber AI, IR 8596, en borrador preliminar (16 de diciembre de 2025).
- **The Open Group.** Los Zero Trust Commandments figuran como estándar. El modelo de referencia sigue en Snapshot 1.0. No hay nada sobre IA. El texto oficial no pudo consultarse.
- **Microsoft.** Tres principios: verificar de forma explícita, usar el mínimo privilegio y asumir la vulneración. Agregó un pilar de IA con siete áreas de control, un taller, una evaluación y un catálogo de defensas. Todo está ligado a sus productos.
- **Derivados.** El modelo de madurez de CISA, versión 2.0, y la arquitectura de referencia del Departamento de Defensa de Estados Unidos.

## 2. Lo que coincide entre las fuentes

Para los agentes de IA, las fuentes coinciden en cinco prácticas. El modelo las toma como criterios, sin adoptar la terminología de ningún proveedor:

1. **Identidad propia por agente**, distinta de la de la persona que lo usa y de la del servicio que lo aloja.
2. **Mínimo privilegio por tarea**: el permiso se otorga para una tarea y un tiempo, no de forma permanente.
3. **Política aplicada fuera del modelo**: el control de acceso no depende de las instrucciones del modelo.
4. **Registro independiente** de lo que el agente hizo, con qué datos y con qué herramientas.
5. **Aprobación humana** para las acciones de alto impacto.

## 3. Tres principios y ocho dominios

| Principio | Qué significa |
|---|---|
| Verificar de forma explícita | Cada acceso se decide con todas las señales disponibles: identidad, dispositivo, recurso, contexto y comportamiento. |
| Mínimo privilegio | Acceso justo, por tiempo limitado y por tarea; nada permanente. |
| Asumir la vulneración | Diseñar para contener el daño, ver lo que ocurre y recuperarse. |

| Dominio | Alcance | Criterios |
|---|---|:--:|
| Identidades | Personas, servicios, cargas y agentes: quién o qué pide acceso. | 6 |
| Dispositivos | Puestos de trabajo, móviles y servidores desde los que se accede. | 5 |
| Aplicaciones y cargas | Aplicaciones propias y de terceros, interfaces y cargas en ejecución. | 5 |
| Datos | La información, donde esté: clasificación, acceso, cifrado y salida. | 5 |
| Infraestructura | Nubes, centros de datos y plataformas que sostienen las cargas. | 5 |
| Red | Segmentación, acceso remoto y tráfico: ninguna ubicación otorga confianza. | 5 |
| Visibilidad, automatización y gobierno | Telemetría, política uniforme, respuesta automatizada y dirección del conjunto. Dominio transversal. | 5 |
| IA y agentes | Sistemas de IA y agentes como sujetos de acceso y como activos por proteger. | 6 |

El dominio «Visibilidad, automatización y gobierno» es transversal. «IA y agentes» trata a los agentes como sujetos de acceso.

## 4. Los 42 criterios

| ID | Dominio | Principio | Criterio | Indicadores | Base |
|---|---|---|---|---|:--:|
| ZT-ID-1 | Identidades | Verificar de forma explícita | Todas las personas se autentican con métodos resistentes a la suplantación; las cuentas privilegiadas, sin excepción. | K33 | Firme |
| ZT-ID-2 | Identidades | Verificar de forma explícita | Cada solicitud de acceso se evalúa con señales de identidad, dispositivo, ubicación y riesgo antes de concederse. | K118 | Firme |
| ZT-ID-3 | Identidades | Mínimo privilegio | Los privilegios se conceden por tiempo limitado y por tarea; no hay privilegios permanentes. | K34 · K146 | Firme |
| ZT-ID-4 | Identidades | Mínimo privilegio | Las altas, los cambios y las bajas de identidades están automatizados y los accesos se recertifican. | K112 · K113 · K114 | Firme |
| ZT-ID-5 | Identidades | Asumir la vulneración | Las identidades no humanas —servicios, cargas y agentes— tienen dueño, credenciales rotadas y privilegio revisado. | K148 | Firme |
| ZT-ID-6 | Identidades | Asumir la vulneración | Un proveedor de identidad central federa las aplicaciones críticas de todos los entornos. | K115 | Firme |
| ZT-DI-1 | Dispositivos | Verificar de forma explícita | Solo los dispositivos inventariados, gestionados y conformes acceden a los recursos corporativos. | K149 | Firme |
| ZT-DI-2 | Dispositivos | Verificar de forma explícita | El estado del dispositivo se evalúa en cada acceso, no solo cuando se lo registra. | K149 | Firme |
| ZT-DI-3 | Dispositivos | Mínimo privilegio | Los usuarios no trabajan con privilegios de administrador local. | K192 | Firme |
| ZT-DI-4 | Dispositivos | Asumir la vulneración | Todos los dispositivos tienen protección y respuesta, con telemetría centralizada. | K150 | Firme |
| ZT-DI-5 | Dispositivos | Asumir la vulneración | Los parches críticos se aplican dentro del plazo definido. | K151 | Firme |
| ZT-AP-1 | Aplicaciones y cargas | Verificar de forma explícita | Las aplicaciones autentican a los usuarios y a otras cargas mediante la identidad central; no hay cuentas locales compartidas. | K115 | Firme |
| ZT-AP-2 | Aplicaciones y cargas | Mínimo privilegio | El acceso se concede por aplicación, no por pertenecer a una red. | K159 | Firme |
| ZT-AP-3 | Aplicaciones y cargas | Asumir la vulneración | El ciclo de desarrollo incluye controles automatizados y bloquea lo que no los supera. | K38 · K157 | Firme |
| ZT-AP-4 | Aplicaciones y cargas | Asumir la vulneración | Los componentes de terceros están inventariados y sus vulnerabilidades se gestionan. | K133 | Firme |
| ZT-AP-5 | Aplicaciones y cargas | Asumir la vulneración | Los secretos no están en el código ni en las configuraciones: se guardan en una bóveda y se rotan. | K156 · K158 | Firme |
| ZT-DA-1 | Datos | Verificar de forma explícita | Los datos sensibles están descubiertos, clasificados y etiquetados en todos los entornos. | K37 · K110 | Firme |
| ZT-DA-2 | Datos | Mínimo privilegio | El acceso a los datos se concede por necesidad y la sobreexposición se corrige. | K155 | Firme |
| ZT-DA-3 | Datos | Asumir la vulneración | La salida de datos sensibles se controla en el correo, la nube, los dispositivos y la IA. | K154 · K52 | Firme |
| ZT-DA-4 | Datos | Asumir la vulneración | Los datos están cifrados en tránsito y en reposo, con las claves bajo el control de la organización. | K156 | Firme |
| ZT-DA-5 | Datos | Asumir la vulneración | Existen respaldos inalterables con restauración probada. | K28 · K180 | Firme |
| ZT-IN-1 | Infraestructura | Verificar de forma explícita | Todos los entornos —nubes y centros de datos— se despliegan bajo una línea base común y su cumplimiento se verifica. | K134 · K141 | Firme |
| ZT-IN-2 | Infraestructura | Mínimo privilegio | La administración de la infraestructura usa acceso privilegiado por tiempo limitado y estaciones dedicadas. | K146 | Firme |
| ZT-IN-3 | Infraestructura | Asumir la vulneración | La deriva de configuración se detecta y se corrige en plazo. | K120 · K121 | Firme |
| ZT-IN-4 | Infraestructura | Asumir la vulneración | Las cargas tienen protección en tiempo de ejecución y las imágenes se analizan antes de desplegarlas. | K161 · K162 | Firme |
| ZT-IN-5 | Infraestructura | Asumir la vulneración | La plataforma de control —identidad, gestión y respaldo— puede recuperarse en un entorno aislado. | K181 | Firme |
| ZT-RE-1 | Red | Verificar de forma explícita | Ninguna ubicación de red otorga confianza por sí misma: la red interna se trata como no confiable. | K118 | Firme |
| ZT-RE-2 | Red | Mínimo privilegio | Los activos críticos están segmentados y la segmentación se verifica con pruebas. | K36 | Firme |
| ZT-RE-3 | Red | Mínimo privilegio | El acceso remoto llega a aplicaciones concretas, no a segmentos completos de la red. | K159 | Firme |
| ZT-RE-4 | Red | Asumir la vulneración | El tráfico está cifrado y el que cruza entre segmentos críticos se inspecciona. | K193 | Firme |
| ZT-RE-5 | Red | Asumir la vulneración | Las reglas de red se revisan y se eliminan las que no se usan o son demasiado amplias. | K160 | Firme |
| ZT-VA-1 | Visibilidad, automatización y gobierno | Verificar de forma explícita | La telemetría de identidades, dispositivos, aplicaciones, datos, infraestructura y red llega a una plataforma central. | K41 · K173 | Firme |
| ZT-VA-2 | Visibilidad, automatización y gobierno | Verificar de forma explícita | Las políticas de acceso se definen una vez y se aplican de manera uniforme en todos los entornos. | K123 · K75 | Firme |
| ZT-VA-3 | Visibilidad, automatización y gobierno | Asumir la vulneración | Las detecciones se prueban contra las técnicas de ataque priorizadas. | K43 | Firme |
| ZT-VA-4 | Visibilidad, automatización y gobierno | Asumir la vulneración | La respuesta a los eventos frecuentes está automatizada, con aprobación humana donde el impacto lo exige. | K55 · K179 | Firme |
| ZT-VA-5 | Visibilidad, automatización y gobierno | Asumir la vulneración | La arquitectura Zero Trust tiene dueño, hoja de ruta y medición informada a la dirección. | K71 · K22 | Firme |
| ZT-IA-1 | IA y agentes | Verificar de forma explícita | Todo sistema de IA y todo agente está inventariado, con dueño y propósito. | K49 · K187 | Provisoria |
| ZT-IA-2 | IA y agentes | Verificar de forma explícita | Cada agente tiene identidad propia: no usa la de su creador ni credenciales compartidas. | K165 | Provisoria |
| ZT-IA-3 | IA y agentes | Mínimo privilegio | Cada agente accede solo a las herramientas, los datos y las acciones que su tarea requiere, con un nivel de autonomía aprobado. | K50 · K88 | Provisoria |
| ZT-IA-4 | IA y agentes | Mínimo privilegio | Los datos que usan los sistemas de IA están clasificados y la IA respeta sus permisos y sus etiquetas. | K52 | Provisoria |
| ZT-IA-5 | IA y agentes | Asumir la vulneración | El contenido que el agente procesa nunca se trata como una instrucción: hay filtros, límites de acción fuera del modelo y pruebas adversariales. | K166 · K54 | Provisoria |
| ZT-IA-6 | IA y agentes | Asumir la vulneración | La actividad de los agentes se registra fuera de su alcance, se vigila y puede detenerse y revertirse. | K53 · K167 · K175 | Provisoria |

## 5. Qué es firme y qué es provisorio

36 de los 42 criterios se apoyan en publicaciones finales. Los 6 de IA y agentes, 16 de los 224 indicadores y los 12 resultados clave del frente F6 se apoyan en borradores, en guía de Microsoft y en pre-ensayos de GM-24. En los libros y en los archivos HTML están marcados «Provisoria».

**Qué haría revisarlos:** la publicación final de cualquiera de los documentos de NIST sobre agentes; un estándar de The Open Group que trate la IA o la versión final de su modelo de referencia; y los anuncios de Microsoft Ignite (17 al 20 de noviembre de 2026), que afectan a la edición Microsoft y no a este núcleo.

## 6. Cómo se usa en el plan

- **En el diagnóstico**: la hoja Zero Trust del libro de diagnóstico califica los criterios con la escala de evidencia.
- **En los OKR**: el frente F3 lleva la arquitectura a los servicios de identificar y proteger; el frente F6, a la IA y a los agentes.
- **En los indicadores**: cada indicador de operación indica su dominio Zero Trust.
- **En la escala de autonomía**: un agente sube de nivel solo si cumple la condición de ese nivel.

| Nivel | Qué puede hacer | Condición para habilitarlo |
|:--:|---|---|
| L0 | Solo informa | Ficha del agente e identidad de lectura. |
| L1 | Propone; la persona ejecuta | Además, evaluación de calidad. |
| L2 | Propone y ejecuta tras aprobación humana registrada | Además, límites de lote, detención de emergencia probada y prueba adversarial. |
| L3 | Ejecuta acciones reversibles y de bajo impacto, con auditoría posterior por muestreo | Además, indicadores de riesgo con umbrales, revisión trimestral y autorización formal. |
| L4 | Autónomo con límites estrictos | No previsto en este plan. |

## 7. Fuentes

| N.º | Organización | Documento | Estado | Fecha | Verificada | Enlace |
|:--:|---|---|---|---|---|---|
| Z01 | NIST | SP 800-207 · Zero Trust Architecture | final | 2020-08-11 | Sí | https://csrc.nist.gov/pubs/sp/800/207/final |
| Z02 | NIST | SP 800-207A · A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Cloud Environments | final | 2023-09-13 | Sí | https://csrc.nist.gov/pubs/sp/800/207/a/final |
| Z03 | NIST | SP 1800-35 · Implementing a Zero Trust Architecture: High-Level Document | final | 2025-06-10 | Sí | https://csrc.nist.gov/pubs/sp/1800/35/final |
| Z04 | NIST | CSWP 20 · Planning for a Zero Trust Architecture: A Planning Guide for Federal Administrators | final | 2022-05-06 | Sí | https://csrc.nist.gov/pubs/cswp/20/planning-for-a-zero-trust-architecture/final |
| Z05 | NIST | Concept paper NCCoE · Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization | borrador | 2026-02-05 | Sí | https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd |
| Z06 | NIST | Proyecto NCCoE · NCCoE Agentic AI Identity and Authorization Project Resource Hub | en curso | 2026-11-15 | Sí | https://pages.nist.gov/nccoe-ai-identity/index.html |
| Z07 | NIST | Blog NIST · Design Tenets for Agent Identity Management Systems | propuesta (blog) | 2026-10-27 | Sí | https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems |
| Z08 | NIST | Blog NIST · Back to the Future: Why Agentic AI Needs a Strong Identity Foundation | publicado (blog) | 2026-08-27 | Sí | https://www.nist.gov/blogs/cybersecurity-insights/back-future-why-agentic-ai-needs-strong-identity-foundation |
| Z09 | NIST | COSIS (antes COSAiS) · SP 800-53 Control Overlays for Super Intelligence Systems | en desarrollo (concept paper y esquema anotado) | 2026-10-20 | Sí | https://csrc.nist.gov/projects/cosis |
| Z10 | NIST | IR 8596 iprd · Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile): NIST Community Profile | borrador preliminar | 2025-12-16 | Sí | https://csrc.nist.gov/pubs/ir/8596/iprd |
| Z11 | NIST | AI 100-1 · Artificial Intelligence Risk Management Framework (AI RMF 1.0) | final (en revisión) | 2023-01-26 | Sí | https://www.nist.gov/itl/ai-risk-management-framework |
| Z12 | NIST | AI 600-1 · Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile | final | 2024-07-26 | Sí | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence |
| Z13 | NIST | AI 800-5 · Summary Analysis of Responses to the Request for Information Regarding Security Considerations for AI Agents | publicado | 2026-05-18 | Sí | https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai |
| Z14 | NIST | CAISI · AI Agent Standards Initiative | en curso | 2026-08-14 | Sí | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative |
| Z15 | The Open Group | no verificado · Zero Trust Commandments (Standard) | estándar vigente | no verificada | No | https://www.opengroup.org/forum/security/Zerotrust |
| Z16 | The Open Group | no verificado · Zero Trust Core Principles (White Paper) | reemplazado | no verificada | No | https://www.opengroup.org/forum/security/Zerotrust |
| Z17 | The Open Group | no verificado · Zero Trust Reference Model, Snapshot Version 1.0 | snapshot (v2.0 en desarrollo) | no verificada | No | https://www.opengroup.org/forum/security-forum-0/zerotrustsecurityarchitecture |
| Z18 | The Open Group | Acta · Security Forum Members' Meeting, Houston Summit 2025 | publicado | 2025-11 | Sí | https://www.opengroup.org/events/Houston-2025-11/Security |
| Z19 | Microsoft | Learn · Zero Trust as a security foundation | publicado | 2026-11-15 | Sí | https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview |
| Z20 | Microsoft | Learn · Zero Trust adoption framework overview | publicado | 2025-05-05 | Sí | https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview |
| Z21 | Microsoft | Learn (SAF) · Secure AI with Zero Trust | publicado | no visible | Sí | https://learn.microsoft.com/en-us/security/saf/technologies/ai/overview |
| Z22 | Microsoft | Learn · Microsoft Zero Trust Workshop - AI security | publicado | no visible | Sí | https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security |
| Z23 | Microsoft | Learn · Zero Trust Assessment - AI pillar | publicado (algunas capacidades en vista previa pública) | no visible | Sí | https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar |
| Z24 | Microsoft | Learn · AI Defense Capabilities for Enterprise AI Security | publicado | 2026-08-01 | Sí | https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities |
| Z25 | Microsoft | Learn (SFI) · Secure autonomous agentic AI systems | publicado | no visible | Sí | https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems |
| Z26 | Microsoft | Learn (SFI) · Least privilege for AI agents with Microsoft Entra Agent ID | publicado | no visible | Sí | https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents |
| Z27 | Microsoft | Learn (SFI) · Microsoft Secure Future Initiative (SFI) overview | publicado | no visible | Sí | https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-future-initiative-overview |
| Z28 | Microsoft | Blog · New tools and guidance: Announcing Zero Trust for AI | publicado | 2026-03-19 | Sí | https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/ |
| Z29 | Microsoft | Blog · Advance Zero Trust for AI: New tools and guidance to secure AI agents and DevSecOps | publicado | 2026-08-04 | Sí | https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/ |
| Z30 | Microsoft | Learn (SAF) · Map The Open Group Zero Trust model to SAF | publicado | 2026-11-15 | Sí | https://learn.microsoft.com/en-us/security/saf/framework-mappings/open-group-zero-trust |
| Z31 | Microsoft | no abierto · Zero Trust reference architecture for AI | anunciado | 2026-03-19 | No | https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/ |
| Z32 | CISA (derivado) | ZTMM v2.0 · Zero Trust Maturity Model Version 2.0 | final | 2023-04-11 | Sí | https://www.cisa.gov/resources-tools/resources/zero-trust-maturity-model |
| Z33 | DoD (derivado) | ZT RA v2.0 · Department of Defense (DoD) Zero Trust Reference Architecture Version 2.0 | final | 2022-07 | Sí | https://dodcio.defense.gov/Portals/0/Documents/Library/%28U%29ZT_RA_v2.0%28U%29_Sep22.pdf |
| Z34 | DoD (derivado) | ZT Strategy · DoD Zero Trust Strategy (placemats) | final | no verificada | No | https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-StrategyPlacemats.pdf |

El informe completo de la investigación está en el archivo `zero_trust_ia_investigacion.md`, en la carpeta de resultados de la tarea.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

# Evaluaciones y respuestas

*Microsoft Defender for Cloud Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Base · Fundamentos y despliegue

**1. En el modelo de responsabilidad compartida, ¿qué queda siempre bajo tu responsabilidad, uses IaaS, PaaS o SaaS?**

- a) Los datos, los dispositivos y las cuentas e identidades  ✅
- b) La seguridad física de los centros de datos
- c) La actualización del hipervisor de los hosts
- d) La red física del proveedor

*Respuesta: a).* En todos los modelos de servicio conservas la responsabilidad sobre la información y los datos, los dispositivos y las cuentas e identidades. La seguridad física, los hosts y la red física son del proveedor de nube; por eso la configuración y los accesos que Defender for Cloud evalúa son tuyos. [Fuente](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) · Repasa [P0](01_Nivel_1_Base.md#p0)

**2. Un servidor local conectado con Azure Arc deja de enviar latidos. ¿Qué ocurre si sigue desconectado 45 días?**

- a) Se elimina automáticamente de la suscripción
- b) Se factura el doble cuando se reconecta
- c) Pasa al estado Expired y hay que volver a conectarlo  ✅
- d) Sigue protegido por Defender for Servers con normalidad

*Respuesta: c).* El agente de Arc envía un latido cada 5 minutos; sin latido, el servidor pasa a Disconnected a los 15-30 minutos y a Expired tras 45 días, cuando hay que reconectarlo. Un servidor de Arc solo se factura en Defender for Servers mientras está Connected. [Fuente](https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview) · Repasa [P0](01_Nivel_1_Base.md#p0)

**3. ¿Qué certificación asociada está más alineada con este programa tras el retiro del examen AZ-500?**

- a) SC-200 (Security Operations Analyst)
- b) SC-500 (Cloud and AI Security Engineer Associate)  ✅
- c) AZ-104 (Azure Administrator)
- d) SC-100 (Cybersecurity Architect)

*Respuesta: b).* El curso y el examen AZ-500 se retiraron el 31 de agosto de 2026 y su reemplazo es SC-500, «Implementing End-to-End Security Controls for Cloud and AI Workloads». Sus dominios incluyen Defender CSPM, los planes de protección de cargas, los conectores de AWS y GCP y Defender for Servers, Containers y AI Services; se aprueba con 700 puntos. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500) · Repasa [B0](01_Nivel_1_Base.md#b0)

**4. ¿Cuál de estas tareas solo puedes hacer hoy en el portal de Azure?**

- a) Ver las alertas de Defender for Cloud
- b) Revisar las rutas de ataque
- c) Consultar la Cloud Secure Score
- d) Usar Cloud Security Explorer y crear reglas de gobernanza  ✅

*Respuesta: d).* Cloud Security Explorer, las reglas de gobernanza, el quick fix y las recomendaciones personalizadas con KQL solo existen en el portal de Azure. Las alertas y las rutas de ataque se ven en ambos portales, y la Cloud Secure Score basada en riesgo vive en el portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/azure-portal-vs-defender-portal-comparison) · Repasa [B1](01_Nivel_1_Base.md#b1)

**5. Usas Plan 1 en algunas VM y Plan 2 en otras de la misma suscripción, con configuración por recurso. ¿Qué pasa si migras esa suscripción al modelo DWU del portal de Defender?**

- a) La configuración por recurso se conserva y se factura en DWU
- b) Los planes se siguen cambiando desde el portal de Azure
- c) La configuración por recurso no se conserva y el portal de Azure queda en solo lectura  ✅
- d) Puedes revertir la migración desde Environment settings

*Respuesta: c).* En el modelo DWU (vista previa desde el 20 de octubre de 2026) la configuración por recurso no se preserva, la gestión de planes pasa al portal de Defender y el portal de Azure queda en solo lectura. Por eso el programa trata el modelo DWU como piloto: inventaría antes las excepciones por recurso. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/plan-management-changes-defender-portal) · Repasa [B1](01_Nivel_1_Base.md#b1)

**6. ¿Dónde ves la Cloud Secure Score basada en riesgo?**

- a) En el portal de Defender, dentro de Exposure Management  ✅
- b) En el portal de Azure, en Environment settings
- c) En un workbook integrado de Azure Monitor
- d) En el portal de cumplimiento de Microsoft Purview

*Respuesta: a).* La Cloud Secure Score basada en riesgo vive en el portal de Defender, en Exposure Management, y es GA desde el 5 de mayo de 2026; la Secure Score clásica sigue en el portal de Azure. Son cifras distintas: no las mezcles en un mismo informe. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) · Repasa [B2](01_Nivel_1_Base.md#b2)

**7. ¿Qué condición se cumple al crear exenciones en Defender for Cloud?**

- a) Aplican también a las recomendaciones personalizadas con KQL
- b) Requieren el estándar MCSB asignado y admiten hasta 5.000 recursos exentos por suscripción  ✅
- c) Solo se pueden crear en el portal de Defender
- d) Una recomendación exenta sigue restando puntos en la puntuación

*Respuesta: b).* Las exenciones requieren el MCSB asignado, admiten hasta 5.000 recursos exentos por suscripción y no aplican a recomendaciones personalizadas. Una recomendación exenta deja de afectar la puntuación; el portal de Defender también las gestiona, en vista previa, pero no es el único lugar. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/exempt-resource) · Repasa [B2](01_Nivel_1_Base.md#b2)

**8. Planeas conectar tu organización de AWS. ¿Qué situación no admite el conector de Defender for Cloud?**

- a) Usar la cuenta de administración de AWS Organizations
- b) Elegir el modo de acceso Least privilege
- c) Fijar el intervalo de escaneo en 12 horas
- d) Conectarte desde una cuenta de administrador delegado o en una nube gubernamental de AWS  ✅

*Respuesta: d).* El conector de AWS admite una cuenta única o la cuenta de administración (con StackSet para las cuentas miembro), los modos Default y Least privilege y un intervalo de 4, 6, 12 o 24 horas. No admite cuentas de administrador delegado ni nubes gubernamentales. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-aws) · Repasa [B3](01_Nivel_1_Base.md#b3)

**9. ¿Cómo se autentica Defender for Cloud ante GCP cuando creas el conector?**

- a) Con una clave JSON de cuenta de servicio que subes al portal
- b) Con un usuario de Google Workspace con rol Owner
- c) Con federación de identidades de carga de trabajo y suplantación de cuentas de servicio  ✅
- d) Con un token personal que caduca a los 90 días

*Respuesta: c).* El script de gcloud del conector configura la federación de identidades de carga de trabajo y las cuentas de servicio que Defender for Cloud suplanta, sin claves de larga duración. Antes, habilita las APIs iam, sts, cloudresourcemanager, iamcredentials y compute. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-gcp) · Repasa [B3](01_Nivel_1_Base.md#b3)

**10. ¿Cuál de estas capacidades requiere Defender for Servers Plan 2?**

- a) File Integrity Monitoring (FIM)  ✅
- b) La integración con Defender for Endpoint
- c) La evaluación de vulnerabilidades con el agente de Defender for Endpoint
- d) Las alertas de seguridad de servidores

*Respuesta: a).* FIM es exclusiva de Plan 2, igual que JIT, el escaneo de malware sin agente y el beneficio de 500 MB por nodo y día. La integración con Defender for Endpoint, las alertas y la evaluación de vulnerabilidades con agente ya vienen en Plan 1. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-overview) · Repasa [B4](01_Nivel_1_Base.md#b4)

**11. ¿Qué cambió en la facturación de Defender for Servers el 1 de noviembre de 2026?**

- a) Plan 2 empezó a cobrar las VM desasignadas
- b) Plan 1 dejó de incluir la licencia de Defender for Endpoint
- c) Los servidores de Arc en Expired empezaron a facturarse
- d) Plan 1 dejó de facturar dispositivos cliente, como Windows 10/11 y Azure Virtual Desktop multisesión  ✅

*Respuesta: d).* Desde el 1 de noviembre de 2026, Plan 1 no factura dispositivos cliente; los Linux con Plan 1 solo se cobran cuando tienen desplegado el agente de Defender for Endpoint, y los clones que comparten ID de Arc se cuentan por separado en Plan 1 y Plan 2. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Repasa [B4](01_Nivel_1_Base.md#b4)

**12. ¿Qué característica de Direct onboarding debes considerar antes de activarlo?**

- a) Instala el agente de Azure Arc en cada servidor
- b) Aplica a todos los servidores elegibles del inquilino, sin opción de piloto  ✅
- c) Solo funciona con VM de Azure
- d) Asigna a los servidores las directivas de Azure Policy

*Respuesta: b).* Direct onboarding (GA) lleva a Defender for Cloud los servidores que ya reportan a Defender for Endpoint, sin instalar agentes ni Arc. Aplica a todos los servidores elegibles del inquilino, actuales y futuros, sin piloto; requiere Owner en la suscripción y Security Administrator, y no ofrece Azure Policy. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/onboard-machines-with-defender-for-endpoint) · Repasa [B4](01_Nivel_1_Base.md#b4)

**13. ¿Qué componente se cobra desde el primer día, sin el período gratuito de 30 días?**

- a) Defender CSPM
- b) Defender for Key Vault
- c) El escaneo de malware de Defender for Storage  ✅
- d) Defender for Resource Manager

*Respuesta: c).* Los planes son gratuitos los primeros 30 días, salvo el escaneo de malware de Storage, que cuesta 0,15 USD por GB desde el primer día, y Defender for AI Services, cuya prueba termina a los 30 días o a los 75.000 millones de tokens. [Fuente](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/) · Repasa [B5](01_Nivel_1_Base.md#b5)

**14. ¿Qué rol indica la documentación para generar alertas de ejemplo desde la página de alertas de seguridad?**

- a) Subscription Contributor  ✅
- b) Security Reader
- c) Global Reader
- d) Log Analytics Reader

*Respuesta: a).* Las alertas de ejemplo se crean desde Security alerts > Sample alerts con el rol Subscription Contributor. Sirven para validar notificaciones, exportación continua y la cola del portal de Defender sin tocar cargas reales; ciérralas como prueba al terminar. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alert-validation) · Repasa [B6](01_Nivel_1_Base.md#b6)

**15. Quieres probar el escaneo sin agente de Servers Plan 2 en VM cercanas a tus usuarios. Según la disponibilidad regional publicada, ¿qué región no lo admite?**

- a) Brazil South
- b) Chile Central
- c) Ninguna: está disponible en todas las regiones de Azure
- d) Mexico Central  ✅

*Respuesta: d).* La página de disponibilidad regional indica que el escaneo sin agente de Servers Plan 2 no se admite en Mexico Central y sí en Brazil South y Chile Central; además, Defender for Storage no está disponible en Chile Central. Revisa la región plan por plan antes de diseñar el laboratorio. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regional-availability) · Repasa [B7](01_Nivel_1_Base.md#b7)

<a id="eval-intermedio"></a>

## Nivel 2 · Avanzado · Diseñar, desplegar y operar

**1. En una arquitectura de Azure Landing Zones, ¿dónde se asignan las iniciativas de Defender for Cloud?**

- a) En el Tenant Root Group
- b) En el grupo de administración raíz intermedio de la organización  ✅
- c) En cada suscripción, una por una
- d) En los grupos de recursos de cada carga

*Respuesta: b).* ALZ asigna sus iniciativas, incluida Deploy-MDFC-Config y las del MCSB, en el grupo raíz intermedio que cuelga del Tenant Root Group, nunca en este. Así controlas el alcance y no afectas suscripciones fuera de la plataforma. [Fuente](https://azure.github.io/Azure-Landing-Zones/policy/policyassignments/) · Repasa [M1](02_Nivel_2_Avanzado.md#m1)

**2. ¿Qué riesgo tiene adoptar Enterprise Policy as Code (EPAC) sin preparación?**

- a) No admite las iniciativas de Azure Landing Zones
- b) Solo funciona con Terraform
- c) Obliga a deshabilitar Defender for Cloud durante la migración
- d) Trata Azure Policy como estado deseado y puede eliminar asignaciones que no estén declaradas  ✅

*Respuesta: d).* EPAC gestiona Azure Policy como estado deseado desde CI/CD: toma posesión de los recursos de Policy de su alcance y elimina lo no declarado. Haz el piloto en un grupo de administración de prueba, con keepDfcSecurityAssignments activado, efectos Audit y aprobación manual en el pipeline. [Fuente](https://azure.github.io/enterprise-azure-policy-as-code/) · Repasa [M1](02_Nivel_2_Avanzado.md#m1)

**3. Una suscripción tiene 16 Function Apps con serverless protection activado en Defender CSPM. ¿Cuántos recursos facturables suman?**

- a) 16
- b) 8
- c) 2  ✅
- d) Ninguno: las funciones no se cobran

*Respuesta: c).* En Defender CSPM, 8 Function Apps o Web Apps equivalen a 1 recurso facturable (con cobro desde el 1 de abril de 2026), así que 16 suman 2. Los contenedores serverless cuentan 2 en ejecución por 1, y el precio de lista es de 5,11 USD por recurso facturable al mes. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) · Repasa [M2](02_Nivel_2_Avanzado.md#m2)

**4. ¿Qué rutas de ataque muestra Defender CSPM?**

- a) Solo escenarios externos y explotables que llegan a activos críticos  ✅
- b) Todas las configuraciones incorrectas, sin importar su exposición
- c) Solo las rutas que el SOC marca a mano
- d) Las de cualquier recurso, aunque no tenga escaneo sin agente ni evaluación de vulnerabilidades

*Respuesta: a).* Las rutas de ataque solo muestran escenarios externos y explotables, validados con escaneos activos de alcanzabilidad desde el punto de entrada. Dependen del escaneo sin agente o de la evaluación de vulnerabilidades de Servers; sin datos de las máquinas, la ruta no se calcula. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path) · Repasa [M2](02_Nivel_2_Avanzado.md#m2)

**5. ¿Con qué frecuencia toma instantáneas de disco el escaneo sin agente de máquinas?**

- a) Cada hora, en cuanto cambia el disco
- b) Una vez cada 24 horas, en un horario que no se puede cambiar  ✅
- c) Cada 4, 6, 12 o 24 horas, según el intervalo del conector
- d) Solo cuando la VM se reinicia

*Respuesta: b).* El escaneo sin agente toma instantáneas una vez cada 24 horas, sin opción de cambiar la frecuencia, y solo escanea las máquinas encendidas en ese momento. El intervalo de 4 a 24 horas es el del escaneo del conector de AWS, no el de los discos. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-agentless-scanning-vms) · Repasa [M3](02_Nivel_2_Avanzado.md#m3)

**6. ¿Qué plan necesitas para el escaneo de malware sin agente en los discos de las VM?**

- a) Foundational CSPM
- b) Defender CSPM
- c) Defender for Servers Plan 1
- d) Defender for Servers Plan 2  ✅

*Respuesta: d).* El escaneo de malware sin agente de máquinas es exclusivo de Servers Plan 2 (en los nodos de Kubernetes también lo da Defender for Containers). Da visibilidad periódica, no protección en tiempo real: la prevención sigue a cargo del antivirus del sensor de Defender for Endpoint. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/agentless-malware-scanning) · Repasa [M3](02_Nivel_2_Avanzado.md#m3)

**7. Habilitaste Plan 2 en la suscripción y creaste una DCR que envía SecurityEvent al área de trabajo, pero el beneficio de 500 MB no aparece. ¿Qué falta?**

- a) Habilitar Plan 2 también en el área de trabajo de Log Analytics  ✅
- b) Mover el área de trabajo a una región de Estados Unidos
- c) Convertir la DCR en una regla de recopilación personalizada de Defender for Endpoint
- d) Esperar a la factura, donde el beneficio aparece como descuento

*Respuesta: a).* El beneficio de 500 MB por nodo y día exige Plan 2 habilitado en el área de trabajo y datos enviados por un método admitido; la DCR sola no lo activa. No aparece en la factura: se ve con el medidor «Standard Data Included per Node» en Cost Management. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/data-ingestion-benefit) · Repasa [M4](02_Nivel_2_Avanzado.md#m4)

**8. ¿Con qué controles de red funciona el acceso just-in-time (JIT)?**

- a) Con cualquier firewall de terceros desplegado en la VNet
- b) Con directivas de Azure Firewall administradas por Firewall Manager
- c) Con NSG y reglas clásicas de Azure Firewall en Azure, y con security groups en AWS (vista previa)  ✅
- d) Solo con NSG de Azure, sin opciones en AWS ni GCP

*Respuesta: c).* JIT abre reglas temporales en NSG y en Azure Firewall con reglas clásicas, no con directivas de Firewall Manager; en AWS usa security groups (vista previa) y en GCP no está disponible. Los puertos por defecto son 22, 3389, 5985 y 5986. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview) · Repasa [M4](02_Nivel_2_Avanzado.md#m4)

**9. ¿Qué necesitas para que gated deployment audite o deniegue imágenes vulnerables en AKS?**

- a) Solo Defender CSPM con el acceso al registro
- b) Kubernetes 1.27 y un plugin de network policy
- c) Azure Policy para Kubernetes con efecto Deny
- d) El sensor, Security Gating, Registry access y Security findings, con Kubernetes 1.31 o posterior y el emisor OIDC  ✅

*Respuesta: d).* Gated deployment es un admission controller que requiere el sensor, Security Gating, Registry access y Security findings, con Kubernetes 1.31 o posterior y, en AKS, el emisor OIDC. Crea por defecto una regla de auditoría para vulnerabilidades altas y críticas, y las directivas Deny sobre el clúster pueden bloquear su aprovisionamiento. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enablement-guide-runtime-gated) · Repasa [M5](02_Nivel_2_Avanzado.md#m5)

**10. Tu clúster de laboratorio no tiene plugin de network policy. ¿Qué acción de respuesta de contenedores puedes probar igualmente desde el portal de Defender?**

- a) Aislar el pod
- b) Terminar el pod  ✅
- c) Bloquear el nodo en el NSG desde el incidente
- d) Ninguna: todas requieren el plugin

*Respuesta: b).* Las acciones de respuesta (vista previa) requieren el sensor, el acceso a la API de Kubernetes y Kubernetes 1.27 o posterior; aislar el pod exige además un plugin de network policy compatible (Azure-NPM, Calico, Cilium o AWS-node). Terminar el pod no depende de ese plugin. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/investigate-respond-container-threats) · Repasa [M5](02_Nivel_2_Avanzado.md#m5)

**11. ¿Qué pasa cuando una cuenta de Storage alcanza el tope mensual del escaneo de malware al cargar?**

- a) Los blobs nuevos quedan sin escanear hasta que subas el tope o empiece el mes siguiente  ✅
- b) Los blobs nuevos se bloquean hasta fin de mes
- c) El escaneo pasa solo al modo bajo demanda
- d) Defender for Storage se deshabilita en la cuenta

*Respuesta: a).* La documentación de Defender for Storage fija un tope por defecto de 10.000 GB al mes por cuenta, configurable por suscripción o cuenta, con alertas al 75 % y al alcanzarlo. Al superarlo, los blobs nuevos quedan sin escanear: ajusta el tope y escanea lo pendiente bajo demanda. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-storage-introduction) · Repasa [M6](02_Nivel_2_Avanzado.md#m6)

**12. Una suscripción nueva necesita las detecciones de Defender for DNS. ¿Cómo las obtienes?**

- a) Habilitando el plan Defender for DNS por API
- b) Con Defender for Resource Manager
- c) Con Defender for Servers Plan 2, que incluye las alertas de DNS  ✅
- d) Con Defender CSPM

*Respuesta: c).* Desde el 1 de agosto de 2023, las alertas de DNS vienen en Servers Plan 2 para suscripciones nuevas. El plan independiente es legado: no admite altas por API desde el 5 de julio de 2026 y se discontinúa en el modelo DWU. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-dns-introduction) · Repasa [M7](02_Nivel_2_Avanzado.md#m7)

**13. ¿Cuál de estas capacidades de DevOps security requiere Defender CSPM?**

- a) Conectar repositorios de GitHub y ver su inventario
- b) Las anotaciones de pull request y el mapeo del código al runtime  ✅
- c) Las recomendaciones de configuración del entorno DevOps
- d) Los hallazgos de IaC del escaneo sin agente

*Respuesta: b).* Conectar repositorios, el inventario y las recomendaciones de postura de DevOps son gratis con Foundational CSPM. Las anotaciones de pull request, el mapeo code-to-cloud, las rutas de ataque y Cloud Security Explorer requieren Defender CSPM; los repositorios no son recursos facturables. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/devops-support) · Repasa [M8](02_Nivel_2_Avanzado.md#m8)

**14. Resuelves en el portal de Defender una alerta de Defender for Endpoint sobre una VM de Azure. ¿Qué ves en Defender for Cloud, en el portal de Azure?**

- a) La alerta aparece resuelta al instante
- b) La alerta desaparece de Defender for Cloud
- c) La alerta se reabre automáticamente
- d) Su estado no se sincroniza: puede seguir activa en el portal de Azure  ✅

*Respuesta: d).* El estado de las alertas de Defender for Cloud se sincroniza entre ambos portales, pero el de las alertas de Defender for Endpoint sobre recursos de nube no. Durante el piloto, verifica el estado en ambos lados y define el portal de Defender como cola principal del SOC. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-integration-365) · Repasa [M9](02_Nivel_2_Avanzado.md#m9)

**15. Creas una regla de alert tuning en el portal de Defender para alertas de Defender for Cloud. ¿Qué acción puede aplicar?**

- a) Resolve  ✅
- b) Hide
- c) Set as behavior
- d) Delete

*Respuesta: a).* Para alertas de Defender for Cloud, alert tuning solo aplica Resolve: Hide es exclusivo de Defender for Endpoint y Set as behavior no aplica a Defender for Cloud. Si necesitas descartar por suscripción o grupo de administración, usa las reglas de supresión de Defender for Cloud y elige una sola fuente de verdad. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) · Repasa [M9](02_Nivel_2_Avanzado.md#m9)

<a id="eval-avanzado"></a>

## Nivel 3 · Experto · Proteger la IA, responder y automatizar

**1. ¿Qué plan necesitas para usar AI-SPM (AI BOM, recomendaciones de IA y rutas de ataque hacia cargas de IA)?**

- a) Foundational CSPM
- b) Defender CSPM  ✅
- c) Defender for AI Services
- d) Defender for Servers Plan 2

*Respuesta: b).* AI-SPM es una capacidad de Defender CSPM en Azure, AWS y GCP; Foundational CSPM no la incluye. Defender for AI Services es la detección de amenazas en runtime: otra compra distinta sobre el mismo activo. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) · Repasa [A1](03_Nivel_3_Experto.md#a1)

**2. Desde el 1 de julio de 2026, ¿qué activo ya no descubre Defender CSPM por sí solo?**

- a) Cuentas de Microsoft Foundry
- b) Despliegues de Amazon Bedrock
- c) Workspaces de Azure Machine Learning
- d) Agentes de Foundry  ✅

*Respuesta: d).* El descubrimiento y la postura de agentes de Foundry y de agentes de nube de terceros exigen Microsoft Agent 365. Defender CSPM sigue descubriendo cuentas y proyectos de Foundry, Bedrock, Vertex AI y Azure Machine Learning. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) · Repasa [A1](03_Nivel_3_Experto.md#a1)

**3. ¿Qué agente de Security Copilot clasifica hoy las alertas de nube y de contenedores de Defender for Cloud?**

- a) El Security Alert Triage Agent, en preview para nube y con Defender for Cloud y Defender for Containers como requisitos  ✅
- b) Un agente propio de Defender for Cloud incluido en Defender CSPM
- c) El Dynamic Threat Detection Agent, que ya consume SCU en GA
- d) Ninguno: Security Copilot no trabaja con alertas de nube

*Respuesta: a).* No existe un agente de Security Copilot específico de Defender for Cloud. El Security Alert Triage Agent es GA para correo y está en preview para nube; el Dynamic Threat Detection Agent es una preview gratuita que consumirá SCU en GA. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [A6](03_Nivel_3_Experto.md#a6)

**4. Aparece la alerta `AI.Azure_Jailbreak.ContentFiltering.DetectedAttempt`. ¿Qué significa?**

- a) Prompt Shields bloqueó el intento
- b) Se filtró una credencial en la respuesta del modelo
- c) Prompt Shields detectó el intento, pero no lo bloqueó por la configuración del filtro o por baja confianza  ✅
- d) Se subió un modelo con malware al registro

*Respuesta: c).* Es la variante «detectada»; la variante BlockedAttempt indica bloqueo. Revisa qué respondió el modelo y cambia el guardrail a bloqueo en ese despliegue. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) · Repasa [A2](03_Nivel_3_Experto.md#a2)

**5. Un desarrollador escribe mal un campo de `UserSecurityContext` en la llamada a Azure OpenAI. ¿Qué ocurre?**

- a) La API devuelve un error 400
- b) Defender bloquea la llamada
- c) Prompt Shields se desactiva para esa sesión
- d) La llamada funciona, pero las alertas pierden ese contexto sin ningún aviso  ✅

*Respuesta: d).* La API no valida los nombres de los campos, así que el contexto se pierde en silencio: valida siempre con una alerta de prueba. Además, el contexto del usuario no funciona con la Azure AI Model Inference API. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai) · Repasa [A2](03_Nivel_3_Experto.md#a2)

**6. Desactivas la evidencia de prompts sospechosos de Defender for AI Services. ¿Qué pasa?**

- a) Defender sigue analizando prompts y respuestas y alertando, pero enmascara el contenido en la alerta  ✅
- b) Defender deja de analizar los prompts
- c) Se borran las alertas anteriores
- d) Purview deja de auditar las interacciones

*Respuesta: a).* La detección continúa; solo cambia lo que muestra la alerta. Con la evidencia activa, los fragmentos redactados son datos del cliente visibles en ambos portales y en las integraciones de socios conectadas. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-onboarding) · Repasa [A2](03_Nivel_3_Experto.md#a2)

**7. Desde el 1 de septiembre de 2026, ¿cómo investigas bajo demanda un servidor protegido por Defender for Endpoint?**

- a) Inicias una investigación automatizada (AIR) desde la página del dispositivo
- b) Lanzas un examen antivirus completo, porque AIR ya no se inicia a mano  ✅
- c) Abres un caso con Microsoft Incident Response
- d) Habilitas Defender Experts for Servers

*Respuesta: b).* AIR dejó de ser una experiencia separada y corre dentro del antivirus; para investigar bajo demanda lanzas un examen completo. El Action center conserva aprobación, historial y deshacer. [Fuente](https://learn.microsoft.com/en-us/defender-endpoint/automated-investigations) · Repasa [A3](03_Nivel_3_Experto.md#a3)

**8. En el caso Storm-0501 de ransomware en la nube, ¿qué controles impidieron que el atacante borrara parte de los datos?**

- a) MFA para todos los usuarios
- b) Grupos de seguridad de red
- c) Acceso a VM just-in-time
- d) Bloqueos de recursos de Azure e inmutabilidad de Storage  ✅

*Respuesta: d).* El atacante pivotó de AD a Entra ID, abusó del rol Owner, obtuvo claves de Storage, exfiltró y borró recursos y backups; los bloqueos de recursos y la inmutabilidad frenaron parte del borrado. [Fuente](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/) · Repasa [A3](03_Nivel_3_Experto.md#a3)

**9. ¿Para qué repositorios genera Defender for Cloud rutas de ataque a partir de secretos expuestos en el código?**

- a) Solo para GitHub
- b) Para GitHub, GitLab y Azure DevOps
- c) Solo para Azure DevOps  ✅
- d) Para ninguno: los secretos de código nunca generan rutas

*Respuesta: c).* Los hallazgos de secretos de código se ven con Foundational CSPM (con GitHub Advanced Security), pero las rutas de ataque por secretos solo existen para repositorios de Azure DevOps. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secrets-scanning-code) · Repasa [A9](03_Nivel_3_Experto.md#a9)

**10. ¿Qué vía recomienda Microsoft en noviembre de 2026 para llevar Defender for Cloud a Microsoft Sentinel?**

- a) La integración de incidentes de Defender XDR más el conector Tenant-based Microsoft Defender for Cloud (preview), sin el conector heredado  ✅
- b) El conector Subscription-based (Legacy) en cada suscripción
- c) Solo la exportación continua a Log Analytics
- d) El conector Azure Activity

*Respuesta: a).* El conector heredado por suscripción no se recomienda: puede duplicar alertas o dejar incidentes con alertas vacías. Desconéctalo y desactiva las reglas que crean incidentes desde estas alertas. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ingest-defender-for-cloud-incidents) · Repasa [A4](03_Nivel_3_Experto.md#a4)

**11. ¿Después de qué fecha Microsoft Sentinel solo estará disponible en el portal de Defender?**

- a) 1 de julio de 2026
- b) 31 de marzo de 2027  ✅
- c) 31 de diciembre de 2026
- d) 1 de julio de 2027

*Respuesta: b).* Después del 31 de marzo de 2027, Sentinel deja el portal de Azure; los workspaces incorporados desde el 1 de julio de 2025 por Owner o User Access Administrator ya quedan en el portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender) · Repasa [A4](03_Nivel_3_Experto.md#a4)

**12. ¿Qué tipo de Logic App puede disparar workflow automation de Defender for Cloud?**

- a) Standard
- b) Standard y Consumo
- c) Consumo (Consumption)  ✅
- d) Azure Functions

*Respuesta: c).* Workflow automation solo dispara Logic Apps de Consumo ante alertas, recomendaciones y evaluaciones de cumplimiento; para Standard, dispara desde Sentinel o desde una Logic App de Consumo intermedia. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/workflow-automations) · Repasa [A5](03_Nivel_3_Experto.md#a5)

**13. ¿Qué incluye Microsoft 365 E5 respecto de Security Copilot?**

- a) Nada: Security Copilot siempre se compra aparte
- b) SCU ilimitadas para Defender for Cloud
- c) 400 SCU al mes por inquilino, también en inquilinos de prueba
- d) 400 SCU al mes por cada 1.000 licencias de usuario pagadas, con tope de 10.000, sin incluir los planes de Defender for Cloud  ✅

*Respuesta: d).* La inclusión se calcula sobre licencias pagadas (un inquilino de prueba no recibe SCU), no se acumula y no incluye prerrequisitos fuera de E5 o E7, como los planes de Defender for Cloud. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [A6](03_Nivel_3_Experto.md#a6)

**14. Desde el 21 de agosto de 2026, ¿dónde se leen los detalles de CVE en Azure Resource Graph?**

- a) En las sub-evaluaciones de las recomendaciones agrupadas
- b) En el tipo `microsoft.security/cvedetails`  ✅
- c) En el tipo `microsoft.security/locations/alerts`
- d) Solo en la tabla DeviceTvmSoftwareVulnerabilities

*Respuesta: b).* Las recomendaciones agrupadas (sub-assessments) se retiraron el 31 de julio de 2026 y los detalles de CVE pasaron al tipo `microsoft.security/cvedetails`: actualiza tus consultas y tableros. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Repasa [A7](03_Nivel_3_Experto.md#a7)

**15. Migras la gestión de planes de una suscripción al portal de Defender (preview). ¿Qué pasa con Servers P1 habilitado por etiqueta en algunas VM?**

- a) No se conserva: la configuración queda por inquilino, grupo de administración o suscripción y el portal de Azure pasa a solo lectura  ✅
- b) Se conserva y se convierte en DWU por recurso
- c) Se exporta a Azure Policy en modo Audit
- d) Se mantiene editable en el portal de Azure

*Respuesta: a).* El modelo DWU no admite ni conserva configuraciones por recurso y no hay reversión documentada: evalúalo en una suscripción piloto, con el Cloud Security Cost Estimator, y trátalo como irreversible. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-portal/plan-management-changes-defender-portal) · Repasa [A8](03_Nivel_3_Experto.md#a8)

<a id="eval-workload"></a>

## Track · Especialización por workload · De cero a experto en cada plan

**1. Una regla de gated deployment en Deny no bloqueó una imagen con CVE críticos que se subió a ACR y se desplegó diez minutos después en un AKS 1.32 con el sensor, Security Gating, Registry access y Security findings activos. ¿Cuál es la causa más probable?**

- a) El gating exige Kubernetes 1.30 o anterior
- b) La imagen aún no tenía resultados de escaneo ni artefacto de hallazgos y la regla no tenía activada la opción «Block all deployments with missing artifacts»  ✅
- c) El sensor está instalado con Helm en el espacio de nombres mdc
- d) Falta habilitar Defender CSPM en la suscripción

*Respuesta: b).* Sin resultados de escaneo ni artefacto firmado (pestaña Referrers de ACR), el gating no aplica la regla salvo que actives el bloqueo de despliegues con artefactos faltantes, y una imagen nueva tarda unas horas en escanearse. El gating requiere Kubernetes 1.31 o posterior, así que 1.32 es válido, y no depende de Defender CSPM. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/troubleshooting-runtime-gated) · Repasa [W1](03b_Track_Especializacion_por_workload.md#w1)

**2. Durante un simulacro, «Isolate pod» aparece deshabilitado para un analista de guardia y, en otro clúster, la acción falla aunque la lanza un analista con todos los permisos. ¿Qué explica ambos hechos?**

- a) Falta Defender CSPM y el clúster no está conectado con Azure Arc
- b) Falta una licencia de Security Copilot y el clúster tiene nodos Windows
- c) El primer analista no tiene Alerts (Manage) y Response (Manage) de Defender for Cloud en el RBAC unificado, y el segundo clúster no tiene un plugin de network policy soportado o usa una versión anterior a Kubernetes 1.27  ✅
- d) El antimalware no está habilitado y el clúster es privado

*Respuesta: c).* Las acciones de respuesta (vista previa) exigen los permisos Alerts (Manage) y Response (Manage) en el RBAC unificado, el sensor y Kubernetes API access; aislar y restringir requieren además Kubernetes 1.27 o posterior y un enforcer de network policy como Azure-NPM, Calico, Cilium o AWS-node. Terminar el pod funciona sin network policy, y Defender CSPM solo aporta las rutas de ataque del grafo. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/investigate-respond-container-threats) · Repasa [W1](03b_Track_Especializacion_por_workload.md#w1)

**3. Quieres revisar desde advanced hunting los cambios de clusterrolebindings de la última semana en tus clústeres protegidos, sin configurar diagnostic settings ni ingerir registros en Sentinel. ¿Qué consulta usas?**

- a) `AKSAuditAdmin | where Verb == "create"`
- b) `SecurityAlert | where AlertType startswith "K8S"`
- c) `DeviceProcessEvents | where ProcessCommandLine has "clusterrolebinding"`
- d) `CloudAuditEvents | where DataSource == "Kubernetes Audit" | where OperationName has "clusterrolebindings"`  ✅

*Respuesta: d).* `CloudAuditEvents` lleva a advanced hunting el registro de auditoría de Kubernetes que recoge Defender for Cloud (DataSource «Kubernetes Audit»). `AKSAuditAdmin` solo existe si envías kube-audit-admin a Log Analytics y solo cubre AKS; `SecurityAlert` contiene alertas, no eventos de auditoría, y `DeviceProcessEvents` es de endpoints. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-cloudauditevents-table) · Repasa [W1](03b_Track_Especializacion_por_workload.md#w1)

**4. Configuraste una condición ABAC que solo permite leer blobs con la etiqueta «No threats found», pero un socio sigue descargando el archivo EICAR con un SAS de cuenta. ¿Qué haces?**

- a) Deshabilitas la autorización con Shared Key (AllowSharedKeyAccess=false) y migras al socio a SAS de delegación de usuario, porque la condición ABAC solo se evalúa con autorización de Microsoft Entra ID  ✅
- b) Subes el tope mensual de escaneo de la cuenta
- c) Activas el análisis de reputación de hashes
- d) Cambias el nivel de acceso de la cuenta a Cool

*Respuesta: a).* Las condiciones ABAC se aplican a solicitudes autorizadas con Microsoft Entra ID; las SAS de cuenta y de servicio se firman con la clave y las evaden. Con Shared Key deshabilitado esas SAS se rechazan, mientras las de delegación de usuario siguen funcionando y se revocan todas con revokeUserDelegationKeys. El tope, la reputación de hashes y el nivel de acceso no cambian la autorización. [Fuente](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent) · Repasa [W2](03b_Track_Especializacion_por_workload.md#w2)

**5. Para ahorrar, habilitaste Defender for Storage solo en tres cuentas críticas con la configuración por cuenta. El SOC no ve datos de esas cuentas en `CloudStorageAggregatedEvents`. ¿Qué falta?**

- a) Activar los registros de diagnóstico de Blob en cada cuenta
- b) Comprar licencias adicionales de Microsoft 365 E5
- c) Conectar cada cuenta a un workspace de Log Analytics
- d) Habilitar Defender for Storage (plan nuevo) a nivel de suscripción: la tabla, en vista previa, no se llena con la habilitación por cuenta  ✅

*Respuesta: d).* `CloudStorageAggregatedEvents` (vista previa) solo recibe datos cuando el plan nuevo está habilitado en la suscripción; la habilitación por cuenta no la alimenta. No depende de los registros de diagnóstico ni de un workspace. Si eliges habilitar por cuenta para ahorrar, documenta que pierdes esta fuente de hunting. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-cloudstorageaggregatedevents-table) · Repasa [W2](03b_Track_Especializacion_por_workload.md#w2)

**6. Despliegas `Microsoft.Security/defenderForStorageSettings` por IaC en 40 cuentas con el escaneo al cargar activado, pero sin indicar `capGBPerMonth`. Según la referencia del recurso, ¿qué tope mensual queda y qué riesgo implica?**

- a) 10.000 GB por cuenta, como en el portal
- b) 5.000 GB por cuenta, como en el laboratorio oficial 19
- c) −1, es decir, sin tope: el costo del escaneo, de 0,15 USD por GB, no tiene límite  ✅
- d) 1.000 GB por cuenta

*Respuesta: c).* El portal aplica 10.000 GB por cuenta al mes, pero la referencia del recurso indica −1 (ilimitado) cuando no se especifica, y el laboratorio 19 todavía menciona 5.000 GB. Fija siempre el valor en la plantilla y vigila las alertas al 75 % y al llegar al tope. [Fuente](https://learn.microsoft.com/en-us/azure/templates/microsoft.security/defenderforstoragesettings) · Repasa [W2](03b_Track_Especializacion_por_workload.md#w2)

**7. Tu regla de automatización cierra cualquier alerta con `AlertType == "SQL.PostgreSQL_BruteForce"` después de bloquear la IP de origen. ¿Qué error de diseño tiene?**

- a) Ninguno: ese tipo solo se usa para intentos fallidos y el acceso exitoso llega como alerta de inicio de sesión anómalo
- b) Cierra también «Suspected successful brute force attack» (High), que comparte ese tipo e indica acceso exitoso: filtra por nombre y severidad  ✅
- c) Las alertas de bases de código abierto no llegan a `SecurityAlert` por la exportación continua, así que la regla nunca se ejecuta
- d) El tipo de PostgreSQL es `SQL.DB_BruteForce`, compartido con Azure SQL, así que la regla también cerraría alertas de SQL Database y de Managed Instance

*Respuesta: b).* En PostgreSQL y MySQL, «Suspected brute force attack», «Suspected brute force attack using a valid user» y «Suspected successful brute force attack» comparten el AlertType `SQL.PostgreSQL_BruteForce` o `SQL.MySQL_BruteForce`. La exitosa es High y exige rotar la credencial y revisar la actividad posterior, no cerrarla. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-open-source-relational-databases) · Repasa [W3](03b_Track_Especializacion_por_workload.md#w3)

**8. Llega «Suspicious extraction of Azure Cosmos DB account keys» y la aplicación productiva usa la clave primaria. ¿Cuál es la contención más segura?**

- a) Regenerar de inmediato la clave primaria y la secundaria y actualizar después la cadena de conexión de la aplicación en todos sus entornos
- b) Deshabilitar la cuenta de Cosmos DB y restaurarla desde un backup cuando termine la investigación
- c) Quitarle el rol al principal y cerrar la alerta, porque una alerta Informational no justifica rotar claves
- d) Rotar primero la clave que no usa la aplicación, mover la aplicación a ella o a RBAC, regenerar la otra y aplicar `disableLocalAuth`  ✅

*Respuesta: d).* La rotación segura bloquea regenerar una clave usada en las últimas 12 horas, por eso rotas primero la que no usa la aplicación y migras antes de regenerar la otra. RBAC con Microsoft Entra ID y `disableLocalAuth=true` eliminan la dependencia de claves; regenerar las dos a la vez provoca una caída. [Fuente](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-rotate-keys) · Repasa [W3](03b_Track_Especializacion_por_workload.md#w3)

**9. Preparas el retiro del 16 de agosto de 2027 con `AuditClassicPolicies.ps1`. ¿Qué afirmación es correcta?**

- a) También se retira la API `advancedThreatProtectionSettings`, así que debes migrar las políticas de ATP de cada servidor a la API unificada
- b) El retiro cambia la facturación: las bases con políticas clásicas pasan a cobrarse por base de datos
- c) Una política clásica con `state == Enabled` en el CSV no prueba que la uses: busca las dependencias en pipelines, IaC y scripts  ✅
- d) Al pasar de Classic a Express se migran las baselines y el historial, así que basta con cambiar la configuración

*Respuesta: c).* La guía de migración aclara que una política con `state == Enabled` no prueba su uso, que `advancedThreatProtectionSettings` no es una API clásica y que no hay impacto en la facturación. Además, al pasar de Classic a Express no se migran baselines ni historial. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/migrate-classic-defender-for-sql-apis) · Repasa [W3](03b_Track_Especializacion_por_workload.md#w3)

**10. Un usuario con el rol Key Vault Contributor leyó secretos de una bóveda sin que nadie le asignara un rol de plano de datos. ¿Qué lo permitió y cuál es la corrección estructural?**

- a) La bóveda usa access policies: cualquier rol con `Microsoft.KeyVault/vaults/write` puede darse acceso; migra la bóveda a Azure RBAC  ✅
- b) El firewall de la bóveda estaba deshabilitado y permitió el acceso; actívalo y limita las IP de origen
- c) En RBAC, Key Vault Contributor incluye la lectura de secretos; reemplázalo por un rol de solo lectura del plano de control y revisa sus asignaciones
- d) Defender for Key Vault estaba en el modelo por transacción y no lo detectó; cámbialo al subplan `PerKeyVault`

*Respuesta: a).* Con access policies, Contributor o Key Vault Contributor pueden concederse acceso al plano de datos; con Azure RBAC solo Owner y User Access Administrator gestionan permisos, con PIM y deny assignments. Desde la API 2026-02-01 las bóvedas nuevas usan RBAC por defecto, pero las existentes no cambian. [Fuente](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-access-policy) · Repasa [W4](03b_Track_Especializacion_por_workload.md#w4)

**11. Un atacante con Owner en una suscripción borra los locks antes de eliminar cuentas de Storage críticas, como en Storm-0501. ¿Qué control seguiría bloqueando el DELETE?**

- a) Un lock ReadOnly en la suscripción, porque el Owner no puede borrar locks heredados
- b) Una alerta de Activity Log sobre `Microsoft.Authorization/locks/delete` con un grupo de acciones que avise al equipo de guardia
- c) Una regla de supresión que impida cerrar las alertas de borrado de Defender for Resource Manager
- d) Una política `denyAction` para DELETE asignada en el grupo de administración, fuera del alcance del Owner  ✅

*Respuesta: d).* Owner y User Access Administrator pueden borrar locks (`Microsoft.Authorization/locks/*`): frenan errores, no a un Owner hostil. `denyAction` devuelve 403 a los DELETE y, asignada en el grupo de administración, el Owner de la suscripción no puede quitarla. Una alerta avisa, pero no bloquea. [Fuente](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny-action) · Repasa [W4](03b_Track_Especializacion_por_workload.md#w4)

**12. Activaste CIEM hace 30 días. Varias identidades creadas hace dos meses nunca usaron sus roles, pero no aparecen en «Permissions of inactive identities in your Azure subscription should be revoked». ¿Por qué?**

- a) CIEM solo evalúa identidades de AWS y GCP; en Azure las evalúa Entra ID Protection para workload identities
- b) Las recomendaciones de inactividad requieren Workload Identities Premium en el inquilino
- c) La inactividad se mide por asignaciones de rol sin uso en 90 días y no se evalúan identidades de menos de 90 días  ✅
- d) La inactividad se mide por inicios de sesión en los últimos 45 días y esas identidades iniciaron sesión hace poco

*Respuesta: c).* La lógica GA del 2 de febrero de 2026 pasó de inicios de sesión en 45 días a asignaciones de rol sin uso en 90 días y excluye las identidades con menos de 90 días; además, el Permissions Creep Index quedó deprecado. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Repasa [W4](03b_Track_Especializacion_por_workload.md#w4)

**13. Tu equipo publica APIs REST en un API Management Premium: unas por el gateway administrado, otras por un gateway autohospedado y otras dentro de workspaces. Al activar Defender for APIs, ¿qué APIs podrás incorporar?**

- a) Todas, porque el nivel Premium está soportado
- b) Solo las publicadas por el gateway administrado y fuera de workspaces  ✅
- c) Solo las del gateway autohospedado, porque el tráfico pasa por tu red
- d) Ninguna: Defender for APIs solo admite el nivel Developer

*Respuesta: b).* Defender for APIs admite los niveles Premium, Standard, Basic y Developer y solo APIs REST, pero no incorpora APIs expuestas por un gateway autohospedado ni gestionadas con workspaces, y tampoco el nivel Consumption. Para esas APIs necesitas otra señal, como un WAF delante del gateway. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-prepare) · Repasa [W5](03b_Track_Especializacion_por_workload.md#w5)

**14. Tienes 24 Function Apps y 6 contenedores serverless en ejecución en suscripciones con Defender CSPM, en el modelo clásico por plan. ¿Cuántos recursos facturables suman los componentes serverless y cuánto cuestan al mes a precio de lista?**

- a) 30 recursos, 153,30 USD
- b) 3 recursos, 15,33 USD
- c) 12 recursos, 61,32 USD
- d) 6 recursos, 30,66 USD  ✅

*Respuesta: d).* Ocho funciones o web apps cuentan como un recurso facturable (24/8 = 3) y dos contenedores serverless en ejecución como otro (6/2 = 3): 6 × 5,11 USD = 30,66 USD al mes. En el modelo DWU estos componentes quedan incluidos sin opción de exclusión. [Fuente](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/) · Repasa [W5](03b_Track_Especializacion_por_workload.md#w5)

**15. Un banco de Colombia crea en noviembre de 2026 una suscripción nueva y necesita las alertas AzureDNS_* sobre la resolución DNS de sus VM. ¿Qué habilita?**

- a) Defender for DNS, el plan independiente
- b) Defender CSPM con la integración de Defender EASM
- c) Defender for Servers Plan 2  ✅
- d) Defender for Containers con la detección DNS de Kubernetes

*Respuesta: c).* Desde el 1 de agosto de 2023 las alertas DNS vienen en Servers Plan 2 para suscripciones nuevas y desde el 5 de julio de 2026 la API bloquea las altas de Defender for DNS. La detección DNS de Defender for Containers usa telemetría de Kubernetes, no la del resolvedor de Azure DNS, y EASM no genera alertas de runtime. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Repasa [W5](03b_Track_Especializacion_por_workload.md#w5)

**16. Un equipo quiere que Defender for Cloud comente en los pull requests de Azure DevOps las dependencias vulnerables, además de la IaC. Ya tiene Defender CSPM y Build Validation. ¿Qué le respondes?**

- a) Hoy las anotaciones de Defender solo cubren hallazgos de IaC; para dependencias usa otra señal, como GitHub Advanced Security for Azure DevOps o la CLI en el pipeline  ✅
- b) Basta con agregar la categoría «Dependencies» en la llamada PATCH de actionableRemediation
- c) Necesita GitLab Ultimate para habilitar esa categoría
- d) Necesita Defender for Containers además de Defender CSPM

*Respuesta: a).* La API de anotaciones lista varias categorías (IaC, Code, Artifacts, Dependencies y Containers), pero solo IaC está soportada. En GitHub las anotaciones requieren GHAS y el workflow de MSDO, y GitLab no las admite. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-pull-request-annotations) · Repasa [W6](03b_Track_Especializacion_por_workload.md#w6)

**17. Quieres probar MDASH, el escáner agéntico de código, conectando desde el portal de Defender la organización de GitHub productiva, que ya está en el conector de DevOps del portal de Azure. ¿Qué ocurre?**

- a) Ambos conectores coexisten y comparten los hallazgos
- b) Solo funciona si la organización migra a GitLab
- c) Basta con el rol Security Reader para crear el conector
- d) Debes borrar el conector del portal de Azure para esa organización y pierdes las capacidades de DevOps security asociadas  ✅

*Respuesta: d).* El conector de GitHub de Exposure Management (vista previa privada) exige Security Administrator y Organization Owner y, si la organización ya está en el conector del portal de Azure, obliga a borrarlo. Haz el piloto con una organización separada. [Fuente](https://learn.microsoft.com/en-us/security-exposure-management/create-github-connector) · Repasa [W6](03b_Track_Especializacion_por_workload.md#w6)

**18. Una aseguradora de Perú tiene 2.000 repositorios conectados, 40 VM y 10 cuentas de almacenamiento con Defender CSPM, en el modelo clásico por plan. ¿Cuánto paga al mes por Defender CSPM a precio de lista?**

- a) 5,11 USD × 2.050 recursos, porque cada repositorio es facturable
- b) 5,11 USD × 50 ≈ 255,50 USD; los repositorios no se facturan y GitHub Advanced Security se licencia aparte  ✅
- c) 5,11 USD por committer activo
- d) Nada: DevOps security es gratuito y cubre también las VM

*Respuesta: b).* Defender CSPM solo factura servidores, cuentas de almacenamiento, bases de datos y cargas serverless; repositorios y pipelines no son recursos facturables. GitHub Secret Protection (19 USD) y Code Security (30 USD) se cobran aparte por committer activo. [Fuente](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/) · Repasa [W6](03b_Track_Especializacion_por_workload.md#w6)

**19. Tu organización usa una cuenta de administrador delegado de AWS para seguridad y quieres incorporar todas las cuentas, incluidas las futuras, con autoaprovisionamiento. ¿Qué cuenta usas para el conector?**

- a) La cuenta de administrador delegado, porque es la que administra seguridad
- b) Cada cuenta miembro por separado, con un conector propio
- c) La cuenta de administración de AWS Organizations, con stack y StackSet y trusted access habilitado  ✅
- d) Cualquier cuenta que tenga el rol OrganizationAccountAccessRole

*Respuesta: c).* Para la incorporación de organización solo sirve la cuenta de administración, que crea conectores para las cuentas miembro descubiertas y para las nuevas; las cuentas de administrador delegado no se admiten. Sin trusted access, el StackSet falla con «You must enable organizations access to operate a service managed stack set». [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-aws) · Repasa [W7](03b_Track_Especializacion_por_workload.md#w7)

**20. El escaneo sin agente de tus EC2 dejó de dar resultados y en la cuenta ves cientos de snapshots con la etiqueta de Defender. ¿Qué está pasando?**

- a) Defender deja de cobrar el plan hasta que se resuelva
- b) Es normal: Defender conserva los snapshots 30 días
- c) Defender copió los snapshots a Azure y espera para analizarlos
- d) Fallan los borrados: con 250 o más snapshots acumulados se suspenden los escaneos nuevos, mientras los snapshots y el plan siguen costando  ✅

*Respuesta: d).* La salvaguarda de 250 snapshots suspende los escaneos en ese alcance si los borrados fallan; revisa el permiso ec2:DeleteSnapshot, los permission boundaries y las SCP. Los snapshots no salen de su región ni se copian a Azure. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-agentless-scanning-vms) · Repasa [W7](03b_Track_Especializacion_por_workload.md#w7)

**21. Ya ingieres CloudTrail en Sentinel con S3 y SQS y ahora activas la ingesta de CloudTrail de Defender for Cloud sobre el mismo trail. ¿Qué haces para no romper Sentinel?**

- a) Configuras un tópico SNS con fan-out a dos colas SQS con raw message delivery y actualizas la directiva de la cola de Sentinel  ✅
- b) Apuntas Defender a la misma cola SQS de Sentinel
- c) Creas un segundo trail sin SNS y dejas que ambos lean el mismo bucket con notificaciones a una sola cola
- d) Nada: no se pueden combinar y debes elegir uno de los dos

*Respuesta: a).* Una cola SQS admite un solo consumidor: con fan-out por SNS cada servicio lee su propia cola. Además, si ya existe el proveedor OIDC de Defender, agregas a Sentinel como audiencia en lugar de crear otro. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sentinel-connected-aws) · Repasa [W7](03b_Track_Especializacion_por_workload.md#w7)

<a id="eval-operacion"></a>

## Track · Operación y excelencia · Operar la seguridad en la nube con excelencia

**1. ¿Qué necesitas para usar reglas de gobernanza que asignen dueño y fecha límite a las recomendaciones?**

- a) Solo Foundational CSPM
- b) Una licencia de Microsoft Sentinel
- c) Defender CSPM y un rol como Security Admin, Contributor u Owner  ✅
- d) Defender for Servers Plan 1

*Respuesta: c).* Las reglas de gobernanza requieren Defender CSPM; toman el dueño de una etiqueta, fijan plazos de 7, 14, 30 o 90 días con período de gracia y envían correos semanales al dueño y a su jefe. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/governance-rules) · Repasa [O1](04_Track_Operacion_y_excelencia.md#o1)

**2. Un usuario es Owner de la suscripción. ¿Ve automáticamente los datos de nube en el portal de Defender con RBAC unificado?**

- a) No: los permisos de Azure no fluyen al RBAC unificado y hay que asignarlos allí  ✅
- b) Sí, se heredan siempre
- c) Solo si además es Security Reader
- d) Solo para los recursos de AWS

*Respuesta: a).* El RBAC unificado del portal de Defender es distinto del RBAC de Azure. Los cloud scopes agrupan entornos, pero los nuevos no se agregan solos. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/cloud-scopes-unified-rbac) · Repasa [O1](04_Track_Operacion_y_excelencia.md#o1)

**3. ¿Qué recomienda la metodología Secure del Cloud Adoption Framework sobre las responsabilidades de seguridad?**

- a) Delegar toda la seguridad de la nube en el proveedor
- b) Centralizar todas las tareas en el SOC
- c) Asignar todo al equipo de plataforma
- d) Documentar un modelo de responsabilidad compartida que funcione como matriz RACI  ✅

*Respuesta: d).* El CAF describe roles de arquitectura, ingeniería, operaciones, postura y DevSecOps y pide documentar un modelo de responsabilidad compartida tipo RACI; no existe un RACI oficial específico de Defender for Cloud. [Fuente](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/secure/teams-roles) · Repasa [O1](04_Track_Operacion_y_excelencia.md#o1)

**4. ¿Qué afirmación sobre las exenciones de recomendaciones es correcta?**

- a) No tienen límite y aplican a las recomendaciones personalizadas
- b) Requieren el MCSB asignado, admiten hasta 5.000 recursos exentos por suscripción y pueden tener vencimiento  ✅
- c) Solo se crean por API
- d) Siempre bajan la puntuación segura

*Respuesta: b).* Las exenciones se crean por recurso, suscripción o grupo de administración, con categoría Mitigated o Risk accepted y vencimiento opcional; no aplican a recomendaciones personalizadas. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/exempt-resource) · Repasa [O1](04_Track_Operacion_y_excelencia.md#o1)

**5. ¿Qué requisito tiene el libro Secure Score Over Time?**

- a) Ninguno: muestra el historial desde la creación de la suscripción
- b) Exportación continua a Log Analytics con streaming e instantáneas semanales  ✅
- c) Una licencia de Power BI Pro
- d) Microsoft Security Exposure Management con licencia aparte

*Respuesta: b).* El libro depende de la exportación continua y sus instantáneas semanales; los datos aparecen después de al menos una semana. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/custom-dashboards-azure-workbooks) · Repasa [O2](04_Track_Operacion_y_excelencia.md#o2)

**6. ¿Qué afirmación sobre las dos puntuaciones seguras es correcta?**

- a) Tienen el mismo valor en ambos portales
- b) La clásica solo existe en el portal de Defender
- c) La Cloud Secure Score basada en riesgo está solo en el portal de Defender y no es comparable con la clásica del portal de Azure  ✅
- d) Las recomendaciones en preview cuentan en ambas

*Respuesta: c).* Son modelos distintos: la Cloud Secure Score pondera riesgo, exposición y criticidad; la clásica cuenta controles del MCSB. Las dos se recalculan cada 8 horas y ninguna cuenta recomendaciones en preview. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) · Repasa [O2](04_Track_Operacion_y_excelencia.md#o2)

**7. Según el Security Adoption Framework, ¿qué mide el MTTA?**

- a) El tiempo desde que se reconoce un incidente hasta que se corrige
- b) El tiempo medio entre dos incidentes
- c) El tiempo desde la detección hasta el cierre administrativo
- d) El tiempo para reconocer una alerta o un incidente desde que se genera  ✅

*Respuesta: d).* El MTTA mide el reconocimiento desde la generación; el MTTR, la corrección después del reconocimiento. En Sentinel se calculan con la tabla SecurityIncident. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations-incidents) · Repasa [O2](04_Track_Operacion_y_excelencia.md#o2)

**8. ¿Qué ofrecen las iniciativas de Exposure Management para medir la postura de la nube?**

- a) Puntuación, meta configurable, tendencia de 14 días e historial; las métricas de nube requieren Defender CSPM  ✅
- b) Una puntuación fija que no se puede ajustar
- c) Solo datos de endpoints
- d) Una exportación mensual en PDF sin historial

*Respuesta: a).* Las iniciativas permiten fijar una meta y seguir la tendencia; las métricas van de 0 a 100, con peso editable y la opción «Risk accepted». [Fuente](https://learn.microsoft.com/en-us/security-exposure-management/initiatives) · Repasa [O2](04_Track_Operacion_y_excelencia.md#o2)

**9. ¿Qué estándares se asignan por defecto al conectar una cuenta de AWS?**

- a) Solo el MCSB
- b) El MCSB y AWS Foundational Security Best Practices  ✅
- c) CIS AWS v3.0.0 y PCI DSS
- d) Ninguno

*Respuesta: b).* Azure recibe el MCSB; AWS, el MCSB más AWS Foundational Security Best Practices, y GCP, el MCSB más GCP Default. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-regulatory-compliance-standards) · Repasa [O3](04_Track_Operacion_y_excelencia.md#o3)

**10. Un auditor externo necesita leer el panel de cumplimiento regulatorio sin cambiar nada. ¿Qué rol le asignas?**

- a) Security Reader
- b) Owner
- c) Policy Contributor
- d) Reader  ✅

*Respuesta: d).* Reader ve los datos de cumplimiento y Security Reader no; asignar estándares requiere Owner o Policy Contributor, que exceden lo que necesita un auditor. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/regulatory-compliance-dashboard) · Repasa [O3](04_Track_Operacion_y_excelencia.md#o3)

**11. ¿Qué dice Microsoft Learn sobre el plan necesario para asignar estándares regulatorios adicionales?**

- a) Todas las páginas coinciden en que basta Foundational CSPM
- b) Solo se habilitan con Defender for Servers Plan 1
- c) Hay versiones contradictorias (solo Defender CSPM, cualquier plan pago salvo Servers P1 o APIs P1, o al menos un plan pago): verifica en tu inquilino  ✅
- d) Requieren una licencia premium de Purview Compliance Manager

*Respuesta: c).* La tabla de CSPM, la guía de asignación y el panel de cumplimiento dan versiones distintas; documenta lo que observes en tu inquilino antes de prometer un costo. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/assign-regulatory-compliance-standards) · Repasa [O3](04_Track_Operacion_y_excelencia.md#o3)

**12. No hay un estándar de Defender for Cloud para la regulación financiera de tu país. ¿Qué haces?**

- a) Mapeas, con Legal, la norma a ISO/IEC 27001:2022 o NIST CSF 2.0 y creas un estándar personalizado con recomendaciones KQL  ✅
- b) Asignas LGPD, porque cubre toda la región
- c) Esperas a que Microsoft publique el estándar
- d) Usas solo la puntuación segura como evidencia

*Respuesta: a).* Las recomendaciones KQL requieren Defender CSPM y Security Admin, y el estándar personalizado, Owner. LGPD es de Brasil, fuera de MCSA, y el mapeo jurídico lo valida Legal. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/create-custom-recommendations) · Repasa [O3](04_Track_Operacion_y_excelencia.md#o3)

**13. Tras el fin del boletín mensual, ¿cuál es la fuente oficial para seguir los cambios próximos y los retiros de Defender for Cloud?**

- a) La página «Important upcoming changes»
- b) El Ninja oficial
- c) What's new, con su feed RSS, que incluye cambios próximos y funciones en desuso  ✅
- d) Azure Status

*Respuesta: c).* La URL de «Important upcoming changes» redirige a What's new, que incluye lo próximo y lo retirado y archiva lo anterior a seis meses; el boletín terminó el 3 de agosto de 2026. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Repasa [O4](04_Track_Operacion_y_excelencia.md#o4)

**14. ¿Qué sabes con certeza sobre Foundational CSPM en las suscripciones nuevas «desde el 27 de octubre de 2026»?**

- a) Que se retiró por completo
- b) Que pasó a ser de pago
- c) Que solo se habilita desde el portal de Defender
- d) Nada con certeza: la página en inglés que anunciaba el opt-in se eliminó el 30 de septiembre, así que debes verificarlo en una suscripción nueva  ✅

*Respuesta: d).* Quedan copias traducidas del anuncio, pero la página en inglés y la entrada de las notas de versión se retiraron. Verifica en una suscripción nueva y habilítalo de forma explícita en tu proceso de alta. [Fuente](https://daily.defender.admin.news/changes/2026-09-30/foundational-cspm-opt-in-10/) · Repasa [O4](04_Track_Operacion_y_excelencia.md#o4)

**15. Las recomendaciones agrupadas se retiraron el 31 de julio de 2026. ¿Qué acción corresponde?**

- a) Ninguna: los tableros se actualizan solos
- b) Migrar consultas ARG, reglas de gobernanza, exenciones y exportaciones al modelo individual y convertir las reglas de deshabilitación en exenciones  ✅
- c) Desactivar Defender CSPM
- d) Volver a la puntuación clásica

*Respuesta: b).* Los tableros, consultas y exportaciones que dependían de sub-assessments dejaron de devolver datos; los KPI de burn-down deben recalcularse con el modelo individual. [Fuente](https://learn.microsoft.com/en-us/azure/defender-for-cloud/transition-grouped-individual-recommendations) · Repasa [O4](04_Track_Operacion_y_excelencia.md#o4)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD, cambian con frecuencia y dependen de tu contrato, canal, región y moneda: confírmalos en la página oficial y con tu proveedor antes de presupuestar. El contenido regulatorio es una referencia y no constituye asesoría legal: las decisiones de cumplimiento corresponden a tus áreas de Legal, riesgo y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

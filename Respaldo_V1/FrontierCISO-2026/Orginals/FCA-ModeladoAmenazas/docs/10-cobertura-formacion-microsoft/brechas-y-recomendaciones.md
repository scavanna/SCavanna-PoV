# Brechas y plan recomendado

## Brecha total en ambos repositorios

| ID | Tecnología | Acción recomendada |
| --- | --- | --- |
| MS-006 | Microsoft Defender for IoT | Ninja: crear; Excelencia: crear |
| MS-015 | Azure Backup | Ninja: crear; Excelencia: crear |
| MS-016 | Azure Site Recovery | Ninja: crear; Excelencia: crear |
| MS-029 | Azure Front Door y Traffic Manager | Ninja: crear; Excelencia: crear |
| MS-031 | Microsoft Priva | Ninja: crear; Excelencia: crear |
| MS-032 | Azure Service Health | Ninja: crear; Excelencia: crear |
| MS-034 | Azure Traffic Manager | Ninja: crear; Excelencia: crear |
| MS-035 | Azure Front Door | Ninja: crear; Excelencia: crear |
| MS-036 | Availability Zones | Ninja: crear; Excelencia: crear |
| MS-037 | Azure Firewall | Ninja: crear; Excelencia: crear |
| MS-039 | Azure Network Watcher | Ninja: crear; Excelencia: crear |

## Cobertura parcial o unilateral

| ID | Tecnología | Ninja | Excelencia Operacional | Acción | Prioridad |
| --- | --- | --- | --- | --- | --- |
| MS-003 | Microsoft Entra ID Protection | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-004 | Microsoft Defender for Identity | Parcial | Directa | Ninja: ampliar/citar | Baja |
| MS-005 | Microsoft Defender for Cloud | Directa | Sin artefacto específico | Excelencia: crear | Baja |
| MS-007 | Microsoft Defender for Endpoint | Parcial | Directa | Ninja: ampliar/citar | Baja |
| MS-008 | Microsoft Intune | Sin artefacto específico | Directa | Ninja: crear | Baja |
| MS-012 | Microsoft Defender for Cloud Apps | Parcial | Directa | Ninja: ampliar/citar | Baja |
| MS-013 | Microsoft Entra Conditional Access | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-014 | Microsoft Entra Privileged Identity Management | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-017 | Azure Monitor y Log Analytics | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-018 | Azure DDoS Protection | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-019 | Azure Web Application Firewall | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-020 | Microsoft Defender for APIs | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-021 | GitHub Advanced Security y Azure DevOps | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-022 | Azure Key Vault y Managed HSM | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-023 | Azure Policy y Guest Configuration | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-025 | Azure AI Content Safety | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-026 | Microsoft Defender for Office 365 | Parcial | Directa | Ninja: ampliar/citar | Baja |
| MS-028 | Microsoft Defender Vulnerability Management | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-030 | Microsoft Security Exposure Management | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |
| MS-033 | Azure Resource Graph | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-038 | Azure Private Link | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-040 | Microsoft Defender for DevOps | Parcial | Sin artefacto específico | Ninja: ampliar/citar; Excelencia: crear | Media |
| MS-041 | Microsoft Purview Data Map | Parcial | Parcial | Ninja: ampliar/citar; Excelencia: ampliar/citar | Media |

## Orden sugerido

1. Crear artefactos para brechas de continuidad, nube, red, OT/IoT y privacidad sin cobertura directa.
2. Convertir cobertura parcial en módulos específicos solo cuando haya suficiente profundidad, cadencia y evidencia independiente.
3. Evitar duplicar contenido transversal: enlazar Sentinel/XDR/Purview/Defender for Cloud donde ya exista y añadir el delta operativo faltante.
4. Para cada nuevo módulo, incluir objetivo, arquitectura, implementación, operación, KPI/KRI, KQL/queries, respuesta, recuperación, pruebas, licencias y fuentes oficiales.
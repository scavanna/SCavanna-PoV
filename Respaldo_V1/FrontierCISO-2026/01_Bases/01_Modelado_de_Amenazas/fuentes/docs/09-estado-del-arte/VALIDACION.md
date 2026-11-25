# Validación de cobertura y hallazgos

## Resultado de la auditoría previa

Antes de esta entrega:

- las **15 categorías** existían como agrupaciones con controles descriptivos dispersos, pero no había una matriz uniforme que cubriera identificación/inventario, prevención/protección, detección y respuesta/recuperación;
- las **79 entradas MAGERIT v3 ampliadas** tenían catálogo y mapeos, pero no tenían cuatro fases de mitigación por amenaza;
- no existía un mapeo reproducible de esas fases a capacidades Microsoft con fuente Learn por capacidad.

Por ello se creó este paquete específico.

## Cobertura generada

| Universo | Registros | Fases | Filas de ciclo | Producto adicional |
|---|---:|---:|---:|---|
| Categorías agregadas | 15 | 4 | 60 | Excel con mapeo Microsoft |
| MAGERIT v3 oficial | 57 | 4 | 228 | incluye 55 específicas + 2 comodines |
| Extensiones no oficiales | 22 | 4 | 88 | `EXT-*` con base MAGERIT |
| Total MAGERIT ampliado | 79 | 4 | 316 | mapeo Microsoft y control family |

## Microsoft

- Fuente: Microsoft Learn MCP Server y páginas oficiales Microsoft Learn.
- Corte de consulta: 2026-11-18.
- 43 fuentes/capacidades registradas.
- 1.308 asociaciones candidato en la matriz de 79 amenazas.
- 256 asociaciones candidato en la matriz de 15 categorías.
- Cada asociación incluye fase, requisito, producto/capacidad, URL, alcance y validación pendiente.

## Estado del mapeo

Los productos se clasifican como capacidades candidatas, no como cobertura aprobada. Para convertir una asociación en control efectivo se necesita validar:

1. licencia y SKU;
2. región y plataforma;
3. onboarding, conector e inventario;
4. política/configuración;
5. telemetría y retención;
6. autoridad/owner;
7. prueba de diseño y operación;
8. riesgo residual;
9. RTO/RPO o criterio de aceptación;
10. límites de producto y dependencias no Microsoft.

## Validaciones ejecutadas

- 15 categorías completas con 4 fases.
- 57 registros MAGERIT y 22 extensiones cargados sin pérdida.
- 79 × 4 = 316 filas exactas.
- IDs únicos por universo.
- Archivos YAML parseables.
- Workbooks `.xlsx` abiertos con `openpyxl`.
- Sin URLs Microsoft vacías en el mapeo.
- Manifiesto con bytes y SHA-256.

## Restricciones

- No todo riesgo físico, natural, de infraestructura crítica o humano puede mitigarse con tecnología Microsoft.
- Microsoft Sentinel y productos Defender requieren fuentes, conectores, políticas, datos y operación para proporcionar detección.
- En OT/IoT, la priorización es seguridad humana, proceso y operación autorizada.
- Privacidad, cumplimiento, notificación y derechos requieren Legal/DPO y fuentes jurídicas aplicables.
- Microsoft Security Copilot es asistencia; no sustituye validación humana.

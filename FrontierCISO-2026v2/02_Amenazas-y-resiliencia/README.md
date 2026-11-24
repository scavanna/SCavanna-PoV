# Del modelado de amenazas a un control que se pueda probar

[Biblioteca](../README.md) · [Guía de ransomware y recuperación](Ransomware.md)

**Cuándo usarlo:** nuevo sistema, cambio de arquitectura, tercero nuevo, agente con acceso a datos o respuesta a un incidente. **Resultado:** un escenario con tratamiento, responsable, prueba y fecha de revisión.

## Taller: una fila por escenario material

1. **Dibujá el sistema.** Identificá procesos, activos, datos, identidades, dependencias y límites de confianza. Versioná el diagrama y explicitá qué queda fuera.
2. **Elegí la lente según la decisión.** MAGERIT organiza amenazas; un diagrama de flujo de datos y STRIDE ayudan con arquitectura de aplicaciones; LINDDUN ayuda a indagar impactos de privacidad; MAESTRO orienta el análisis de capas en IA. Si la decisión es económica, una estimación tipo FAIR ayuda a comparar opciones. Una base de técnicas no es un catálogo de escenarios de negocio.
3. **Escribí la cadena causa–evento–consecuencia.** Indicá precondición, activo o proceso afectado, quién sufriría el impacto y qué todavía no se sabe. «Ransomware» suelto no es un escenario.
4. **Seleccioná controles por fase y definí la prueba antes de dar el riesgo por tratado.** Si un control requiere tecnología Microsoft, verificá el entorno y la documentación de [operación y formación](../03_Operacion-y-formacion-Microsoft/README.md); un producto mencionado no acredita cobertura.
5. **Decidí sobre el riesgo residual.** Registrá la opción, el responsable autorizado, evidencia de diseño y de operación, excepción y próximo evento de revisión: un cambio de datos, identidad, tercero, alcance o evidencia.

## Las cuatro fases del catálogo FCA

| Fase | Pregunta | Ejemplo de evidencia |
| --- | --- | --- |
| I · Inventario | ¿Qué activos, funciones y dependencias importan? | Activos y responsables conciliados con el diagrama y el inventario real. |
| P · Prevención y protección | ¿Qué control reduce probabilidad o impacto, y en qué alcance? | Política, configuración y prueba positiva/negativa en la población definida. |
| D · Detección | ¿Qué indicio debería verse, dónde y quién lo atiende? | Evento benigno de prueba, alerta o resultado de consulta, tiempos y recepción en la cola. |
| R · Respuesta y recuperación | ¿Qué se hará, con qué autoridad, y cómo se verificará la restitución? | Ejercicio, acta de contención y prueba de retorno de servicio aceptada por negocio. |

**Separá universos:** 15 categorías para agrupar; 57 entradas del núcleo MAGERIT v3 (incluidos dos comodines) y 22 extensiones no oficiales para seleccionar amenazas; 16 casos de uso genéricos para orientar actividades. Que estén documentadas las cuatro fases de las 79 entradas no implica un vínculo 1:1 con los 16 casos, ni una mitigación instalada.

## Ficha de tratamiento para copiar

| ID / activo y dueño | Causa, condición, evento e impacto | Control por fase y dueño | Prueba, evidencia y fecha | Riesgo residual / decisor / revisión |
| --- | --- | --- | --- | --- |
| | | | | |
| Ejemplo ficticio: RES-01 / facturación | Pérdida de disponibilidad del plano de identidad y de los datos del servicio; la organización queda sin capacidad de facturar durante su ventana crítica. | I: dependencias y dueño; P: copias y administración segregada; D: alertas de cambios anómalos; R: restauración aislada y continuidad manual. | Reponer identidad, datos y aplicación en un ejercicio autorizado; registrar punto restaurado, tiempo, integridad y transacciones reconciliadas. | Si falla alguna dependencia, declarar brecha y pedir al dueño de negocio ajuste de capacidad o aceptación temporal. |

## Anexos de trabajo

- [Matriz de 15 categorías](artefactos/amenazas/matriz-estado-del-arte-15-categorias.xlsx) y [MAGERIT ampliado: 79 entradas](artefactos/amenazas/matriz-estado-del-arte-magerit-v3-ampliado.xlsx): filtrar por ID y fase. Los dos libros cubren universos distintos; el segundo es una adaptación no oficial.
- [16 casos de uso de método](artefactos/amenazas/casos-uso.csv): elegir la actividad adecuada por disparador, salida y cadencia.
- [Mapeo a capacidades Microsoft](artefactos/amenazas/mapeo-microsoft-magerit-v3-ampliado.xlsx): controles posibles por amenaza; verificar cobertura y eficacia en el entorno propio.
- [Programa de ransomware y sus tres libros de trabajo](Ransomware.md#libros-y-formularios-de-trabajo).

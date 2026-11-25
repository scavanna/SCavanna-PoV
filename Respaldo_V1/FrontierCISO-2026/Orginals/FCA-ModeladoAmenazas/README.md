# FCA · Modelado de Amenazas

Repositorio documental para gobernar amenazas, casos de uso, métodos de modelado, estándares, organizaciones y actividades asociadas de gestión de riesgos de ciberseguridad y privacidad.

**Criterio rector:** MAGERIT v3 es el núcleo metodológico compatible. Las ampliaciones de ATT&CK, LINDDUN, OWASP, ATLAS, MAESTRO, ISO/NIST, ENISA y FAIR se mantienen en capas separadas. El resultado es una **adaptación NO OFICIAL** y no altera los textos, códigos ni la valoración MAGERIT.

## Propósito

Separar y relacionar cuatro niveles sin confundirlos:

1. **Amenaza**: causa potencial de un evento de seguridad.
2. **Escenario de riesgo**: combinación contextual de amenaza, precondiciones/vulnerabilidades, activo, evento e impacto.
3. **Modelado de amenazas**: método sistemático para descubrir y tratar escenarios.
4. **Control y evidencia**: medidas y pruebas que cambian probabilidad o consecuencia.

El ransomware es un ejemplo útil: puede ser malware, técnica o patrón de ataque; no debe ser por sí solo un enunciado completo de riesgo.

## Cobertura de formación y excelencia operacional

`docs/10-cobertura-formacion-microsoft/` cruza las 43 capacidades Microsoft con los repositorios Ninja Training y Guías de Excelencia Operacional, clasificando cobertura directa, parcial o ausente, con evidencia local, brechas y Excel.

## Estado del arte de mitigación

`docs/09-estado-del-arte/` contiene matrices Markdown/Excel para las 15 categorías, 79 entradas MAGERIT v3 ampliadas y capacidades Microsoft verificadas mediante Microsoft Learn MCP.

## Paquetes de distribución

Consulte `PAQUETES.md`. Se generan dos ediciones: **metodología sin ejemplo** y **metodología con ejemplo**, ambas con manifiestos y hashes.

## Estructura

- `Amenazas.md`: fuente original proporcionada; se conserva sin modificación.
- `docs/00-fundamentos/analisis-fuente.md`: análisis de la fuente, correcciones y lagunas.
- `docs/01-dominio/glosario.md`: conceptos, relaciones y reglas de clasificación.
- `docs/02-catalogos/catalogo-amenazas.md`: 15 dominios de agrupación, no amenazas individuales exhaustivas.
- `docs/02-catalogos/magerit-v3-compatibilidad.md`: núcleo canónico MAGERIT v3 y reglas de mapeo.
- `docs/02-catalogos/adaptacion-no-oficial.md`: gobernanza y política de ampliación no oficial.
- `docs/03-casos-uso/casos-uso.md`: catálogo de actividades y artefactos operativos.
- `docs/04-metodos/metodos-modelado.md`: selección de métodos y cuándo combinarlos.
- `docs/05-marcos/marcos-organizaciones.md`: estándares, bases de conocimiento y propietarios.
- `docs/06-gobierno/matriz-gobierno.md`: trazabilidad ejecutivo–técnico–privacidad.
- `docs/07-guia-didactica/guia-metodologia-ransomware.md`: guía para articular jerarquías, dimensiones, vistas y artefactos.
- `docs/08-ejemplos/`: casos prácticos de ransomware empresarial híbrido y OT/industrial.
- `data/schema-registro.yaml`: esquema canónico del registro.
- `data/escenario-ransomware.ejemplo.yaml`: ejemplo contextual de un escenario completo.
- `templates/`: plantillas reutilizables para análisis, valoración, salvaguardas y playbooks.
- `data/magerit-v3-amenazas.csv`: 57 entradas del índice oficial del Libro II, incluidos 2 comodines.
- `data/extensiones-amenazas.csv`: extensiones modernas con mapeo a núcleos MAGERIT.
- `data/mapa-ransomware-multivista.csv`: vínculo operativo entre MAGERIT, técnicas, sectores, privacidad y playbooks.
- `data/*.csv`: registros editables para dominios, casos de uso, métodos y referencias.

## Regla de trazabilidad

Cada registro debe enlazar `amenaza → escenario → activo/proceso → controles → evidencia → riesgo inherente/residual → dueño → fecha de revisión`. Los IDs externos (p. ej., `T1486`) nunca sustituyen al contexto empresarial.

## Criterio de completitud

No existe una lista universal y cerrada de amenazas. Este repositorio conserva un catálogo base y exige extenderlo mediante inteligencia de amenazas, arquitectura, incidentes, privacidad, terceros, continuidad y cambios tecnológicos.

## Estado inicial

- **Versión**: 0.1.0.
- **Fecha de corte**: 2026-11-17.
- **Origen**: texto suministrado por el usuario.
- **Fuentes externas**: referencias oficiales enlazadas; verificar vigencia antes de auditorías o decisiones regulatorias.
- **Nota**: MITRE, ISO, NIST, ENISA, OWASP, CSA, LINDDUN y FAIR cumplen funciones distintas; no son equivalentes.

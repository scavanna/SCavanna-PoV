# AI CISO Atlas — Paquete de cierre y continuidad

**Baseline documentada:** Atlas Taxonomy 5.3 + Core Ontology 1.0 + Curator 6.0  
**Fecha de corte:** 2026-11-04  
**Propósito:** cerrar la sesión sin perder contexto y permitir reanudar el análisis en otra sesión, en un repositorio Git o con GitHub Copilot.

## Inicio rápido

1. Leer `docs/00_RESUMEN_EJECUTIVO.md`.
2. Leer `docs/01_ARQUITECTURA_FINAL.md` y `docs/08_DECISIONES_ARQUITECTURALES.md`.
3. Verificar que las siete fuentes canónicas listadas en `source_inventory/SOURCE_REGISTER.md` estén disponibles.
4. Ejecutar:

```bash
bash scripts/run_recommended_order.sh
```

El script valida catálogos, crea/carga SQLite en modo local, valida el ejemplo y ejecuta pruebas. **No aplica ChangeSets**.

## Mapa del paquete

- `docs/`: documentación funcional, técnica, operativa y de continuidad.
- `data/`: taxonomía estructural, ontología, entidades, relaciones y reglas.
- `schemas/`: contratos JSON para sidecars y ChangeSets.
- `sql/`: catálogo ontológico y property graph sobre SQLite.
- `scripts/`: carga, validación, exportación y aplicación segura.
- `config/`: instrucciones del agente y contratos de los cuatro skills.
- `.github/`: instrucciones para GitHub Copilot.
- `examples/`: ensayo, sidecar y ChangeSets de prueba.
- `diagrams/`: Mermaid editable.
- `tests/`: pruebas automatizadas.

## Estado y autoridad

La taxonomía v5.3 conserva 8 territorios, 24 dominios, 6 funciones NIST CSF 2.0, 32 subfunciones editoriales y 4 horizontes. El catálogo de 32 subfunciones **no se duplica** aquí: su autoridad es `AICISO_5_3_01_Taxonomia.pdf`. Esto evita crear una segunda fuente divergente. Las demás dimensiones estables sí se incluyen en `data/taxonomy_v5_3_structure.json`.

Core Ontology v1.0 se documenta como baseline **proposed**, con 57 tipos de entidades, 58 relaciones y 21 reglas. El agente propone; el validador verifica; una persona aprueba; el aplicador local modifica SQLite.

## Resultado esperado

Flujo de extremo a extremo:

`Ensayo → clasificación X/Y/Z → análisis H → mapeo GM-24 → extracción ontológica → sidecars → ChangeSet → validación determinista → revisión → aprobación → aplicación en SQLite`

## Navegación de archivos

[Consultar el índice de archivos y subcarpetas](indice-catalogo.md).

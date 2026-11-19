# 07 — Scripts y orden de ejecución

## Orden recomendado de implementación

1. Incorporar este paquete al repositorio.
2. Confirmar las siete fuentes canónicas.
3. Validar catálogos.
4. Crear/cargar SQLite.
5. Cargar fuentes ontológicas al conocimiento del agente.
6. Regenerar Graph Contributor.
7. Ajustar los otros tres skills.
8. Actualizar instrucciones generales.
9. Ejecutar tres ensayos piloto.
10. Revisar y congelar baseline operativa.

## Comandos

```bash
python3 scripts/validate_catalogs.py
python3 scripts/load_ontology.py graph/atlas.sqlite
python3 scripts/validate_changeset.py examples/example.changeset.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

Atajo seguro:

```bash
bash scripts/run_recommended_order.sh
```

Aplicación explícita, solo después de aprobación y validación `passed`:

```bash
python3 scripts/apply_changeset.py changesets/approved/CHG-000121.json graph/atlas.sqlite --apply
```

## Semántica de éxito

- Catálogo válido: consistencia de tipos y restricciones.
- ChangeSet válido: compatibilidad con contrato.
- Ninguno de esos resultados demuestra que una afirmación sea verdadera ni que un control sea efectivo.

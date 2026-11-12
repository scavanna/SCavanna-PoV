# Ecosistema Integrado de Resiliencia Operativa ante Ransomware · CISO 365 · KPIs/OKRs · Ninja Training 2026

Repositorio estático autoportante listo para **GitHub Pages (subdominio propio o subruta)** que integra en un único árbol verificable cuatro artefactos canónicos para dirección y operación de ciberseguridad sobre tecnología **Full Microsoft**:

| Carpeta en el repositorio | Paquete canónico | Contenido incluido |
|---|---|---|
| [`packages/ransomware-v2/`](packages/ransomware-v2/README.md) | `PKG-RANSOM` (`v2.0`) | **Programa Operativo de Resiliencia ante Ransomware v2.0**: 16 guías Markdown (`01` a `15`), 3 libros Excel (`01`, `02`, `03`), `Catalogo-correlacion-v2.json` y 3 aplicaciones HTML offline/sandbox-safe (`Mapa-de-correlacion-y-prioridades.html`, `Panel-de-resiliencia.html`, `Consola-de-incidente.html`). |
| [`packages/ciso-365/`](packages/ciso-365/AI_CISO_Atlas_CISO365_00_Indice_y_Guia_de_Uso_v1.0.md) | `PKG-CISO365` (`v1.0`) | **Modelo Operativo CISO 365**: guías `00` a `07` (`.md`), `AI_CISO_Atlas_CISO365_Catalogo_v1.0.json` y los 3 libros Excel (`Plan_y_Ciclo_Anual`, `Evaluacion_y_Entrevistas`, `Tablero_Rendicion_de_Cuentas`). |
| [`packages/kpis-okrs/`](packages/kpis-okrs/AI_CISO_Atlas_KPIs_OKRs_CISO_de_Frontera_Guia_v1.1.md) | `PKG-KPI-OKR` (`v1.0` / `v1.1`) | **KPIs y OKRs del CISO de Empresa de Frontera**: guías Markdown, catálogos JSON (`64 KPIs` + `6 KSG`, 7 perfiles sectoriales y OKR) y libros Excel (`v1.0` y `v1.1`). |
| [`packages/ninja-training/`](packages/ninja-training/README.md) | `PKG-NINJA` (`v2026-11-08`) | **Ninja Training de Seguridad Microsoft · Edición 2026**: `index.html`, `MANIFIESTO_VERSION.json`, anexos de laboratorio y los **15 programas completos** (`01_Sentinel` a `15_Seguridad_de_agentes_de_IA_en_Foundry`) con sus portales `.html`, libros `.xlsx` y módulos `.md`. |

## Acceso rápido cuando GitHub Pages está activo

- **Portal raíz del subdominio:** `index.html` (incluye lanzador de aplicaciones, **lector Markdown integrado con tabla de contenidos y buscador global**, acceso a los 15 portales Ninja, centro de descargas Excel/JSON y visor de integridad).
- **Mapa 360° de correlación, prioridades sectoriales, operación Full Microsoft y calculadora Ninja:** `packages/ransomware-v2/Mapa-de-correlacion-y-prioridades.html`
- **Panel de evaluación (`CT-01..21`) y BIA:** `packages/ransomware-v2/Panel-de-resiliencia.html`
- **Consola local de incidente fuera de banda:** `packages/ransomware-v2/Consola-de-incidente.html`
- **Portada interactiva Ninja Training 2026:** `packages/ninja-training/index.html`

## Publicación en subdominio e integridad

1. Consulta [PUBLICACION_SUBDOMINIO.md](PUBLICACION_SUBDOMINIO.md) para configurar el registro DNS `CNAME`, renombrar `CNAME.example` a `CNAME` y activar HTTPS en GitHub Pages.
2. Verifica la integridad byte a byte de todos los archivos mediante [SHA256SUMS.txt](SHA256SUMS.txt) y [MANIFIESTO_INTEGRIDAD.json](MANIFIESTO_INTEGRIDAD.json).
3. **Aviso:** todas las plantillas y herramientas son de referencia y operan localmente en el navegador; no subas datos reales de incidentes, activos ni evaluaciones de una organización a un repositorio con GitHub Pages público.

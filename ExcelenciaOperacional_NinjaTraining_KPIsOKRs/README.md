# Ecosistema Integrado de Ciberseguridad Microsoft: CISO 365, OKRs/KPIs, Excelencia Operacional y Ninja Training

**Fecha de consolidación:** `2026-11-12`  
**Arquitectura:** 100 % estática, autocontenida, sin llamadas externas ni errores CORS, lista para publicar directamente en **GitHub Pages**.

## Propósito del Repositorio

Este repositorio reúne en una sola estructura coherente y con integridad verificada los cuatro artefactos necesarios para que una organización —desde el **CISO** hasta cada **Product Owner de Control Tecnológico** y sus equipos de ingeniería y SOC— conecte el gobierno anual del riesgo con la ejecución diaria y el entrenamiento técnico profundo:

1. **[`00_Puente_ProductOwner/`](./00_Puente_ProductOwner/Guia_Maestra_CISO365_ProductOwner_EO_y_Ninja_Training.md)**: Puente maestro que vincula las `130` actividades del Plan CISO 365 y los `70` indicadores del CISO con los `23` controles de Excelencia Operacional (`833` acciones separadas en Configuración Puntual, Rutinas Periódicas y Respuesta Ad-Hoc) y los `387` módulos de Ninja Training.
2. **[`Excelencia_Operacional/`](./Excelencia_Operacional/README.md)**: Los `23` módulos canónicos (`00` a `22`), cada uno con su Guía `.md`, Contrato `.json`, Libro `.xlsx` y Dashboard `.html`.
3. **[`Ninja_Training/`](./Ninja_Training/README.md)**: Los `15` programas completos de Ninja Training de Seguridad Microsoft Edición 2026 (`387` módulos, `2.165` ejercicios etiquetados `[LAB]`, `[LAB-PARCIAL]` y `[SOLO-PRODUCCION]`, guías `.md`, portales `.html` y planes `.xlsx`).
4. **[`Referencias_CISO/`](./Referencias_CISO/index.html)**: Copias íntegras de referencia del **Modelo Operativo CISO 365 (`v1.0`)** y del **Catálogo de KPIs y OKRs del CISO de Empresa de Frontera (`v1.0` y `v1.1`)**, acompañadas de un visor web interactivo para GitHub Pages.

## Estructura de Carpetas

```text
.
├── .nojekyll                                       # Desactiva Jekyll en GitHub Pages
├── index.html                                      # Portal web unificado de entrada (GitHub Pages)
├── README.md                                       # Documentación principal del repositorio
├── INTEGRIDAD_Y_TRAZABILIDAD.md                    # Reporte de integridad de copias de referencia
├── MANIFIESTO_SHA256.json                          # Hashes criptográficos SHA-256 de los archivos incluidos
├── 00_Puente_ProductOwner/                         # Guía, JSON, Excel dinámico y Navegador HTML del Product Owner
├── Excelencia_Operacional/                         # 23 módulos tecnológicos (00 a 22) + index.html
├── Ninja_Training/                                 # 15 programas Ninja Training 2026 (01 a 15) + anexos + index.html
└── Referencias_CISO/                               # Copias de CISO 365 y KPIs/OKRs + visor web index.html
    ├── CISO_365_Plan_Anual/
    └── KPIs_y_OKRs_CISO_Frontera/
```

## Cómo publicar en GitHub Pages en 3 pasos

1. Crear un repositorio en GitHub (público o privado según tu plan de GitHub Enterprise/Pro) y descomprimir el contenido de este paquete directamente en la raíz de la rama `main`:
   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "Initial commit: Ecosistema CISO 365 + Excelencia Operacional + Ninja Training 2026"
   git remote add origin https://github.com/<ORGANIZACION_O_USUARIO>/<NOMBRE_REPO>.git
   git push -u origin main
   ```
2. Confirmar que el archivo `.nojekyll` está presente en la raíz del repositorio.
3. En GitHub, abrir **Settings → Pages → Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main` y carpeta `/ (root)` → pulsar **Save**.

En 1 a 2 minutos el sitio completo quedará activo en `https://<ORGANIZACION_O_USUARIO>.github.io/<NOMBRE_REPO>/`.

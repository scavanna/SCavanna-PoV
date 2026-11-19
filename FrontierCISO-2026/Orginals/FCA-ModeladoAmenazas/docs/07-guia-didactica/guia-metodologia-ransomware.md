# Guía didáctica: metodología multidimensional de modelado de amenazas

## 1. Propósito

Esta guía explica cómo pasar de una amenaza conocida —ransomware— a decisiones verificables de riesgo, arquitectura, respuesta y gobierno, manteniendo **MAGERIT v3 como núcleo compatible** y utilizando marcos externos como vistas complementarias.

> Adaptación NO OFICIAL basada en MAGERIT v3. Conserva códigos y estructura oficial en su propio namespace, y añade extensiones y mapeos externos trazables. No sustituye los libros oficiales ni constituye interpretación normativa.

## 2. Idea central

No debe existir un único árbol que intente responder todas las preguntas. Se necesita:

- un **registro canónico**;
- jerarquías o familias estables;
- dimensiones de valoración;
- vistas para distintos públicos;
- artefactos operativos derivados.

```text
Registro canónico de amenaza
        |
        +--> Núcleo MAGERIT: familia, código, dimensión, valoración
        +--> Contexto: sector, activo, tecnología, dependencia
        +--> Escenario: actor, evento, precondición, consecuencia
        +--> Técnica: ATT&CK / CAPEC / ATLAS / OWASP
        +--> Privacidad: LINDDUN / tratamiento / titulares
        +--> Control: requisito, salvaguarda, evidencia
        +--> Respuesta: playbook, detección, contención, recuperación
        +--> Riesgo: inherente, residual, tratamiento, aceptación
```

## 3. Jerarquías, dimensiones, vistas y ejes

| Elemento | Responde a | Ejemplo con ransomware |
|---|---|---|
| Familia MAGERIT | ¿de qué origen es la amenaza? | Principalmente `A`; en errores asociados, `E`; en indisponibilidad ambiental/industrial, `I/N` |
| Amenaza MAGERIT | ¿qué evento oficial clasifico? | `A.8`, `A.18`, `A.19`, `A.29`, etc. |
| Dominio | ¿qué exposición superviso? | malware, identidad, disponibilidad, terceros |
| Activo | ¿qué necesita protección? | ERP, identidad, POS, backups, PLC/SCADA |
| Tecnología | ¿dónde ocurre? | Windows/Linux, cloud, SaaS, OT/ICS, IoT |
| Sector | ¿qué contexto cambia el impacto? | retail, financiero, salud, industria, gobierno |
| Escenario | ¿cómo se combina la amenaza con el negocio? | interrupción de facturación; parada segura de planta |
| Dimensión | ¿qué atributo se degrada? | disponibilidad, integridad, confidencialidad, autenticidad, trazabilidad, según diseño MAGERIT |
| Técnica | ¿cómo se comporta el adversario? | ATT&CK/ICS/IoT IDs, validados por alcance |
| Playbook | ¿qué hacemos ante señales o incidentes? | contención de identidad, aislamiento, recuperación segura |
| Riesgo | ¿qué incertidumbre y pérdida quedan? | valoración MAGERIT y traducción ejecutiva |

Las familias MAGERIT son estables; los dominios, sectores y tecnologías son filtros; las técnicas y controles cambian con la evidencia y las versiones.

## 4. Regla de no confusión

### Ransomware no es un único registro

- **Software/capacidad**: malware que cifra, destruye, impide acceso o aplica extorsión.
- **Comportamiento técnico**: ATT&CK `T1486` describe cifrado con impacto, pero no todo ransomware ni toda cadena.
- **Amenazas MAGERIT**: pueden coexistir varias según la cadena y el daño.
- **Escenario**: combinación de activo, evento, precondiciones, dependencias y consecuencias.
- **Riesgo**: valoración de degradación/probabilidad/consecuencia contextual.
- **Playbook**: respuesta operativa ante el evento observado o plausible.

Una misma familia puede generar escenarios y playbooks diferentes. Ransomware sobre retail y ransomware sobre OT no deben tener el mismo plan de contención o recuperación.

## 5. Flujo de trabajo

### Paso 1 · Contextualizar

Definir servicio, misión, activos, dependencias, sector, datos, usuarios, terceros, criterios de continuidad y límites de confianza.

### Paso 2 · Clasificar en MAGERIT

Asignar los códigos oficiales aplicables sin alterar nombres ni numeración. Si la expresión moderna no cabe completamente, usar `EXT-*` con mapeo y justificación.

Para ransomware, mapeos candidatos —no automáticos—:

- `A.8` Difusión de software dañino.
- `A.11` Acceso no autorizado.
- `A.15` Modificación deliberada de la información, cuando aplica.
- `A.18` Destrucción de información.
- `A.19` Divulgación de información.
- `A.24` Denegación de servicio, cuando la consecuencia sea indisponibilidad.
- `A.29` Extorsión.

La aplicabilidad se decide por activo, evidencia y escenario.

### Paso 3 · Descomponer el escenario

```text
fuente/actor + precondiciones + evento
                 ↓
       activo y dependencias afectados
                 ↓
    degradación por dimensión y consecuencia
                 ↓
       impacto directo + acumulado/repercutido
```

### Paso 4 · Añadir capas técnicas

Relacionar técnicas ATT&CK Enterprise/ICS/IoT, patrones CAPEC, privacidad LINDDUN y controles, manteniendo ID y versión de la fuente. Un mapeo no prueba cobertura ni explotación.

### Paso 5 · Valorar con MAGERIT

Por activo–amenaza–dimensión, registrar:

- probabilidad/frecuencia;
- degradación;
- impacto directo, acumulado o repercutido;
- riesgo inherente;
- salvaguardas y eficacia;
- riesgo residual y decisión.

Una cuantificación FAIR puede añadirse para una decisión de inversión concreta, pero no sustituye la valoración MAGERIT.

### Paso 6 · Derivar controles y pruebas

Para cada escenario:

- requisito preventivo;
- fuente de detección;
- acción de contención;
- recuperación y continuidad;
- evidencia esperada;
- criterio de aceptación;
- dueño, frecuencia y última prueba.

### Paso 7 · Seleccionar playbook

El playbook se selecciona por **tipo de activo y contexto**, no solo por la palabra ransomware:

- TI/usuario final;
- identidad y cloud;
- retail/POS;
- datos personales o información regulada;
- OT/ICS;
- infraestructura crítica;
- gobierno/servicio público.

### Paso 8 · Validar y gobernar

Ejecutar tabletop, purple team, restauración, simulación segura y revisión de comunicaciones. Recalcular riesgo solo con reglas aprobadas y evidencia; no por automatismo narrativo.

## 6. Artefactos y cómo utilizarlos

| Artefacto | Usuario principal | Momento | Resultado |
|---|---|---|---|
| `magerit-v3-amenazas.csv` | riesgo, auditoría, GRC | base | catálogo oficial normalizado |
| `extensiones-amenazas.csv` | arquitectura, threat modeling | diseño | detalle moderno trazable |
| `plantilla-analisis-magerit.yaml` | facilitador de workshop | análisis | escenario completo |
| `matriz-activo-amenaza.csv` | owner y GRC | inventario/valoración | riesgo por activo |
| `registro-salvaguardas.csv` | control owners | tratamiento/prueba | evidencia y eficacia |
| `mapa-ransomware-multivista.csv` | CISO, arquitectura, SOC | coordinación | vínculo entre capas |
| `playbook-ransomware-*.yaml` | IR, SOC, continuidad, OT | ejercicio/incidente | acciones condicionadas |
| informe ejecutivo | comité | decisión | exposición, opciones y riesgo residual |

## 7. Cómo presentar a tres audiencias

### Dirección/comité

Mostrar:

- servicio afectado;
- consecuencias operativas, financieras, legales, de seguridad humana o servicio público;
- apetito/tolerancia;
- riesgo residual;
- opciones y coste de tratamiento;
- incertidumbres y decisiones requeridas.

Ocultar: listados de técnicas sin traducción al negocio.

### Arquitectura/ingeniería

Mostrar:

- DFD, trust boundaries, activos, dependencias;
- cadena técnica y precondiciones;
- requisitos, controles y telemetría;
- excepciones y pruebas.

### SOC/respuesta

Mostrar:

- señales, hipótesis, severidad y ámbito;
- acciones autorizadas y prohibidas;
- dependencias humanas/técnicas;
- conservación de evidencia;
- criterios de escalado y recuperación.

En OT, las acciones de aislamiento no deben comprometer seguridad física o proceso seguro; requieren autoridad y coordinación operativa.

## 8. Taller de 90 minutos

1. **0–10 min**: misión, alcance y definición de éxito.
2. **10–25 min**: activos, dependencias y trust boundaries.
3. **25–40 min**: códigos MAGERIT y extensiones aplicables.
4. **40–55 min**: dos escenarios, precondiciones y consecuencias.
5. **55–70 min**: controles, detecciones y pruebas existentes.
6. **70–82 min**: playbook y decisiones por contexto.
7. **82–90 min**: riesgo residual, acciones, propietarios y próxima revisión.

## 9. Criterios de aceptación

Un ejemplo está bien modelado cuando:

- usa códigos MAGERIT sin cambiarlos;
- distingue amenaza, técnica, incidente, escenario y riesgo;
- identifica activos, dimensiones y dependencias;
- documenta por qué cada amenaza aplica o no aplica;
- vincula controles a evidencia;
- diferencia diseño, implantación y eficacia;
- adapta el playbook al sector/tecnología;
- deja decisiones y aprobaciones explícitas;
- registra fecha, versión, dueño e incertidumbre.

## 10. Continuar con los ejemplos

- `docs/08-ejemplos/ransomware-empresa-hibrida.md`: IT híbrida, retail/finanzas/salud/gobierno.
- `docs/08-ejemplos/ransomware-ot-industrial.md`: OT/ICS y consecuencias ciberfísicas.
- `data/mapa-ransomware-multivista.csv`: artefacto común entre ambos.
- `templates/playbook-ransomware.yaml`: plantilla adaptable por entorno.

# Guía didáctica de la metodología

## 1. Objeto

Esta guía documenta el método sin desarrollar un caso concreto. Su propósito es enseñar cómo organizar una evaluación compatible con MAGERIT v3, ampliada mediante dimensiones, vistas y referencias externas, y cómo derivar de ella artefactos de riesgo, control, respuesta y gobierno.

> Adaptación NO OFICIAL basada en MAGERIT v3. No sustituye los libros oficiales ni modifica sus códigos, nombres o criterios.

## 2. Qué se conserva

- activos y dependencias;
- familias y códigos de amenazas MAGERIT;
- valoración por activo, amenaza y dimensión;
- probabilidad/frecuencia, degradación, impacto y riesgo;
- salvaguardas, eficacia y tratamiento;
- riesgo inherente, residual y decisiones;
- trazabilidad y revisión.

## 3. Qué se añade sin alterar MAGERIT

- extensiones `EXT-*` en namespace separado;
- dominios de agrupación como vistas navegables;
- tecnologías, sectores y ámbitos como atributos filtrables;
- ATT&CK/CAPEC/ATLAS/OWASP como mapeos de comportamiento;
- LINDDUN/NIST Privacy como lentes de privacidad;
- FAIR/CVSS/EPSS como capas de priorización con propósito declarado;
- requisitos, evidencias, KRIs, playbooks y casos de uso.

## 4. Modelo de representación

```text
Registro canónico
 ├─ Clasificación MAGERIT
 ├─ Extensión, si procede
 ├─ Activo, proceso y dependencias
 ├─ Sector, tecnología y ámbito
 ├─ Escenario y consecuencias
 ├─ Comportamientos/técnicas externas
 ├─ Requisitos, controles y evidencias
 ├─ Tratamiento y riesgo residual
 └─ Playbook, métricas, dueño y revisión
```

Una extensión nunca sustituye una clasificación oficial aplicable. Un mapeo externo no implica cobertura ni eficacia.

## 5. Secuencia metodológica

### Fase A · Preparar

- confirmar patrocinio, dueños y decisores;
- definir misión, servicios, alcance y exclusiones;
- fijar apetito/tolerancia y escalas;
- registrar versiones de taxonomías y fuentes;
- acordar criterios de “aplica / condicionado / no aplica / pendiente”.

### Fase B · Inventariar

- activos y procesos esenciales;
- dependencias ascendentes/descendentes;
- personas, terceros, ubicaciones y datos;
- tecnologías y trust boundaries;
- obligaciones, criticidad y restricciones.

### Fase C · Clasificar amenazas

1. Revisar la lista oficial MAGERIT por origen y aplicabilidad.
2. Asignar código oficial sin modificarlo.
3. Documentar la razón de aplicabilidad o exclusión.
4. Añadir `EXT-*` únicamente si el detalle moderno no puede mapearse sin pérdida.
5. Asociar técnicas externas versionadas cuando aporten valor.

### Fase D · Modelar escenarios

Construir:

```text
Actor o fuente
+ precondiciones/debilidades
+ evento amenazante
+ activo/proceso/dependencias
→ degradación por dimensión
→ consecuencias e impacto
```

Separar evento, incidente observado, riesgo y control.

### Fase E · Analizar y valorar

Por activo–amenaza–dimensión:

- valor del activo y base;
- probabilidad/frecuencia;
- degradación;
- impacto directo, acumulado y repercutido;
- riesgo inherente;
- incertidumbres;
- salvaguardas vigentes;
- riesgo residual.

### Fase F · Tratar

Definir decisión, medidas, dueño, plazo, evidencia, coste y excepciones. Registrar si el control está propuesto, diseñado, desplegado, probado, efectivo o inefectivo.

### Fase G · Derivar operación

De los escenarios priorizados derivar:

- fuentes de detección;
- alertas y criterios de escalado;
- acciones de contención;
- conservación de evidencia;
- recuperación/continuidad;
- comunicación, privacidad, reguladores y terceros;
- restricciones especiales por OT/safety;
- prueba y criterio de salida.

### Fase H · Validar

- revisión de arquitectura;
- pruebas de control;
- restauración o simulación;
- tabletop;
- purple team o BAS cuando sea seguro;
- revisión independiente;
- revaloración y aprobación del residual.

## 6. Vistas necesarias

| Vista | Pregunta | Artefacto principal |
|---|---|---|
| MAGERIT | ¿qué amenaza, activo y dimensión valoro? | matriz activo–amenaza |
| Riesgo | ¿qué exposición queda y quién decide? | registro de riesgo |
| Técnica | ¿qué comportamiento y superficie se analiza? | mapa de técnicas |
| Privacidad | ¿qué tratamiento y titular puede afectarse? | ficha LINDDUN/DPIA |
| Control | ¿qué medida existe y cómo se prueba? | registro de salvaguardas |
| Respuesta | ¿qué hacemos ante señales? | playbook |
| Sector | ¿qué obligaciones y consecuencias cambian? | perfil sectorial |
| Portafolio | ¿dónde priorizamos recursos? | tablero de cobertura/tendencias |

Las vistas referencian el mismo registro; no duplican datos ni crean taxonomías rivales.

## 7. Casos de uso

- análisis inicial;
- cambio de arquitectura;
- nueva tecnología o integración;
- alta/cambio de proveedor;
- nuevo tratamiento de datos;
- planificación anual;
- incidente o ejercicio;
- cambio normativo;
- revisión de controles;
- decisión de inversión;
- aceptación o excepción de riesgo.

## 8. Taller

1. misión y alcance;
2. activos, dependencias y límites;
3. amenazas MAGERIT y ampliaciones;
4. escenarios prioritarios;
5. valoración;
6. controles/evidencia;
7. respuesta/continuidad;
8. riesgos, decisiones, dueños y fecha.

## 9. Gestión de artefactos

- Cada registro tiene ID, versión, dueño y fecha.
- Los mapeos externos incluyen fuente y versión.
- Los controles separan diseño, despliegue y efectividad.
- Los ejemplos nunca se confunden con evaluación real.
- Las extensiones explican por qué no caben sin pérdida en el núcleo.
- Los registros retirados quedan obsoletos con sucesor.

## 10. Paquetes

- **Metodología sin ejemplo**: este documento, catálogos, esquemas, plantillas y gobierno; no incluye escenarios desarrollados.
- **Metodología con ejemplo**: incluye todo lo anterior más casos prácticos, mapas concretos y playbooks poblados como material didáctico.

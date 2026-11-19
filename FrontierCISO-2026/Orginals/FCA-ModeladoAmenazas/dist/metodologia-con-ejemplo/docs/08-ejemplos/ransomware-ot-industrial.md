# Ejemplo 2: ransomware con posible impacto OT

## 1. Contexto de enseñanza

Planta industrial ficticia con DMZ, red corporativa, sistemas de ingeniería, estaciones de operación, servidores de supervisión, PLC/RTU y proceso físico. Puede representar manufacturing, energía, agua, salud ciberfísica o infraestructura crítica.

Este ejemplo no presupone que cualquier ransomware IT puede controlar PLC; el objetivo es modelar acceso, dependencia y consecuencia sin inventar capacidad.

## 2. Caso de uso

**Objetivo**: evaluar escenarios que afecten disponibilidad, integridad o seguridad de operación por propagación/cifrado desde TI o compromiso del entorno OT.

**Activos**:

- proceso industrial y misión operativa;
- supervisión/SCADA/HMI;
- estaciones de ingeniería;
- historizadores;
- controladores y redes de campo;
- identidad y acceso remoto;
- backups/configuraciones del proceso;
- personal y procedimientos de operación segura.

## 3. Clasificación multidimensional

| Eje | Registro del ejemplo |
|---|---|
| MAGERIT | potencialmente `A.8`, `A.11`, `A.15`, `A.18`, `A.23`, `A.24`, `A.29`; `I.5`, `I.6`, `I.8`, `I.9` para fallos/dependencias; validar por escenario |
| Extensión | `EXT-001`; `EXT-021`; `EXT-022` según contexto |
| Dominio | malware, disponibilidad, acceso, manipulación, terceros, físico/safety |
| Tecnología | OT/ICS, Windows OT, HMI, SCADA, PLC, protocolos industriales, remote access |
| Sector | industria, energía, agua, transporte, salud o infraestructura crítica |
| Escenario | pérdida de supervisión; pérdida de control; parada segura; degradación del proceso |
| Técnica | ATT&CK for ICS u otra base pertinente, versión validada |
| Playbook | ransomware OT/ICS con comandancia operativa y safety |

## 4. Escenarios distintos

### RS-OT-01 · Pérdida de supervisión y parada segura

> Existe riesgo de pérdida de visibilidad de operación y parada controlada de planta cuando ransomware cifra servidores HMI/historian y afecta servicios compartidos en la zona OT, impidiendo mantener la operación dentro de condiciones seguras.

### RS-OT-02 · Manipulación/integridad de configuración o control

> Existe riesgo de cambio no autorizado de configuraciones, lógica o parámetros cuando una sesión o estación de ingeniería queda comprometida, sujeto a que el atacante consiga acceso y capacidad específica para modificar el proceso.

### RS-OT-03 · Propagación de TI a OT por dependencia compartida

> Existe riesgo de degradación OT cuando la red corporativa, identidad, soporte remoto o servicios compartidos facilitan propagación o acceso a la DMZ/OT sin barreras efectivas.

El riesgo no se describe como “ransomware OT” genérico: se diferencia disponibilidad, integridad, pérdida de supervisión, efecto físico y seguridad humana.

## 5. Arquitectura didáctica

```text
TI / Internet
      |
 acceso remoto / identidad / proveedor
      |
     DMZ
      |
 salto controlado / broker / jump host
      |
 zona de supervisión OT
      |
  HMI / historian / engineering
      |
  control / field / PLC / proceso físico
```

El workshop debe dibujar fronteras reales, rutas, dependencias, protocolos, cuentas, tiempos de sincronización, capacidad offline y procedimientos seguros.

## 6. Regla crítica de respuesta

La prioridad OT no es simplemente “aislar el endpoint infectado”. Debe equilibrarse:

- seguridad humana;
- continuidad del control seguro;
- integridad del proceso;
- impacto ambiental;
- estabilidad física;
- preservación forense;
- posibilidad de operación manual.

Una acción de contención que interrumpa supervisión, comunicación o control puede aumentar riesgo. Toda acción automatizada debe tener aprobación, límites y procedimiento local.

## 7. Mapa de valoración MAGERIT

### Activo: HMI/SCADA

- Dimensión: disponibilidad e integridad; autenticidad/trazabilidad según función.
- Amenazas: `A.8`, `A.11`, `A.15`, `A.18`, `A.24`.
- Impacto: pérdida de supervisión, operación degradada, parada segura.
- Dependencias: identidad OT, servidores, comunicaciones, procedimiento manual.

### Activo: estación de ingeniería

- Amenazas: `A.5`/`A.6` si incluye suplantación/privilegios, `A.8`, `A.11`, `A.22`, `A.23`.
- Impacto: cambio de lógica/configuración, indisponibilidad de mantenimiento, propagación.

### Activo: configuraciones y backups OT

- Amenazas: `A.18`, `A.19`, `A.23`, `E.18`/`E.15` para fallos no deliberados como comparación.
- Impacto acumulado: tiempo de reconstrucción, falta de configuración confiable.

### Proceso/seguridad física

La consecuencia se registra como impacto sobre misión, personas y entorno. No se fuerza dentro de un único código técnico si la ontología del modelo requiere activos de servicio/proceso y dependencias.

## 8. Preguntas de modelado

- ¿OT puede operar sin TI, identidad corporativa, DNS, PKI, virtualización o servicios de proveedor?
- ¿Existen jump hosts y sesiones de proveedor con MFA y aprobación?
- ¿Qué estaciones pueden programar controladores?
- ¿Existen reglas de red con entrada/salida explícita y puertos necesarios?
- ¿Hay PLC/firmware/estaciones compatibles o irreemplazables?
- ¿La restauración utiliza imágenes/versiones confiables y configuraciones validadas?
- ¿Se puede cambiar a operación local/manual de forma segura?
- ¿Quién decide aislar, parar, mantener o reiniciar? ¿Bajo qué umbral?
- ¿Qué señales IT son detectables en OT sin introducir agentes inseguros?

## 9. Controles y evidencia

| Control propuesto | Particularidad OT | Evidencia |
|---|---|---|
| Segmentación IT/DMZ/OT | deny-by-default, rutas y protocolos mínimos | arquitectura, firewall rules, test |
| Acceso remoto controlado | broker, MFA, aprobación, grabación cuando proceda | logs, lista autorizada, prueba |
| Hardening compatible | sin romper soporte o validación de proveedor | baseline y excepciones |
| Engineering workstation control | uso dedicado, medios controlados, permisos mínimos | inventario, sesiones, procedimiento |
| Detección pasiva/red | evitar agentes o escaneos disruptivos | sensores, pcaps, líneas base |
| Configuración/backups | offline, versionado, hash, prueba de restauración | inventario, restore/simulation |
| Operación manual y recuperación | procedimientos por proceso y estado seguro | tabletop, drill, tiempos |
| Gestión de terceros | ventana, credenciales, terminación y evidencia | contrato, logs, offboarding |

## 10. Playbook OT resumido

1. Declarar incidente y activar mando conjunto SOC–OT–operaciones–safety.
2. Obtener estado del proceso y modo seguro antes de actuar.
3. Identificar zonas, rutas y dependencias; no realizar escaneo activo no aprobado.
4. Contener mediante bloqueos de frontera o aislamiento selectivo autorizados.
5. Preservar supervisión/control y activar modos manuales si están aprobados.
6. Evitar reinicios, reimágenes o cambios de PLC sin autoridad OT y plan.
7. Aislar estaciones de ingeniería y accesos de terceros.
8. Recuperar desde configuraciones y copias confiables; validar con ingeniería y operación.
9. Reintroducir por zonas/fases con monitorización del proceso.
10. Evaluar impacto ambiental, humano, regulatorio y de infraestructura crítica.
11. Ejecutar lecciones y revalorizar dependencias y recuperación.

## 11. Diferencia con el ejemplo empresarial

| Dimensión | Empresa híbrida | OT/industrial |
|---|---|---|
| Impacto dominante | continuidad digital, financiero, datos | continuidad física, safety, ambiente |
| Detección | agentes, logs, EDR/XDR | pasiva, ICS/telemetría, operación |
| Contención | aislamiento/revocación rápida | aislamiento con autoridad y análisis de safety |
| Recuperación | reimagen/restauración de servicios | limpieza + validación de proceso/configuración |
| Prueba | tabletop/purple team/restore | tabletop, simulación, prueba no disruptiva |
| Aprobador | CISO/riesgo/negocio | operación/safety/engineering + CISO |

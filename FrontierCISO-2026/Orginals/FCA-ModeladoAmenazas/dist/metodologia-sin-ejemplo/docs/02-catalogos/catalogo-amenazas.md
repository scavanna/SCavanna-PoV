# Catálogo base de amenazas y casos de amenaza

## 1. Criterio de uso

Las 15 filas siguientes son **dominios de agrupación**, no una lista exhaustiva de amenazas. Fueron una simplificación inicial y se conservan como vista de navegación. Para compatibilidad y detalle, el núcleo oficial está en `magerit-v3-compatibilidad.md` y en `data/magerit-v3-amenazas.csv`: 57 entradas de índice MAGERIT v3, incluidas dos entradas comodín. Cada fila específica debe convertirse en un registro contextual con actor/fuente, evento, precondiciones, activo/proceso, consecuencias, privacidad, controles y evidencia.

## 2. Taxonomía inicial

| ID | Dominio/categoría | Subcasos de ejemplo | Eventos o resultados a modelar | Fuente técnica posible |
|---|---|---|---|---|
| THR-001 | Malware y código malicioso | ransomware, wiper, troyano, infostealer, rootkit, cryptojacking | ejecución, propagación, cifrado, destrucción, robo, consumo de recursos | ATT&CK: Impact/Execution |
| THR-002 | Identidad e ingeniería social | phishing, AitM, BEC, credential stuffing, fatiga MFA | acceso no autorizado, robo de sesión, suplantación, fraude | ATT&CK: Initial/Credential Access |
| THR-003 | Aplicaciones, software y API | inyección, XSS, SSRF, BOLA, lógica de negocio, dependencia vulnerable | explotación, acceso no autorizado, corrupción/extracción | OWASP, CAPEC, ATT&CK |
| THR-004 | Disponibilidad y denegación | DDoS L3/L4/L7, agotamiento, ransomware DDoS | degradación o indisponibilidad | ATT&CK Impact, continuidad |
| THR-005 | Amenaza interna | abuso, negligencia, sabotaje, fuga previa a salida | acceso, copia, alteración, interrupción | Insider risk, DLP, IAM |
| THR-006 | Cadena de suministro y terceros | dependencia, proveedor SaaS/BPO, actualización comprometida, subcontratado | acceso indirecto, propagación, pérdida de control | ATT&CK T1195/T1199, NIST/ENISA |
| THR-007 | Vulnerabilidades y configuración | zero-day, N-day, secretos expuestos, IAM excesivo, cloud pública | explotación o acceso por mala configuración | CVE/CWE/CVSS/EPSS, CSPM |
| THR-008 | Física, seguridad y ambiente | robo, sabotaje, incendio, agua, energía, telecomunicaciones, clima | daño, pérdida, interrupción | continuidad y seguridad física |
| THR-009 | Errores, fallos y deuda técnica | borrado, fallo hardware, corrupción, claves perdidas, despliegue incorrecto | error operativo, pérdida o indisponibilidad | incidentes, postmortems, RMA |
| THR-010 | Manipulación, intercepción e integridad | MitM, DNS/BGP poisoning, modificación fraudulenta, fraude de pago | manipulación de datos o decisiones | ATT&CK, fraude, integridad |
| THR-011 | IA y agentes | prompt injection, poisoning, extracción, fuga, tool misuse, memoria, agencia excesiva | acción indebida, filtración, manipulación, daño | OWASP LLM, MITRE ATLAS, MAESTRO |
| THR-012 | Privacidad por diseño | linking, identifying, detecting, disclosure, lack of transparency/intervenability | profiling, inferencia, exposición, pérdida de control | LINDDUN, DPIA, NIST Privacy |
| THR-013 | Fraude, uso indebido y abuso | fraude transaccional, bot, abuso promocional, manipulación de proceso | pérdida financiera, daño a clientes | fraud patterns, abuse cases |
| THR-014 | Dependencia y concentración | nube, región, telecom, proveedor único, licencias, capacidad | interrupción, indisponibilidad estratégica | continuidad, arquitectura |
| THR-015 | Cumplimiento y obligaciones | retención, transferencia, notificación, derechos, registros | sanción, litigio, imposibilidad de defender decisiones | ISO 27701, regulación aplicable |

## 3. Aplicación del catálogo

Las agrupaciones son vistas. Cada amenaza específica debe registrarse por código MAGERIT, extensión trazable, activo, precondición, evento, consecuencia, control y evidencia.

## 4. Campos obligatorios por amenaza

- ID estable y alias.
- Dominio y clasificación de fuente.
- Evento amenazante verificable.
- Activos/procesos expuestos.
- Actores o fuentes relevantes.
- Precondiciones y su evidencia.
- Consecuencias CIA + negocio + privacidad + seguridad humana.
- Técnicas/enlaces externos con versión.
- Controles propuestos/implantados y modo.
- Detecciones, respuesta y recuperación.
- Propietario, fecha y supuestos.

## 5. Mantenimiento

Actualizar al menos trimestralmente o ante incidente, cambio crítico, nueva tecnología, cambio regulatorio, adquisición, proveedor nuevo o variación material de inteligencia. No sustituir IDs; marcar registros retirados como obsoletos con sucesor.

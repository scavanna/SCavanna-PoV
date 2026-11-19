# Ejemplo 1: ransomware en una empresa híbrida

## 1. Contexto de enseñanza

Organización ficticia con servicios digitales, identidad cloud, aplicaciones SaaS, ERP, sedes y empleados híbridos. El ejercicio puede adaptarse a retail, finanzas, salud o gobierno modificando misión, datos, tolerancia y obligaciones.

No contiene una valoración real: las cifras y estados deben reemplazarse por datos del negocio.

## 2. Caso de uso

**Objetivo**: evaluar la posibilidad de interrupción prolongada y divulgación de información tras comprometer identidad y mover lateralmente hasta sistemas críticos.

**Activos**:

- ERP y facturación;
- directorio de identidades;
- endpoints administrativos;
- backups;
- repositorios de documentos y datos personales;
- canal de atención/POS si aplica.

## 3. Clasificación multidimensional

| Eje | Registro del ejemplo |
|---|---|
| MAGERIT | `A.8`, `A.11`, `A.15`, `A.18`, `A.19`, `A.24`, `A.29`; preselección, no afirmación automática |
| Extensión | `EXT-001 Ransomware y doble extorsión` |
| Dominio | malware; identidad; aplicaciones/cloud; disponibilidad; terceros |
| Tecnología | Windows/Linux, cloud, SaaS, endpoint, API, backup |
| Sector | retail, financiero, salud o gobierno, según el servicio |
| Escenario | parada del ERP/canal y posible filtración |
| Técnica | ATT&CK según comportamiento observado, incluyendo acceso, credenciales, movimiento, exfiltración e impacto |
| Privacidad | aplicable si se afectan titulares y tratamientos |
| Playbook | ransomware en entorno TI; identidad y datos como playbooks secundarios |

## 4. Escenario canónico

> Existe riesgo de indisponibilidad del ERP y servicios asociados por encima del RTO tolerado, pérdida financiera y posible exposición de datos, cuando un actor obtiene acceso mediante una credencial o sesión comprometida, alcanza privilegio suficiente, propaga capacidad maliciosa y cifra o altera sistemas y backups.

## 5. Cadena plausible para el taller

```text
Phishing/AitM o exploit externo
             ↓
Sesión o credencial válida
             ↓
Privilegio y enumeración
             ↓
Movimiento lateral
             ↓
Desactivación/evitación + descubrimiento de backups
             ↓
Cifrado/destrucción + posible exfiltración
             ↓
Extorsión + interrupción del servicio
```

La cadena es una hipótesis que debe confrontarse con telemetría, arquitectura y evidencia; no debe asumirse que todas sus fases aplican.

## 6. Valoración MAGERIT orientativa

### Activo: ERP

- Dimensión principal: disponibilidad.
- Otras dimensiones: integridad, confidencialidad y autenticidad, según diseño/dependencias.
- Amenazas principales: `A.8`, `A.18`, `A.24`, `A.29`.
- Impacto: pérdida de facturación, pagos, operación, información y obligaciones.
- Dependencias: identidad, base de datos, red, backups, personal y terceros.

### Activo: repositorio de datos personales

- Amenazas principales: `A.11`, `A.19`, `A.29`.
- Dimensión: confidencialidad y disponibilidad.
- Impacto adicional: titular, privacidad, regulator, litigio, comunicación.

### Activo: backups

- Amenazas: `A.18`, `A.23` si existe manipulación física/lógica, `A.24`/continuidad según contexto.
- Relevancia: su degradación aumenta impacto acumulado/repercutido y el tiempo de recuperación.

La probabilidad, degradación y riesgo deben medirse con escalas MAGERIT aprobadas, evidencia de exposición e incidentes/simulacros.

## 7. Preguntas de modelado

- ¿Qué identidades permiten acceder desde internet?
- ¿Existe MFA resistente al phishing?
- ¿Los administradores usan estaciones separadas?
- ¿Qué rutas laterales existen?
- ¿Quién puede borrar o modificar backups?
- ¿Los backups se recuperan dentro del RTO real?
- ¿Qué señales detectan robo de sesión, privilegio y movimiento?
- ¿Qué datos pueden exfiltrarse y con qué alcance?
- ¿Qué servicios se degradan si SaaS/identity provider falla?
- ¿Cómo se decide pagar/no pagar y quién coordina autoridades, legal y comunicación?

## 8. Controles y evidencias

| Control propuesto | Evidencia requerida | Métrica |
|---|---|---|
| MFA resistente a phishing | cobertura, excepciones, prueba de recuperación | % identidades privilegiadas cubiertas |
| Acceso condicional/restricción de sesión | políticas, logs, casos probados | sesiones anómalas bloqueadas |
| Segmentación y mínimos privilegios | arquitectura, ACL, prueba | rutas laterales innecesarias |
| EDR/XDR y respuesta | cobertura, telemetría, ejercicio | MTTC y cobertura real |
| Backup inmutable aislado | inventario, permisos, restore probado | RTO/RPO real |
| DLP/egress monitoring | reglas, alertas, prueba | volumen bloqueado/contexto |
| Gestión de vulnerabilidades | inventario, SLA, excepción | exposición crítica vencida |
| Playbook y simulacro | acciones, tiempos, decisiones | tiempo de decisión/recovery |

## 9. Playbook de respuesta resumido

1. **Detectar y confirmar**: señales de cifrado, herramientas, anomalía, exfiltración o extorsión.
2. **Preservar y clasificar**: evidencia, criticidad, alcance y posible ataque en curso.
3. **Contener identidad y endpoints**: revocar sesiones/credenciales, aislar activos autorizadamente.
4. **Proteger recuperación**: restringir y verificar backups/infraestructura limpia.
5. **Evaluar datos**: alcance, titulares, clasificación y obligaciones.
6. **Erradicar/reconstruir**: entrar desde entorno confiable, eliminar persistencia y reintroducir de forma segura.
7. **Recuperar**: priorizar misión, probar integridad y escalar por fases.
8. **Comunicar**: CISO, riesgo, negocio, DPO/Legal, reguladores y partes según procedimiento.
9. **Cerrar**: lecciones, controles, actualización del modelo, riesgo residual y evidencia.

## 10. Adaptación sectorial

| Sector | Variantes de impacto | Evidencia o decisión especial |
|---|---|---|
| Retail | POS, ecommerce, inventario, picos comerciales | modo degradado, transacciones y reconciliación |
| Finanzas | pagos, fraude, integridad transaccional | autoridad, reconciliación, continuidad regulatoria |
| Salud | atención, datos clínicos, seguridad paciente | seguridad humana, acceso de emergencia, titular |
| Gobierno | servicio público, expedientes y confidencialidad | continuidad democrática/servicio, ENS y obligaciones |

## 11. Salida del workshop

- AM-A: mapeo MAGERIT por activo.
- RS: escenario y riesgo.
- CTL: controles con evidencia.
- PB: ramas del playbook por servicio.
- DEC: decisiones pendientes.
- GAP: brechas, dueño y plazo.

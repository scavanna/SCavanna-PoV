# 12. Formularios operativos (plantillas vacías · v2.0 con trazabilidad DD##, ACT-### y KPIs)

**Uso:** copiar a un repositorio de incidente aprobado y restringido. No guardar datos personales, evidencias reales, contraseñas ni contactos sensibles en esta carpeta portable. Utilizar UTC y `INC-ID`/`EV-ID` estables. Los Excel ofrecen columnas editables; estas fichas ayudan en modo fuera de banda.

## F1. Apertura y triage

```text
INC-ID: ___________________   Apertura UTC: ____________  Operador: ____________
Origen de alerta/reporte: __________________  Evento UTC / ingesta UTC: ____________
Hechos observados (con EV-ID): _________________________________________________
Hipótesis / confianza / contraevidencia: ________________________________________
Funciones, sistemas, usuarios, datos y respaldos afectados:
  Confirmados: __________________ Posibles: ______________ No revisados: ________
Señales DE-*: ____________  Nivel provisional: ________  CI avisado UTC: _______
Siguiente validación y plazo: ___________________________________________________
```

## F2. BIA y contingencia por función

```text
Proceso / dueño / suplente: ______________________________________________________
Servicio mínimo y dependencia de identidad/red/proveedor: ________________________
Interrupción UTC: ______ RTO aprobado (h): ______ RPO aprobado (h): ______
Punto de activación del modo degradado: __________________________________________
Operación alternativa / límites de seguridad y privacidad: _______________________
Transacciones manuales a reconciliar / custodio: _________________________________
Último dato válido UTC: _______ Retorno aceptado UTC: ________
RTO/RPO medidos y excepciones: ______  Aprobación de negocio: ____________________
```

## F3. Orden de contención / repudio

```text
INC-ID / PB-ID / DD-ID (DD10/11/14/18): ______ Acción propuesta / ámbito exacto: ______
Evidencia que la justifica (EV-ID): ______ Riesgo de no actuar: ___________________
Impacto potencial en negocio y seguridad: ______ Alternativa: ___________________
Autorizador y UTC: ______ Operador y UTC: ______ Tarea registrada: _______________
Estado anterior / plan de reversión: _____________________________________________
Resultado plataforma: _______ Efecto independiente verificado UTC: ______________
Actividad residual / próxima observación: _______________________________________
```

## F4. Cadena de custodia

```text
EV-ID / INC-ID: _______ Fuente / intervalo UTC / filtros: _______________________
Autorización: _______ Método / herramienta / versión: _______ Operador: _________
Captura UTC: _______ Formato / tamaño: _______ SHA-256 si aplica: ______________
Depósito aprobado restringido (referencia, no enlace público): _________________
Transferencia de / a / UTC / motivo / integridad comprobada / acuse: ____________
Clasificación / hold / retención aprobada por Legal: ____________________________
Limitaciones, alteraciones previas o huecos: _____________________________________
```

## F5. Mensaje y aprobación

```text
INC-ID / versión: ______ Audiencia: ______ Objetivo y canal seguro: _____________
Hechos confirmados y EV-ID: ____________ Desconocidos declarados: _______________
Obligación / jurisdicción / hecho disparador / reloj validado: _________________
Texto EXACTO propuesto (adjuntar copia versionada): _____________________________
Legal / privacidad / negocio / Comms / portavoz y UTC: __________________________
Destinatario verificado por: ______ Envío UTC / acuse / ID de mensaje: _________
Próxima revisión / corrección de versión anterior: ______________________________
```

## F6. Evaluación o ejercicio

```text
ID de evaluación/prueba: ______ Fecha UTC: ______ Inicial / Trimestral / E1 / E2 / E3
Escenario, perímetro, permisos, reglas de parada y observador: _________________
CT-*, DE-*, PB-*, ACT-### / ritual R## y KPIs (K##/KSG##) medidos: ______________
Objetivos aprobados antes de probar (RTO/RPO y tiempos si aplican): _____________
Cronología UTC de señal → decisión → efecto → evidencia → negocio/comunicación: ___
Evidencia EV-ID y repositorio aprobado: __________________________________________
Resultado Aprobada / Fallida / Incompleta; criterios fallidos/no aplicables: _____
Brechas con dueño y plazo / riesgo aceptado hasta / fecha de retest: ___________
Aprobación del CI, negocio y, cuando aplique, Legal: ____________________________
```

## F7. Relevo fuera de banda

```text
INC-ID: _______ Sale / entra / UTC: _________ Canal verificado: _________________
Hechos confirmados / hipótesis / principales lagunas: ____________________________
Contenciones vigentes y reversión autorizada: ___________________________________
RTO restante de funciones críticas: ______ Próximo punto de decisión UTC: ______
Custodio y ubicación restringida de evidencia: _________________________________
Acciones, dueños y plazos / acuse de recepción del relevo: _______________________
```

**Control de calidad:** si un campo no se conoce, escribir `Desconocido` y asignar investigación; si no aplica, justificar. Un campo vacío en una evidencia de prueba **no** equivale a aprobación. Consultar [11-Fuentes-y-cobertura.md](11-Fuentes-y-cobertura.md) para alcance de las recomendaciones.

## F8. Ficha de práctica segura o validación Ninja en entorno real / laboratorio

```text
ID de práctica / Rol (ROL-01..09): ____________  Titular o suplente: ________________
Programa y módulo canónico PKG-NINJA (NT-## / código): ____________________________
Etiqueta ([LAB] / [LAB-PARCIAL] / [SOLO-PRODUCCION]): _____________________________
Control CT-* / Detección DE-* / Playbook PB-* que habilita: _______________________
Si es en producción: modo simulación/report-only activo: ______ Ventana UTC: ______
Aprobaciones previas (CI / cambio / Legal / Privacidad / RR. HH.): ________________
Plan de reversión inmediata y límite de gasto/SCU verificado: _____________________
Resultado sin pistas (Aprobada / Fallida / Incompleta) y EV-ID: ___________________
```

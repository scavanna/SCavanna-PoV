# Fuentes y límites de cobertura

[Guía de resiliencia](../README.md)

Estas referencias sustentan el diseño del kit v2.0, no acreditan controles desplegados, una evaluación ejecutada ni cumplimiento normativo. Los IDs `MS-*` y `EXT-*` permiten interpretar las referencias de las guías y los libros.

| ID | Referencia pública | Uso y límite |
| --- | --- | --- |
| `MS-01` | [Microsoft: proteger frente al ransomware](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware) | Prioridades generales, no secuencia técnica obligatoria. |
| `MS-02` | [Microsoft: plan de recuperación](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase1) | Preparación, procedimientos y pruebas; no acredita copias recuperables. |
| `MS-03` | [Microsoft: limitar el impacto](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase2) | Privilegios y detección; la eficacia depende del entorno y la configuración. |
| `MS-04` | [Microsoft: medidas de defensa](https://learn.microsoft.com/en-us/security/ransomware/protect-against-ransomware-phase3) | Prioridades de prevención; confirmar el alcance de cada medida. |
| `MS-05` | [Defender XDR: guía de respuesta](https://learn.microsoft.com/en-us/defender-xdr/playbook-responding-ransomware-m365-defender) | Contención e investigación defensiva; no es una autorización de intervención. |
| `MS-06` | [Defender for Endpoint: acciones de respuesta](https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts) | Confirmar permisos, alcance, impacto y reversión. |
| `MS-07` | [Azure: respaldo y restauración](https://learn.microsoft.com/en-us/azure/security/fundamentals/backup-plan-to-protect-against-ransomware) | Diseñar y ensayar recuperación; validar dependencias propias. |
| `MS-08` | [Microsoft Support: restaurar OneDrive](https://support.microsoft.com/en-us/office/restore-your-onedrive-fa231298-759d-41cf-bcd0-25ac53eb8a15) | Restitución de archivos dentro del alcance del producto, no recuperación integral. |
| `MS-09` | [Defender XDR: evaluación y piloto](https://learn.microsoft.com/en-us/defender-xdr/eval-overview) | Planificar pruebas y cobertura; una licencia no verifica instalación. |
| `MS-10` | [Microsoft Entra: revocar acceso](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) | El efecto de la revocación depende de la aplicación, la sesión y el protocolo. |
| `EXT-01` | [CISA: StopRansomware Guide](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) | Referencia general; validar el texto aplicable antes de atribuirle procedimientos. |
| `EXT-02` | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Referencia para gestión de incidentes, no declaración de conformidad. |
| `EXT-03` | [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/final) | Referencia de continuidad; ajustar las pruebas y objetivos al negocio. |

Las referencias `INT-*` de la edición original corresponden a antecedentes consultados parcialmente. No se incluyen sus documentos ni se usan como evidencia de implantación. Los ejercicios E1–E3, criterios de aceptación y plazos operativos son propuestas del kit; verificá el mandato, la jurisdicción y los niveles de servicio propios.

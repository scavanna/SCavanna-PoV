Para Microsoft, un incidente es un contenedor de alertas correlacionadas que cuenta la historia de un ataque: un objeto de investigación, no una declaración de que hubo daño. Los clientes que discrepan usan la palabra en el sentido de sus marcos de gobierno, donde "incidente" implica compromiso o impacto y dispara obligaciones.

## Cómo lo define Microsoft

| Ámbito            | Definición                                                   |
| ----------------- | ------------------------------------------------------------ |
| Defender XDR      | Las alertas son señales de eventos maliciosos o sospechosos; los incidentes son contenedores de alertas relacionadas que cuentan la historia completa de un ataque. [[Incidents...soft Learn \| Learn.Microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/incidents-overview) |
| Sentinel          | Archivos que agregan toda la evidencia relevante de una investigación. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents) Incluyen alertas, entidades, comentarios y acciones. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/sentinel/incident-investigation) |
| SAF Modern SecOps | La alerta indica una posible anomalía técnica; el incidente representa la operación del atacante. [[Microsoft...ern SecOps \| PowerPoint\]](https://microsoft-my.sharepoint.com/personal/scavanna_microsoft_com/_layouts/15/Doc.aspx?sourcedoc={5A8EE17C-DE5C-4E09-91B1-B577C5709B3C}&file=Microsoft Security ADS - 3 - Modern SecOps.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1) |

Dos detalles explican la fricción:

- **Una sola alerta puede crear un incidente.** Si la alerta es suficientemente única, Defender abre un incidente nuevo. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/alerts-incidents-correlation)
- **El veredicto llega al cierre.** Defender clasifica en verdadero positivo, falso positivo o actividad informativa esperada.  Sentinel agrega "positivo benigno" e "indeterminado".  Es decir, el propio producto admite que un "incidente" termine siendo un falso positivo. [[learn.microsoft.com\]](https://learn.microsoft.com/defender-xdr/managed-detection-and-response-xdr) [[techcommun...rosoft.com\]](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what’s-new-improved-incident-closing-experience-is-now-available/1278807)

Microsoft ya se mueve hacia otra palabra: los "casos de incidente" son la experiencia recomendada, y un caso se define como un elemento de trabajo. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management)

## Por qué algunos clientes no están de acuerdo

No encontré objeciones de clientes documentadas en tus correos o chats; estas razones son inferencia mía a partir de los marcos.

- **ISO 27035:** un evento indica una posible brecha; un incidente es uno o más eventos que pueden dañar activos o comprometer operaciones.  Un ataque bloqueado por el firewall es un evento, no un incidente.  Ambas son fuentes secundarias. [[sorena.io\]](https://www.sorena.io/artifacts/global/iso-27035/faq/event-vs-incident) [[advisera.com\]](https://advisera.com/27001academy/blog/2018/12/03/iso-27001-information-security-event-vs-incident-vs-non-compliance/)
- **NIST:** su glosario también recoge una definición de incidente como evento que tuvo impacto en la organización. [[csrc.nist.gov\]](https://csrc.nist.gov/glossary/term/Cybersecurity_Incident)
- **ITIL:** un incidente es una interrupción no planificada de un servicio.  Si cada incidente de Defender abre un ticket de ese tipo, la mesa de servicios se inunda. [[matrix42.com\]](https://www.matrix42.com/en/incident-management)
- **Reporte y contratos:** la palabra dispara notificaciones, métricas para el directorio y acuerdos de servicio. Un SOC que informa miles de "incidentes" por mes genera una lectura equivocada.

## Dónde el cliente tiene razón y dónde no

- **Tiene razón** en que el "incidente" del producto no equivale al incidente de su política.
- **Un ataque fallido no es un falso positivo.** Falso positivo es actividad confirmada como no maliciosa.  Un ataque real bloqueado es un verdadero positivo sin impacto; marcarlo como falso positivo distorsiona el ajuste de las detecciones. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks)
- **El impacto no se conoce al abrir el caso.** La definición principal de NIST incluye lo que pone en riesgo "de forma real o inminente".  En el caso Zava, cada etapa parecía no tener consecuencias. [[csrc.nist.gov\]](https://csrc.nist.gov/glossary/term/Cybersecurity_Incident)
- **El regulador separa incidente de materialidad.** La SEC define incidente como una ocurrencia no autorizada que pone en riesgo la confidencialidad, integridad o disponibilidad.  Solo exige divulgar los que la empresa determina materiales. [[ecfr.gov\]](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106) [[sec.gov\]](https://www.sec.gov/newsroom/press-releases/2023-139)

## Cómo conciliarlo

Mi recomendación es no discutir la palabra del producto y fijar la equivalencia en la política del cliente:

| Objeto en Defender o Sentinel                      | Término en la política del cliente                           |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Alerta                                             | Evento de seguridad                                          |
| Incidente o caso abierto                           | Caso en investigación                                        |
| Cerrado como falso positivo                        | Detección errónea                                            |
| Cerrado como actividad esperada o positivo benigno | Actividad autorizada                                         |
| Verdadero positivo sin impacto                     | Ataque fallido o contenido                                   |
| Verdadero positivo con compromiso                  | Incidente declarado, que activa respuesta y evaluación de materialidad |

No vi en la clasificación nativa un valor para "verdadero positivo sin impacto"; la lista que revisé viene de un foro que cita la API.  Habría que marcarlo con etiquetas o con los campos personalizados de los casos. [[discuss.rapid7.com\]](https://discuss.rapid7.com/t/updated-values-for-defender-incidents-plugin/49398) [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management)
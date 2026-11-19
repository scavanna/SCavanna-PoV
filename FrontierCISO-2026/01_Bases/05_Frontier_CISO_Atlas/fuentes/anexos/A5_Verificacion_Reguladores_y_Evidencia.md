> **Anexo del Frontier CISO Atlas 1.0.** Informe de verificación de Reguladores e informes de evidencia, hecho el 15 de noviembre de 2026 contra las páginas de los organismos emisores. Es el informe tal como lo entregó el agente de verificación; la base consolidada está en `data/base_de_referencia.json` y el resumen en `docs/04_Base_de_Referencia.md`.

# Base de referencia verificada: reguladores e informes de evidencia (estado al 15-nov-2026)

## Resumen

- **UE.** El Reglamento de IA fue modificado por el Reglamento (UE) 2026/1744 («Ómnibus digital de IA», en vigor el 27-jul-2026), que corre el alto riesgo a 2-dic-2027 (Anexo III) y 2-ago-2028 (Anexo I). NIS2, DORA y CRA están vigentes; el CRA ya exige notificación desde el 11-sep-2026.
- **Reino Unido y EE. UU.** El proyecto de ley británico sigue sin sanción real: los Comunes tratan las enmiendas de los Lores el 24-nov-2026. La regla final de CIRCIA no está publicada: está en revisión en la Casa Blanca desde el 1-oct-2026.
- **América Latina.** Hay normas nuevas en casi todos los países pedidos. Destacan el BCRA (aviso en 1 hora), Chile (Ley 21.719 desde el 1-dic-2026), Ecuador (ley de ciberseguridad de mayo de 2026) y Uruguay (aviso al CERTuy en 24 h).
- **Evidencia.** Las ediciones más recientes son DBIR 2026, WEF GCO 2026, ENISA ETL 2026, IBM 2026, ISC2 2025, Microsoft DDR 2026, M-Trends 2026 y McKinsey State of AI 2026.
Se agotó el cupo de búsquedas antes de cerrar algunas verificaciones; están marcadas «parcial» o «no verificado».

## Parte A — Regulación

**A1 · UE — Reglamento de IA**
- `tipo` regulacion · `organismo` Unión Europea (Comisión / Oficina de IA) · `artefacto` Reglamento de Inteligencia Artificial · `identificador` Reglamento (UE) 2024/1689, modificado por Reglamento (UE) 2026/1744 · `version_o_edicion` texto modificado por 2026/1744
- `fecha`: en vigor el 1-ago-2024 y aplicable en general desde el 2-ago-2026.
- `estado`: vigente, con calendario escalonado.
  - 2-feb-2025: prácticas prohibidas y alfabetización en IA; 2-ago-2025: gobernanza y obligaciones para modelos de propósito general.
  - 2-dic-2026: nuevas prohibiciones y fin del plazo de gracia del art. 50(2) para sistemas generativos ya comercializados antes del 2-ago-2026.
  - 2-dic-2027 (alto riesgo, Anexo III) y 2-ago-2028 (alto riesgo en productos, Anexo I), confirmado en el art. 113 modificado.
  - 2-ago-2030: sistemas destinados a autoridades públicas.
- `estructura_cantidad` 7 · `estructura_nombres` (arts. 9–15, títulos en inglés): Art. 9 Risk management system; Art. 10 Data and data governance; Art. 11 Technical documentation; Art. 12 Record-keeping; Art. 13 Transparency and provision of information to deployers; Art. 14 Human oversight; Art. 15 Accuracy, robustness and cybersecurity.
- `cifras` []
- `url_oficial`: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng · https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng · https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- `novedades_2025_2026`:
  - Ómnibus de IA propuesto el 19-nov-2025, acuerdo político el 7-may-2026, en vigor el 27-jul-2026; firmado el 8-jul-2026 y publicado en el DO el 24-jul-2026.
  - Agrega la prohibición de contenido íntimo no consentido y CSAM, refuerza a la Oficina de IA y centraliza la supervisión de sistemas basados en modelos de propósito general, y extiende facilidades de pymes a empresas de mediana capitalización.
  - El art. 4 pasa a exigir «medidas para apoyar» la alfabetización en IA.
  - Primera norma armonizada publicada en el DO el 19-oct-2026.
  - El resto del paquete ómnibus (RGPD, ePrivacy, NIS2, Data Act) sigue en negociación y no es ley.
- `verificado` si · `nota`: los títulos de los arts. 9–15 salen de https://artificialintelligenceact.eu/section/3-2/ porque EUR-Lex no devolvió el texto completo del 2024/1689.

**A2 · UE — NIS2 y Reglamento de Ejecución**
- `tipo` regulacion · `organismo` Unión Europea · `artefacto` Directiva NIS2 y su reglamento de ejecución · `identificador` Directiva (UE) 2022/2555; Reglamento de Ejecución (UE) 2024/2690 · `version_o_edicion` textos originales, sin modificaciones adoptadas
- `fecha`: transposición a más tardar el 17-oct-2024 y aplicación desde el 18-oct-2024 (art. 41). El reglamento de ejecución se adoptó el 17-oct-2024 y se publicó al día siguiente; en vigor el 7-nov-2024 según fuentes secundarias.
- `estado`: vigente. Plazos del art. 23: alerta temprana en 24 h, notificación en 72 h, informe final a un mes de la notificación.
- `estructura_cantidad` 10 medidas; anexo de 13 secciones.
- `estructura_nombres` (art. 21(2)): (a) políticas de análisis de riesgos y seguridad de los sistemas; (b) gestión de incidentes; (c) continuidad y gestión de crisis; (d) seguridad de la cadena de suministro; (e) seguridad en adquisición, desarrollo y mantenimiento, con gestión y divulgación de vulnerabilidades; (f) evaluación de la eficacia de las medidas; (g) ciberhigiene básica y formación; (h) criptografía y cifrado; (i) seguridad de recursos humanos, control de acceso y gestión de activos; (j) autenticación multifactor o continua y comunicaciones seguras.
- Secciones del anexo del 2024/2690: 1 Policy on the security of network and information systems; 2 Risk management policy; 3 Incident handling; 4 Business continuity and crisis management; 5 Supply chain security; 6 Security in network and information systems acquisition, development and maintenance; 7 Policies and procedures to assess the effectiveness of cybersecurity risk-management measures; 8 Basic cyber hygiene practices and security training; 9 Cryptography; 10 Human resources security; 11 Access control; 12 Asset management; 13 Environmental and physical security.
- `cifras` []
- `url_oficial`: https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng · https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj/eng
- `novedades_2025_2026`:
  - Propuesta de modificación COM(2026) 13 final (20-ene-2026, 2026/0012(COD)): certificación como vía de cumplimiento, más rol de ENISA, categoría de mediana capitalización, políticas nacionales de migración a criptografía poscuántica y recolección de datos de ransomware.
  - Informe de la ponente del 22-sep-2026; informe de la Presidencia irlandesa previsto para el 1-dic-2026. Sin adopción.
  - Fuente: https://www.europarl.europa.eu/legislative-train/package-digital-package/file-targeted-amendments-to-the-nis2-directive
- `verificado` si (texto) / parcial (transposición) · `nota`: el reglamento de ejecución solo obliga a proveedores digitales (DNS, nube, centros de datos, servicios gestionados, etc.). Último dato de transposición hallado: 22 de 27 Estados a marzo de 2026 (Skadden).

**A3 · UE — DORA**
- `tipo` regulacion · `organismo` Unión Europea (EBA, EIOPA, ESMA) · `artefacto` Reglamento de resiliencia operativa digital · `identificador` Reglamento (UE) 2022/2554 · `version_o_edicion` texto original
- `fecha`/`estado`: vigente; aplicable desde el 17-ene-2025.
- `estructura_cantidad` 5 pilares (capítulos II–VI) · `estructura_nombres`: II ICT risk management; III ICT-related incident management, classification and reporting; IV Digital operational resilience testing; V Managing of ICT third-party risk (incluye la supervisión de proveedores críticos); VI Information-sharing arrangements.
- `cifras` []
- `url_oficial`: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554 · https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en
- `novedades_2025_2026`: el 18-nov-2025 las autoridades europeas publicaron la primera lista de proveedores TIC críticos: 19 empresas.
- `verificado` si (fecha y estructura) / parcial (lista de críticos, por fuentes secundarias) · `nota`: los plazos de reporte están en normas técnicas no relevadas.

**A4 · UE — Reglamento de Ciberresiliencia (CRA)**
- `tipo` regulacion · `organismo` Unión Europea (Comisión, ENISA) · `artefacto` Cyber Resilience Act · `identificador` Reglamento (UE) 2024/2847, de 23-oct-2024 · `version_o_edicion` texto original
- `fecha`: en vigor el 10-dic-2024; capítulo IV (organismos notificados) desde el 11-jun-2026; notificación desde el 11-sep-2026 y obligaciones principales desde el 11-dic-2027.
- `estado`: vigente, en aplicación parcial.
- `estructura_cantidad` 3 pasos de notificación (art. 14) · `estructura_nombres`: alerta temprana en 24 h; notificación en 72 h; informe final a 14 días de la medida correctiva (vulnerabilidad explotada) o a un mes (incidente grave).
- `cifras` []
- `url_oficial`: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act · https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- `novedades_2025_2026`: guía práctica de la Comisión del 27-jul-2026; la notificación alcanza también a productos ya comercializados antes del 11-dic-2027.
- `verificado` si · `nota`: multas de hasta 15 millones de euros o 2,5 % de la facturación mundial. La fecha del 11-jun-2026 proviene de transcripciones del art. 71.

**A5a · Reino Unido — NCSC Cyber Assessment Framework**
- `tipo` regulacion · `organismo` NCSC · `artefacto` Cyber Assessment Framework · `identificador` CAF · `version_o_edicion` 4.0
- `fecha`: registro de cambios al 4-ago-2025; anuncio del NCSC del 6-ago-2025 · `estado`: vigente.
- `estructura_cantidad` 4 objetivos, 14 principios, 41 resultados contribuyentes.
- `estructura_nombres`:
  - A Managing security risk: A1 Governance, A2 Risk Management, A3 Asset Management, A4 Supply Chain.
  - B Protecting against cyber attack: B1 Service Protection Policies, Processes and Procedures, B2 Identity and Access Control, B3 Data Security, B4 System Security, B5 Resilient Networks and Systems, B6 Staff Awareness and Training.
  - C Detecting cyber security events: C1 Security Monitoring, C2 Threat Hunting.
  - D Minimising the impact of cyber security incidents: D1 Response and Recovery Planning, D2 Lessons Learned.
- `cifras` []
- `url_oficial`: https://www.ncsc.gov.uk/collection/cyber-assessment-framework · https://www.ncsc.gov.uk/files/NCSC-Cyber-Assessment-Framework-4.0.pdf
- `novedades_2025_2026`: versión 4.0; nuevo perfil base, que fija un mínimo de resiliencia frente a adversarios moderadamente sofisticados y apoya la transición a la 4.0.
- `verificado` si · `nota`: conté 41 resultados en el PDF de la 4.0; una guía gubernamental aún cita 39.

**A5b · Reino Unido — Cyber Security and Resilience (Network and Information Systems) Bill**
- `tipo` regulacion · `organismo` Parlamento del Reino Unido (DSIT) · `artefacto` proyecto de ley · `identificador` Bill 4035 · `version_o_edicion` Bill 175 2026-27 (Lords Amendments), 3-nov-2026
- `fecha`: primera lectura en los Comunes el 12-nov-2025; tercera lectura en los Comunes el 16-jun-2026; tercera lectura en los Lores el 2-nov-2026.
- `estado`: proyecto sin sanción real. Vuelve a los Comunes para tratar las enmiendas de los Lores el 24-nov-2026; el plazo de caducidad se extendió al 29-abr-2027.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras` []
- `url_oficial`: https://bills.parliament.uk/bills/4035
- `novedades_2025_2026`: todo el trámite ocurrió en este período.
- `verificado` si · `nota`: modifica las NIS Regulations 2018.

**A6 · EE. UU. — CIRCIA**
- `tipo` regulacion · `organismo` CISA (DHS) · `artefacto` regla de notificación de incidentes · `identificador` Cyber Incident Reporting for Critical Infrastructure Act of 2022; RIN 1670-AA04; futura 6 CFR Part 226 · `version_o_edicion` propuesta de 2024; regla final pendiente
- `fecha`: propuesta publicada el 4-abr-2024.
- `estado`: sin regla final. CISA la envió a la Oficina de Gestión y Presupuesto, tras incumplir su meta de septiembre (1-oct-2026); seguía en revisión al 11-nov-2026 según MeriTalk. Hasta que rija, el reporte es voluntario.
- `estructura_cantidad` 2 obligaciones · `estructura_nombres`: 72 horas para incidentes «sustanciales» y 24 horas para pagos de rescate, en 16 sectores.
- `cifras` []
- `url_oficial`: https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=1670-AA04&pubId=202504
- `novedades_2025_2026`: plazo legal de octubre de 2025 incumplido y meta interna de mayo de 2026 también; envío a revisión el 1-oct-2026.
- `verificado` parcial · `nota`: cisa.gov no se pudo abrir. Hay sitios que afirman que la regla final ya salió; las fuentes fechadas en octubre y noviembre lo contradicen. Respaldo: https://www.meritalk.com/articles/cisa-updates-cyber-incident-reporting-form-as-circia-rule-awaits-white-house-review/

**A7a · Comité de Basilea — Principios de resiliencia operativa**
- `tipo` regulacion · `organismo` BCBS (BIS) · `artefacto` Principles for operational resilience · `identificador` ISBN 978-92-9259-467-1 · `version_o_edicion` marzo de 2021
- `fecha` 31-mar-2021 · `estado` vigente («Current» en bis.org).
- `estructura_cantidad` 7 · `estructura_nombres`: Governance; Operational risk management; Business continuity planning and testing; Mapping interconnections and interdependencies; Third-party dependency management; Incident management; ICT including cyber security.
- `cifras` []
- `url_oficial`: https://www.bis.org/publications/202103-guidelines-principles-operational-resilience
- `novedades_2025_2026`: no verificado.
- `verificado` si (documento) / no (novedades) · `nota`: no pude confirmar si Basilea publicó la versión final de sus principios sobre riesgo de terceros.

**A7b · FSB — Formato FIRE**
- `tipo` regulacion · `organismo` Financial Stability Board · `artefacto` Format for Incident Reporting Exchange · `identificador` P150425-1 · `version_o_edicion` informe final
- `fecha` 15-abr-2025 · `estado` publicado, de adopción voluntaria.
- `estructura_cantidad` 4 grupos; 87 ítems de información, 39 opcionales · `estructura_nombres`: Reporting Details; Incident Details; Impact Assessment; Incident Closure.
- `cifras` []
- `url_oficial`: https://www.fsb.org/2025/04/format-for-incident-reporting-exchange-fire-final-report/ · https://www.fsb.org/uploads/P150425-1.pdf
- `novedades_2025_2026`: paquete de taxonomía legible por máquina; taller de revisión con industria y autoridades en 2027.
- `verificado` si · `nota`: el formato no fija umbrales ni plazos de reporte.

**A8-AR · Argentina**
- `tipo` regulacion · `organismo` BCRA; Centro Nacional de Ciberseguridad; AAIP · `artefacto` normas de ciberseguridad financiera y datos personales · `identificador` Com. «A» 7724; Com. «A» 8280; Ley 25.326 · `version_o_edicion` textos ordenados vigentes
- `fecha`: «A» 7724 del 10-mar-2023 (vigencia a los 180 días); «A» 8280 del 17-jul-2025 (vigencia 18-jul-2025).
- `estado`: vigentes. Plazos BCRA: aviso inicial dentro de la primera hora de ocurrido o detectado el incidente importante o crítico; actualizaciones frecuentes; reporte de cierre en no más de 5 días corridos.
- `estructura_cantidad` 3 · `estructura_nombres`: requisitos mínimos de riesgos de tecnología y seguridad de la información («A» 7724); lineamientos de respuesta y recuperación ante ciberincidentes («A» 8280, que actualiza la «A» 7266); protección de datos (Ley 25.326).
- `cifras` []
- `url_oficial`: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7724.pdf · https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-rrci.pdf · https://www.boletinoficial.gob.ar/detalleAviso/primera/341893/20260513
- `novedades_2025_2026`: la «A» 8280 alcanza también a proveedores de servicios de pago e infraestructuras de mercado. El Decreto 941/2025 (31-dic-2025) creó el Centro Nacional de Ciberseguridad; su Disposición 1/2026 fija planes de contingencia para el sector público. Proyecto de ley de datos 3397-D-2026 (16-jul-2026).
- `verificado` si (BCRA y Centro) / parcial (datos) · `nota`: el plazo de aviso de brechas bajo la Ley 25.326 no está verificado; el proyecto propone 72 h.

**A8-CL · Chile**
- `tipo` regulacion · `organismo` ANCI; Agencia de Protección de Datos Personales; CMF · `artefacto` ley marco, ley de datos y normas bancarias · `identificador` Ley 21.663; Ley 21.719; RAN capítulos 20-10 y 20-8 · `version_o_edicion` textos vigentes
- `fecha`: Ley 21.663 publicada el 8-abr-2024, rige desde el 1-ene-2025 (fuentes secundarias). Ley 21.719 publicada el 13-dic-2024, entra en vigencia el 1-dic-2026 (BCN).
- `estado`: Ley 21.663 vigente; Ley 21.719 a 16 días de regir. Plazos:
  - ANCI: alerta temprana en 3 h e informe final en 15 días corridos (fuente oficial); segundo reporte en 72 h, o 24 h para operadores de importancia vital (fuentes secundarias).
  - CMF: 30 minutos desde la ocurrencia del incidente operacional.
  - Ley 21.719: «sin dilaciones indebidas», sin plazo en horas.
- `estructura_cantidad` 3 · `estructura_nombres`: Ley Marco de Ciberseguridad; ley de protección de datos; capítulos de la RAN sobre ciberseguridad e incidentes operacionales.
- `cifras` []
- `url_oficial`: https://anci.gob.cl/preguntas-frecuentes/preguntas-frecuentes-portal-anci/ · https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01 · https://www.cmfchile.cl/portal/normativa/624/articles-28983_doc_pdf.pdf?ts=1746206514
- `novedades_2025_2026`: reglamento de reporte (Decreto 295, 1-mar-2025). Nómina de operadores de importancia vital: Resolución Exenta 87 (16-dic-2025) y Resolución Exenta 187 (24-jul-2026); total 1.154 según fuentes secundarias.
- `verificado` si / parcial (72 h, 24 h y total de operadores).

**A8-CO · Colombia**
- `tipo` regulacion · `organismo` Superintendencia Financiera; SIC · `artefacto` circulares de ciberseguridad y ley de datos · `identificador` Circular Externa 007 de 2018; Circular Externa 033 de 2020; Ley 1581 de 2012 · `version_o_edicion` vigentes
- `fecha`: junio de 2018 y noviembre de 2020 · `estado`: vigentes. Plazo de datos: 15 días hábiles para reportar a la SIC. Plazo de reporte a la Superintendencia Financiera: no verificado.
- `estructura_cantidad` 3 · `estructura_nombres`: requerimientos mínimos de gestión del riesgo de ciberseguridad; taxonomía única de incidentes cibernéticos y métricas; protección de datos.
- `cifras` []
- `url_oficial`: https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1031904 · https://sedeelectronica.sic.gov.co/publicaciones/boletin-juridico/concepto/cumplimiento-de-la-obligacion-del-reporte-de-incidentes-de-seguridad
- `novedades_2025_2026`: la Circular Básica Jurídica fue reexpedida por la Circular Externa 006 de 2025 (26-jun-2025), según fuente secundaria. Un proyecto de Agencia Nacional de Seguridad Digital y Asuntos Espaciales fue archivado el 20-jun-2025.
- `verificado` parcial · `nota`: no hallé ley que cree la agencia digital. La Ley 2603 de 2026 crea la Agencia Nacional de Seguridad Nuclear, no digital. Estado de un nuevo proyecto: no verificado.

**A8-MX · México**
- `tipo` regulacion · `organismo` Secretaría Anticorrupción y Buen Gobierno; CNBV; Agencia de Transformación Digital y Telecomunicaciones · `artefacto` ley de datos, disposiciones bancarias y política de ciberseguridad · `identificador` LFPDPPP (DOF 20-mar-2025); disposiciones para instituciones de crédito, arts. 168 Bis 11 a 168 Bis 17; Acuerdo DOF 17-dic-2025 · `version_o_edicion` LFPDPPP con última reforma DOF 14-nov-2025
- `fecha`: LFPDPPP en vigor al día siguiente de su publicación.
- `estado`: vigente. Plazo de datos: aviso «de forma inmediata» al titular (art. 19), sin plazo en horas. CNBV: aviso inmediato e información en 5 días hábiles, según fuente secundaria.
- `estructura_cantidad` 3 · `estructura_nombres`: ley de datos de 2025; seguridad de la información bancaria; Política General de Ciberseguridad para la Administración Pública Federal.
- `cifras` []
- `url_oficial`: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf · https://www.gob.mx/cms/uploads/attachment/file/1043595/2025_12_17_MAT_atdt.pdf · https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf
- `novedades_2025_2026`: nueva ley de datos; política de ciberseguridad federal; Plan Nacional de Ciberseguridad 2025–2030 presentado en diciembre de 2025, que prevé una ley general.
- `verificado` parcial · `nota`: la ley de ciberseguridad no estaba vigente al 19-oct-2026 (iniciativas en el Senado sin dictamen), según fuentes secundarias. No extraje el texto oficial de la CNBV.

**A8-PE · Perú**
- `tipo` regulacion · `organismo` Autoridad Nacional de Protección de Datos Personales; PCM (Centro Nacional de Seguridad Digital) · `artefacto` reglamento de datos y marco de confianza digital · `identificador` DS 016-2024-JUS; DU 007-2020; DS 126-2025-PCM · `version_o_edicion` vigentes
- `fecha`: DS 016-2024-JUS publicado el 30-nov-2024, vigente a los 120 días calendario (30-mar-2025). DS 126-2025-PCM dado el 4-nov-2025, vigente a los 90 días de publicado (febrero de 2026).
- `estado`: vigentes. Plazo de datos: 48 horas desde que se toma conocimiento del incidente.
- `estructura_cantidad` 2 · `estructura_nombres`: reglamento de la Ley 29733; Marco de Confianza Digital y su reglamento.
- `cifras` []
- `url_oficial`: https://www3.congreso.gob.pe/Docs/DGP/DIDP/files/ds_016-2024-jus.pdf · https://busquedas.elperuano.pe/dispositivo/EX/2455024-1
- `novedades_2025_2026`: ambos reglamentos entraron en vigor en este período.
- `verificado` parcial · `nota`: no verifiqué una ley marco de ciberseguridad aprobada ni el texto de la norma de la SBS; los plazos de aviso al Centro Nacional de Seguridad Digital no fueron extraídos.

**A8-UY · Uruguay**
- `tipo` regulacion · `organismo` AGESIC (CERTuy); URCDP; BCU · `artefacto` decreto de ciberseguridad, decreto de datos y circular bancaria · `identificador` Ley 20.212 arts. 78–84 y Decreto 66/025; Ley 18.331 y Decreto 64/020; Circular BCU 2497 · `version_o_edicion` vigentes
- `fecha`: Decreto 66/025 publicado el 14-mar-2025; Decreto 64/020 publicado el 21-feb-2020; Circular 2497 del 28-ene-2026.
- `estado`: vigentes. Plazos: 24 horas al CERTuy (sectores críticos); 72 horas a la URCDP (datos).
- `estructura_cantidad` 3 · `estructura_nombres`: marco de ciberseguridad y cometidos del CERTuy; protección de datos; seguridad de instrumentos electrónicos.
- `cifras` []
- `url_oficial`: https://www.impo.com.uy/bases/decretos/66-2025 · https://www.impo.com.uy/bases/decretos/64-2020/4 · https://www.bcu.gub.uy/Circulares/seggci2497.pdf
- `novedades_2025_2026`: Decreto 66/025; Circular 2497 (autenticación reforzada), vigente desde el 1-oct-2026 según fuente secundaria.
- `verificado` si (decretos) / parcial (BCU) · `nota`: una fuente secundaria indica 4 horas para el reporte inicial en el sistema de pagos; no lo verifiqué en el BCU.

**A8-CR · Costa Rica**
- `tipo` regulacion · `organismo` CONASSIF (superintendencias); PRODHAB; MICITT · `artefacto` reglamento financiero de TI y ley de datos · `identificador` Acuerdo CONASSIF 5-24; Ley 8968 · `version_o_edicion` CONASSIF 5-24 versión del 15-jul-2025
- `fecha`: CONASSIF 5-24 aprobado el 15-jul-2024 y publicado el 22-jul-2024.
- `estado`: vigentes. Sin ley marco de ciberseguridad verificada. El art. 39 exige comunicar incidentes de impacto «moderado» o «alto»; los plazos están en lineamientos no extraídos.
- `estructura_cantidad` 2 · `estructura_nombres`: Reglamento General de Gobierno y Gestión de la Tecnología de Información; ley de protección de datos.
- `cifras` []
- `url_oficial`: https://www.sugef.fi.cr/normativa/normativa_transversal/documentos/CONASSIF%205-24%20%28v03%2015%20julio%202025%29.pdf
- `novedades_2025_2026`: proyecto de reforma de la Ley 8968 que propone avisar a PRODHAB en 72 h (BDO, 2026). Proyectos de ciberseguridad en los expedientes 23.292 y 24.007.
- `verificado` parcial · `nota`: plazo vigente de aviso de brechas y estado de los proyectos: no verificados.

**A8-PA · Panamá**
- `tipo` regulacion · `organismo` ANTAI; Asamblea Nacional; Superintendencia de Bancos · `artefacto` ley de datos, proyecto de ley marco y acuerdo bancario · `identificador` Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021; Proyecto de Ley 627 · `version_o_edicion` vigentes
- `fecha`: decreto del 28-may-2021; proyecto presentado el 9-mar-2026 y prohijado el 29-abr-2026.
- `estado`: ley de datos vigente; ley marco pendiente de primer debate. Plazo de datos: 72 horas desde que se conoce el incidente.
- `estructura_cantidad` 3 · `estructura_nombres`: protección de datos; Ley Marco de Ciberseguridad (proyecto); acuerdo bancario sobre gobernanza de TI, seguridad de la información y ciberseguridad.
- `cifras` []
- `url_oficial`: https://antai.gob.pa/wp-content/uploads/2021/05/Reglamentacio%CC%81n-de-Ley-81-de-Proteccio%CC%81n-de-Datos-Personales.pdf · https://sistemas.asamblea.gob.pa/segLegis/Documents/8317.pdf
- `novedades_2025_2026`: proyecto 627; un «Acuerdo 4» bancario figura publicado en Gaceta Oficial el 13-nov-2026 según vLex (https://vlex.com.pa/vid/acuerdo-4-dictan-disposiciones-1140134458).
- `verificado` parcial · `nota`: el acuerdo bancario no fue confirmado en fuente oficial.

**A8-EC · Ecuador**
- `tipo` regulacion · `organismo` MINTEL; Superintendencia de Protección de Datos Personales · `artefacto` ley de ciberseguridad y ley de datos · `identificador` Ley Orgánica para el Fortalecimiento de la Ciberseguridad (Registro Oficial, Quinto Suplemento 290); LOPDP · `version_o_edicion` vigentes
- `fecha`: ley de ciberseguridad aprobada el 10-feb-2026 y publicada el 22-may-2026.
- `estado`: vigentes. Plazos: 72 horas desde la detección para entidades públicas e infraestructura crítica digital; 5 días a la autoridad de datos y 3 días a los titulares.
- `estructura_cantidad` 2 · `estructura_nombres`: ley de ciberseguridad (reforma la Ley Orgánica para la Transformación Digital y Audiovisual); ley de protección de datos.
- `cifras` []
- `url_oficial`: no obtenida. Respaldo: https://www.pbplaw.com/es/publicaciones/ley-organica-para-el-fortalecimiento-de-la-ciberseguridad-1/ · https://dds.ec/normativa/ley-ciberseguridad-ecuador/
- `novedades_2025_2026`: nueva ley de ciberseguridad; norma técnica de notificación de vulneraciones (Resolución SPDP-SPD-2026-0040-R).
- `verificado` parcial · `nota`: todo proviene de estudios jurídicos; no abrí el Registro Oficial.

## Parte B — Evidencia

**B9 · Verizon — Data Breach Investigations Report**
- `tipo` evidencia · `organismo` Verizon · `artefacto` DBIR · `identificador` 19.ª edición · `version_o_edicion` 2026 · `fecha` 19-may-2026 · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 31 %: brechas cuyo acceso inicial fue la explotación de vulnerabilidades (abuso de credenciales: 13 %).
  - 48 %: brechas con participación de terceros, 60 % más que el año anterior.
  - 48 %: brechas con ransomware (44 % el año anterior); la mediana de rescate pagado fue USD 139.875.
  - 62 %: brechas con elemento humano (60 % el año anterior).
  - 45 %: empleados con uso frecuente de herramientas de IA (15 % un año antes).
- `url_oficial`: https://www.verizon.com/business/resources/T5d3/reports/2026-dbir-data-breach-investigations-report.pdf
- `novedades_2025_2026`: primera vez en 19 años que las vulnerabilidades superan a las credenciales robadas.
- `verificado` si · `nota`: universo de más de 31.000 incidentes y más de 22.000 brechas confirmadas en 145 países; ventana temporal no extraída.

**B10 · World Economic Forum — Global Cybersecurity Outlook**
- `tipo` evidencia · `organismo` WEF · `artefacto` Global Cybersecurity Outlook · `identificador` — · `version_o_edicion` 2026 · `fecha` 2026 (día no verificado) · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 94 %: encuestados que esperan que la IA sea el mayor factor de cambio en ciberseguridad en el año.
  - 87 %: señalan las vulnerabilidades ligadas a IA como el riesgo de más rápido crecimiento en 2025.
  - 64 %: organizaciones con procesos para evaluar la seguridad de herramientas de IA (37 % en 2025).
  - 64 %: organizaciones que contemplan ciberataques de motivación geopolítica.
  - 73 %: encuestados afectados, ellos o alguien de su red, por fraude cibernético en 2025.
- `url_oficial`: https://www.weforum.org/publications/global-cybersecurity-outlook-2026
- `novedades_2025_2026`: solo 13 % de los encuestados de América Latina y el Caribe confía en la protección de la infraestructura crítica de su país (84 % en Medio Oriente y Norte de África).
- `verificado` parcial · `nota`: cifras verificadas; tamaño de muestra y fecha exacta no.

**B11 · ENISA — Threat Landscape**
- `tipo` evidencia · `organismo` ENISA · `artefacto` ENISA Threat Landscape · `identificador` — · `version_o_edicion` 2026 · `fecha` septiembre de 2026 · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 51,3 %: incidentes registrados que fueron ataques de denegación de servicio.
  - 39,5 %: incidentes de acceso no autorizado.
  - 57,3 %: incidentes de motivación ideológica (29,3 % de motivación financiera).
  - 31,8 %: incidentes contra la administración pública, el sector más afectado.
  - 72,9 %: incidentes que afectaron a entidades esenciales de NIS2.
- `url_oficial`: https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf
- `novedades_2025_2026`: el período pasó a año calendario.
- `verificado` si · `nota`: universo de 8.257 incidentes del 1-ene al 31-dic-2025; se solapa seis meses con la edición anterior.

**B12 · IBM — Cost of a Data Breach**
- `tipo` evidencia · `organismo` IBM (investigación de Ponemon Institute) · `artefacto` Cost of a Data Breach Report · `identificador` — · `version_o_edicion` 2026 · `fecha` 2026 (mes no verificado) · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - USD 4,99 millones: costo promedio global de una brecha, 12 % más que el año anterior.
  - 56 %: aumento de los ataques impulsados por IA; suman en promedio USD 1 millón por brecha.
  - 43 %: incidentes de seguridad que involucraron IA no autorizada (20 % el año anterior).
  - 68 %: organizaciones vulneradas sin gobernanza para gestionar IA o detectar IA no autorizada (63 % antes).
  - 247 días: ciclo medio de una brecha (183 para identificar y 64 para contener).
- `url_oficial`: https://www.ibm.com/reports/data-breach
- `novedades_2025_2026`: incorpora secciones sobre IA agéntica en seguridad, identidades no humanas y criptografía poscuántica.
- `verificado` si (cifras) / parcial (fecha) · `nota`: 602 organizaciones con brechas entre marzo de 2025 y febrero de 2026; la muestra latinoamericana cubre México, Argentina, Chile y Colombia.

**B13 · ISC2 — Cybersecurity Workforce Study**
- `tipo` evidencia · `organismo` ISC2 · `artefacto` Cybersecurity Workforce Study · `identificador` — · `version_o_edicion` 2025 · `fecha` no verificada · `estado` última edición listada en isc2.org al 15-nov-2026.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 95 %: encuestados cuya organización tiene al menos una necesidad de habilidades de ciberseguridad.
  - 59 %: califican esa carencia de crítica o significativa.
  - 34 %: dicen tener la cantidad adecuada de personas (44 % solo una leve escasez).
  - 30 %: de quienes tienen carencias, reportan dificultad para contratar las habilidades buscadas.
  - 15 %: dicen que la IA genera incertidumbre sobre qué habilidades se necesitarán.
- `url_oficial`: https://www.isc2.org/research
- `novedades_2025_2026`: el problema se desplaza de la cantidad de personas a las habilidades.
- `verificado` parcial · `nota`: cifras tomadas de un análisis de ISC2 de abril de 2026 sobre «el estudio más reciente» (https://www.isc2.org/Insights/2026/04/aligning-skills-people-and-hiring-in-cybersecurity); muestra y fecha no verificadas.

**B14 · Microsoft — Digital Defense Report**
- `tipo` evidencia · `organismo` Microsoft · `artefacto` Microsoft Digital Defense Report · `identificador` — · `version_o_edicion` 2026 · `fecha` 1-oct-2026 · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 5,3 horas: tiempo promedio hasta que una carga de trabajo expuesta en la nube fue atacada.
  - 93 %: ataques de phishing por voz que retuvieron a la víctima lo suficiente para iniciar la ingeniería social.
  - 73,3 %: intentos de acceso inicial por ejecución del usuario, cuentas válidas, ingeniería social y phishing.
  - Más de 46 millones: ataques de suplantación de correo empresarial detectados.
  - 58 %: detecciones ligadas a las cinco vulnerabilidades principales que correspondieron a una sola, divulgada en 2020 (CVE-2020-1472).
- `url_oficial`: https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
- `novedades_2025_2026`: anticipa mayor uso de agentes de IA por atacantes y defensores.
- `verificado` si / parcial (período de datos no extraído).

**B15 · Mandiant (Google Cloud) — M-Trends**
- `tipo` evidencia · `organismo` Mandiant / Google Cloud · `artefacto` M-Trends · `identificador` — · `version_o_edicion` 2026 · `fecha` 23-mar-2026 · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 14 días: mediana global de permanencia (11 días el período anterior).
  - 32 %: intrusiones con exploits como vector inicial, el más común por sexto año.
  - 11 %: intrusiones iniciadas por phishing de voz, segundo vector (correo: 6 %).
  - 52 %: casos detectados internamente por la organización (43 % en 2024).
  - −7 días: tiempo medio estimado hasta la explotación, es decir, antes del parche.
- `url_oficial`: https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/
- `novedades_2025_2026`: la permanencia sube por espionaje y trabajadores de TI norcoreanos (mediana de 122 días en esos casos).
- `verificado` si · `nota`: basado en más de 500.000 horas de investigaciones de 2025.

**B16 · Adopción y riesgos de agentes de IA**
- `tipo` evidencia · `organismo` McKinsey (principal); Cloud Security Alliance (riesgo) · `artefacto` The State of AI: Global Survey 2026 · `identificador` — · `version_o_edicion` 2026 · `fecha` 25-ago-2026 · `estado` última edición.
- `estructura_cantidad` no relevada · `estructura_nombres` []
- `cifras`:
  - 40 %: encuestados de organizaciones con ingresos sobre USD 1.000 millones que están escalando agentes (27 % el año anterior).
  - 22 %: la misma proporción en organizaciones más chicas, sin cambio.
  - 32 %: organizaciones que desistieron de comprar algún software porque podían construirlo con codificación agéntica.
  - 47 %: organizaciones que reportan un incidente de seguridad con un agente de IA (CSA).
  - 54 %: organizaciones que reportan entre 1 y 100 agentes no autorizados (CSA).
- `url_oficial`: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai · https://cloudsecurityalliance.org/artifacts/enterprise-ai-security-starts-with-ai-agents
- `novedades_2025_2026`: el informe de CSA (15-abr-2026) añade que solo 13 % se siente muy preparado para la regulación de IA.
- `verificado` si (McKinsey) / parcial (CSA) · `nota`: McKinsey encuestó a 1.719 participantes de 97 países entre el 4-may y el 8-jun-2026. El informe de CSA fue encargado por un proveedor (Zenity) y no verifiqué su muestra.

## Brechas e incertidumbres

- **Fuentes que no abrieron:** cisa.gov, el texto completo del AI Act en EUR-Lex y la Ley 21.663 en la BCN.
- **Sin verificar por falta de búsquedas:**
  - estado actual de transposición de NIS2;
  - novedades de Basilea sobre riesgo de terceros;
  - el acuerdo bancario de Panamá en fuente oficial;
  - el Registro Oficial de Ecuador;
  - los plazos de la CNBV y de la Superintendencia Financiera de Colombia;
  - la muestra y fecha de ISC2 y del WEF.
- **Fuera de la lista pedida:** Guatemala aprobó el 3-nov-2026 el Decreto 26-2026, Ley Marco de Ciberseguridad (https://www.congreso.gob.gt/noticias_congreso/17397/2026/4); no verifiqué su publicación ni vigencia.

## Los 8 hallazgos para un CISO de la región

1. **El aviso en horas ya es la norma regional.** Rigen 30 minutos (CMF Chile), 1 hora (BCRA), 3 horas (ANCI Chile), 24 horas (CERTuy), 48 horas (datos en Perú) y 72 horas (datos en Uruguay y Panamá; ciberseguridad en Ecuador). Colombia mantiene 15 días hábiles y México exige aviso «inmediato» al titular.

2. **Obligaciones nuevas de 2025–2026.** Son la Com. «A» 8280 del BCRA, el Decreto 66/025 de Uruguay, la ley de ciberseguridad de Ecuador, la nueva ley de datos de México y los reglamentos peruanos. La Ley 21.719 de Chile rige desde el 1-dic-2026. Siguen como proyecto la ley general de México, la de Panamá y las de Costa Rica.

3. **La regulación europea alcanza a proveedores latinoamericanos.** El CRA exige desde el 11-sep-2026 avisar vulnerabilidades explotadas en 24 horas a quien venda productos digitales en la UE. El AI Act suma hitos el 2-dic-2026, el 2-dic-2027 y el 2-ago-2028.

4. **EE. UU. y el Reino Unido siguen pendientes.** CIRCIA mantiene los relojes de 72 y 24 horas pero no tiene regla final. El proyecto británico está en su fase final.

5. **La IA es la fuerza dominante, como catalizador y como riesgo.**
   - El 94 % la ve como principal factor de cambio (WEF).
   - Los ataques impulsados por IA crecieron 56 % (IBM).
   - La explotación de vulnerabilidades ya ocurre antes del parche (M-Trends).
   - La gobernanza va atrás: 68 % de las organizaciones vulneradas no la tenía (IBM).
   - Los agentes ya generan incidentes en 47 % de las organizaciones (CSA).

6. **Los terceros son el frente que más crece.** Participan en 48 % de las brechas (Verizon). DORA ya supervisa directamente a 19 proveedores críticos. NIS2, el CAF y Basilea tienen un requisito específico de cadena de suministro.

7. **Geopolítica y soberanía pesan más que el delito común en Europa.** El 57,3 % de los incidentes fue ideológico (ENISA). La confianza latinoamericana en la protección de infraestructura crítica es de 13 % (WEF). La revisión de la Ley de Ciberseguridad europea propone excluir proveedores de alto riesgo de las redes de telecomunicaciones.

8. **Fraude, talento y criptografía poscuántica tienen respaldo desigual.**
   - El fraude está bien respaldado: 73 % afectado (WEF) y el phishing de voz es el segundo vector de intrusión (M-Trends).
   - En talento, la carencia es de habilidades más que de personas: 59 % la califica de crítica o significativa (ISC2).
   - La criptografía poscuántica aparece como obligación propuesta en la reforma de NIS2 y como tema nuevo en IBM, pero no extraje cifras que la midan.

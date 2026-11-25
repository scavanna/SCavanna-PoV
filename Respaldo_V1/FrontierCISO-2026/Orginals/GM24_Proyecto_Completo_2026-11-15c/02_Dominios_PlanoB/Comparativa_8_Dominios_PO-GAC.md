# Comparativa de las ocho instancias de dominio del rol PO-GAC

> 2026-11-15 · Plano B. Todas comparten rol, 41 competencias, 379 conceptos (GM-24 V7.1), 24 AGC, RACI, L0–L4 y recursos comunes (5 tools, 2 knowledge, 5 skills). **Ninguna requirió conceptos nuevos en el plano A.**

| Dominio | Tecnología | Versión | Tareas | Agentes | Tools nuevos |
|---|---|---|---|---|---|
| Productividad | Defender for Office 365 (EOP) en Defender XDR | v1.1 | 31 | 15 | 0 |
| XDR | Defender XDR + sensores + Sentinel | v1.0 | 28 | 15 | 12 |
| Endpoints | Defender for Endpoint + Vulnerability Management + Intune | v1.0 | 26 | 13 | 8 |
| Identidades | Defender for Identity + Entra ID Protection + CA + ID Governance | v1.0 | 23 | 11 | 9 |
| Datos | Purview (labels, DLP, DSPM/DSPM for AI, Insider Risk) + MDA | v1.0 | 25 | 11 | 10 |
| SIEM/SOAR | Microsoft Sentinel (portal Defender) | v1.0 | 24 | 10 | 8 |
| Nube | Defender for Cloud (CSPM, CWPP, AI Services) | v1.0 | 23 | 10 | 9 |
| Apps / SaaS | Defender for Cloud Apps + app governance + CA app control | v1.0 | 26 | 11 | 10 |

**Totales:** 206 tareas · 96 agentes · 24 tools base + 66 específicos de dominio.

## Lectura

1. **Dominios de canal** (Productividad, Endpoints, Identidades, Datos): protegen una superficie con sensores propios.
2. **Dominios de plataforma** (XDR, SIEM, Nube): integran, correlacionan, automatizan y dan postura; su riesgo principal es la pérdida de visibilidad, la automatización indebida y el costo.
3. **Transversales a las flotas de agentes:** Identidades (AGC-05/06/18), Datos (AGC-07), SIEM (observabilidad, Sentinel MCP), Nube (postura de recursos de IA, AMP-51).
4. **Hitos de plataforma:** AIR embebido en MDE (1-sep-2026); Sentinel solo en el portal de Defender (31-mar-2027); multicloud en Secure Score (jun-2026).
5. **Apps/SaaS** (Dominio_APPS v1.0) cierra la hoja de ruta del plano B: gobierna consentimiento OAuth, shadow IT (incl. IA generativa) y sesiones; audita las apps OAuth de las flotas de agentes desde afuera. Hito: file policies de MDA se retiran el 6-ene-2027 (→ Purview DLP).
6. **Transversales adicionales:** Apps (permisos OAuth de agentes, AMP-33/36/50).

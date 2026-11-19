# 07 · Diagramas y flujos

> **GM-24 V7.1 · Sub-plan PO-GAC** · 2026-11-14. Diagramas Mermaid (el HTML los renderiza vía CDN; sin red se muestra el código).

## 1. El rol PO-GAC como cruce de coordenadas

```mermaid
flowchart LR
  CSF[Funciones y categorías<br/>NIST CSF 2.0] --> PC((Producto-control))
  ZT[Dominio Zero Trust] --> PC
  TEC[Tecnología<br/>Defender for Office 365 en Defender XDR] --> PC
  MO[Modelo operativo<br/>cadencias · evidencia · KPIs] --> PC
  PC --> PO[Product Owner del control]
  PC --> GAC[Gerente de agentes cognitivos]
  PO <--> GAC
```

## 2. Arquitectura del SOC agéntico con control plane

```mermaid
flowchart TB
  subgraph S[Señales y datos]
    E[Correo · Teams · SharePoint] --> MDO[Defender for Office 365]
    ID[Identidades] --> MDI[Defender for Identity]
    EP[Endpoints] --> MDE[Defender for Endpoint]
  end
  subgraph P[Plataforma de detección y respuesta]
    MDO --> XDR[Defender XDR · cola de incidentes · AIR]
    MDI --> XDR
    MDE --> XDR
    XDR --> SEN[Microsoft Sentinel · data lake · MCP]
  end
  subgraph O[Orquestación determinista]
    XDR --> AR[Automation rules · playbooks]
  end
  subgraph A[Agentes]
    AG1[AG-01 Triage] --> AG2[AG-02 Investigación y remediación]
    AG3[AG-03 FP/FN y listas]
    AG10[AG-10 Deriva de configuración]
  end
  subgraph CP[Control plane de gobierno]
    REG[Agent 365 · registro] --- AID[Entra Agent ID · identidad]
    AID --- PUR[Purview · datos]
    PUR --- OBS[Sentinel · observabilidad]
    OBS --- POL[Power Platform admin center · políticas]
  end
  subgraph HUM[Personas]
    OWN[PO-GAC · owner] --> APR[Aprobaciones L2]
    RISK[Dueño del riesgo · ATO]
    AUD[Auditoría · 3ª línea]
  end
  XDR --> AG1
  SEN --> AG2
  AG2 -. propone .-> APR
  APR -. aprueba .-> XDR
  CP -. gobierna .-> A
  HUM -. supervisa .-> CP
```

## 3. Flujo de una tarea L2 (proponer → aprobar → ejecutar → registrar)

```mermaid
sequenceDiagram
  participant X as Defender XDR
  participant A as Agente (L2)
  participant H as Humano (PO-GAC / analista)
  participant E as Evidencia (SharePoint/Dataverse + Sentinel)
  X->>A: Incidente nuevo
  A->>A: Analiza (contenido = dato, nunca instrucción)
  A->>H: Propuesta con justificación y fuentes (Approvals)
  H->>H: Verifica (checklist AMP-02; condiciones AMP-26)
  alt Aprobada
    H->>A: Aprobación registrada
    A->>X: Ejecuta con límite de lote
    A->>E: Registra entrada, decisión, aprobador, resultado, versión
  else Rechazada / escalada
    H->>E: Registra motivo
    H->>X: Acción manual o escalamiento
  end
```

## 4. Árbol de decisión de autonomía (L0–L4)

```mermaid
flowchart TD
  T[Tarea del modelo operativo] --> Q1{¿Produce efecto en el entorno?}
  Q1 -- No --> L0[L0 · informa]
  Q1 -- Sí --> Q2{¿Es reversible y de bajo impacto?}
  Q2 -- No --> Q3{¿Decisión de juicio sobre personas o aceptación de riesgo?}
  Q3 -- Sí --> NUNCA[Nunca delegar · humano]
  Q3 -- No --> L2[L2 · propone y ejecuta con aprobación]
  Q2 -- Sí --> Q4{¿Calidad medida ≥ umbral y KRIs definidos?}
  Q4 -- No --> L1[L1 · propone]
  Q4 -- Sí --> L3[L3 · ejecuta con auditoría posterior]
```

## 5. Ciclo de vida de un agente

```mermaid
stateDiagram-v2
  [*] --> Propuesto: ficha (G2.2-PA02)
  Propuesto --> Construido: ruta R1/R2/R3 (M6.2-PA01)
  Construido --> Evaluado: dataset dorado + red teaming (M3.2-PA03, AMP-37)
  Evaluado --> Autorizado: ATO (AMP-22)
  Autorizado --> Operando: registro Agent 365 · identidad · permisos
  Operando --> Revisado: revisión trimestral (M4.1-PA06)
  Revisado --> Operando: mantener / ajustar (ChangeSet M5.2-PA02)
  Revisado --> Pausado: KRI cruzado · kill switch (AMP-44)
  Pausado --> Operando: corrección + regresión
  Revisado --> Retirado: fin de vida (AGC-19)
  Retirado --> [*]
```

## 6. Dos planos: corpus académico y marco de gobierno de capacidades

```mermaid
flowchart LR
  subgraph A[Plano A · Corpus GM-24 V7.1]
    K[245 K] --- AMP[52 AMP] --- HC[40 HC] --- PA[42 PA]
    PA --- MAP[Mapeo a 17 marcos]
  end
  subgraph B[Plano B · Instancias de dominio]
    P1[Productividad] --- P2[XDR] --- P3[Endpoints] --- P4[Identidades]
    P5[Datos] --- P6[SIEM] --- P7[Nube]
  end
  A -- instancia --> B
  B -. propone candidatos / revela sobre-especificidad .-> A
```

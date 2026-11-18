#Requires -Version 7.0
param(
    [Parameter(Mandatory)][Guid]$WorkspaceId,
    [switch]$CommitSnapshot,
    [Uri]$DcrEndpoint,
    [ValidatePattern('^dcr-[a-fA-F0-9]{32}$')][string]$DcrImmutableId
)

$ErrorActionPreference = 'Stop'

function Get-AzureToken([string]$Resource) {
    $token = az account get-access-token --resource $Resource --query accessToken -o tsv --only-show-errors
    if ($LASTEXITCODE -ne 0 -or -not $token) { throw "No se pudo obtener un token Azure para $Resource. Revisar contexto e identidad." }
    return $token.Trim()
}

$required = @('SourceAlertTime','AlertKey','AlertType','MappingVersion','Disposition',
              'CandidateCAAT','CandidateATLAS','CandidateOWASP2025','CandidateOWASP2026')
if ($CommitSnapshot) {
    if (-not $DcrEndpoint -or -not $DcrImmutableId) { throw 'Indicá DcrEndpoint y DcrImmutableId para escribir.' }
    if (-not $DcrEndpoint.IsAbsoluteUri -or $DcrEndpoint.Scheme -ne 'https' -or
        $DcrEndpoint.DnsSafeHost -notmatch '^[a-z0-9-]+(\.[a-z0-9-]+)*\.ingest\.monitor\.azure\.com$' -or
        -not $DcrEndpoint.IsDefaultPort -or $DcrEndpoint.AbsolutePath -ne '/' -or
        $DcrEndpoint.UserInfo -or $DcrEndpoint.Query -or $DcrEndpoint.Fragment) {
        throw 'Usá el endpoint directo HTTPS del DCR de Azure comercial, sin ruta, puerto alternativo ni credenciales.'
    }
}

$query = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot '..\kql\14_Capturar_clasificacion.kql')
$request = @{query=$query;timespan='P2D'} | ConvertTo-Json -Compress
$result = Invoke-RestMethod -Method Post -Uri "https://api.loganalytics.azure.com/v1/workspaces/$WorkspaceId/query" `
    -Headers @{ Authorization = "Bearer $(Get-AzureToken 'https://api.loganalytics.io')" } `
    -MaximumRedirection 0 -ContentType 'application/json' -Body $request
if ($result.error) { throw "Consulta incompleta: $($result.error.code). No se escribió ninguna captura." }
$table = @($result.tables | Where-Object name -eq 'PrimaryResult')
if ($table.Count -ne 1 -or $null -eq $table[0].rows) { throw 'No se encontró la tabla PrimaryResult esperada.' }
$columns = @($table[0].columns.name)
if (($columns -join ',') -cne ($required -join ',')) { throw 'El esquema de la consulta no coincide con la lista de campos permitidos.' }
$rows = $table[0].rows
$count = $rows.Count
if ($count -gt 25000) { throw 'Más de 25.000 filas; ajustar el rango de la consulta antes de persistir.' }
if (-not $CommitSnapshot -or $count -eq 0) {
    [pscustomobject]@{ Rows = $count; Uploaded = 0; Preview = (-not $CommitSnapshot) }
    return
}

$uri = "$($DcrEndpoint.GetLeftPart([UriPartial]::Authority))/dataCollectionRules/$DcrImmutableId/streams/Custom-MDCAI_EnrichmentV3_CL?api-version=2023-01-01"
$header = @{ Authorization = "Bearer $(Get-AzureToken 'https://monitor.azure.com')" }
$now = [DateTime]::UtcNow.ToString('o')
$sent = 0
try {
    for ($i = 0; $i -lt $count; $i += 250) {
        $end = [Math]::Min($i + 250, $count)
        $batch = for ($j = $i; $j -lt $end; $j++) {
            $r = $rows[$j]
            if ($r.Count -ne $required.Count) { throw "Esquema de fila inesperado en índice $j." }
            $obj = [ordered]@{TimeGenerated=$now}
            for ($k = 0; $k -lt $required.Count; $k++) { $obj[$required[$k]] = $r[$k] }
            $obj
        }
        $bytes = [Text.Encoding]::UTF8.GetBytes((ConvertTo-Json -InputObject @($batch) -Depth 4 -Compress))
        if ($bytes.Length -gt 900000) { throw 'Lote demasiado grande para el envío.' }
        $null = Invoke-RestMethod -Uri $uri -Method Post -Headers $header -MaximumRedirection 0 -ContentType 'application/json' -Body $bytes
        $sent += $end - $i
    }
} catch {
    throw "Envío incompleto; $sent de $count filas confirmadas. Reintentar puede repetir filas físicas; la consulta 13 deduplica por alerta y versión. $($_.Exception.Message)"
}
[pscustomobject]@{ Rows = $count; Uploaded = $sent; Preview = $false }

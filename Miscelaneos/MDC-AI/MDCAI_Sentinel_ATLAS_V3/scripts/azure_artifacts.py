from __future__ import annotations

import html
import json
import uuid
from pathlib import Path

INSIGHTS_API = "2025-09-01"
LOGS_API = "2025-07-01"
ARM_SCHEMA = "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#"
WDL_SCHEMA = "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#"
DATA_STREAM = "Custom-MDCAI_EnrichmentV3_CL"
SNAPSHOT_COLUMNS = [
    ("TimeGenerated", "datetime"), ("SourceAlertTime", "datetime"), ("AlertKey", "string"),
    ("AlertType", "string"), ("MappingVersion", "string"), ("Disposition", "string"),
    ("CandidateCAAT", "string"), ("CandidateATLAS", "string"), ("CandidateOWASP2025", "string"), ("CandidateOWASP2026", "string"),
]


def emit(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def template(params, resources, *, variables=None, outputs=None):
    doc = {"$schema": ARM_SCHEMA, "contentVersion": "3.0.0.0", "parameters": params, "resources": resources}
    if variables:
        doc["variables"] = variables
    if outputs:
        doc["outputs"] = outputs
    return doc


def plan_for_type(profile, relations, atlas_version):
    direct = [r for r in relations if r["Relation"] == "direct"]
    other_count = len(relations) - len(direct)
    tags = []
    sources = []
    for r in direct:
        fw, ver, tid = r["Framework"], r["FrameworkVersion"], r["TargetId"]
        if fw == "CAAT":
            tags.append(f"MDCAI:CAAT:{tid.removeprefix('CAAT-')}")
        elif fw == "ATLAS":
            tags.append(f"MDCAI:ATLAS:{tid}")
        elif fw == "OWASP-LLM" and ver == "2026":
            tags.append(f"MDCAI:OWASP:{ver}:{tid}")
        if fw != "OWASP-LLM" or ver == "2026":
            edition = f":{ver}" if fw == "OWASP-LLM" else ""
            sources.append(f'<a href="{html.escape(r["TargetUrl"], quote=True)}">{html.escape(tid + edition)}</a>')
    direct_summary = " · ".join(sources) if sources else "sin vínculo directo"
    line = (
        f'<div><a href="{html.escape(profile["LearnUrl"], quote=True)}">{html.escape(profile["AlertType"])}</a>'
        f' · {direct_summary}<br/>{html.escape(profile["Triage"])}'
        f'<br/>{html.escape(profile["EvidenceBoundary"])}'
        + (f"<br/>Vínculos no automáticos: {other_count}; consultar la matriz V3." if other_count else "")
        + "</div>"
    )
    return {"line": line, "tags": sorted(set(tags)), "scope": profile["SignalScope"], "atlasVersion": atlas_version}


def build_playbook(policy, atlas_version, profiles, candidate_rows):
    workspace = "[resourceId('Microsoft.OperationalInsights/workspaces', parameters('workspaceName'))]"
    connection = "[resourceId('Microsoft.Web/connections', variables('connectionName'))]"
    host = {"connection": {"name": "@parameters('$connections')['azuresentinel']['connectionId']"}}
    auth = {"type": "ManagedServiceIdentity", "audience": "@parameters('armAudience')"}
    release = policy["release"]
    comment_guid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:mdcai:sentinel:enrichment:{release}"))
    profile_lookup = {r["AlertType"]: plan_for_type(r, candidate_rows[r["AlertType"]], atlas_version) for r in profiles}
    if not all(len(x["line"]) < 1300 for x in profile_lookup.values()):
        raise ValueError("Revisar el límite de tamaño de las notas del playbook")
    secure_all = {"secureData": {"properties": ["inputs", "outputs"]}}

    def compose(inputs, after=None):
        return {"type": "Compose", "inputs": inputs, "runAfter": {after: ["Succeeded"]} if after else {}}

    def set_var(name, value, after=None):
        return {"type": "SetVariable", "inputs": {"name": name, "value": value}, "runAfter": {after: ["Succeeded"]} if after else {}}

    def init_var(name, kind, value, after):
        return {"type": "InitializeVariable", "runAfter": {after: ["Succeeded"]},
                "inputs": {"variables": [{"name": name, "type": kind, "value": value}]}}

    def append(name, value, after=None):
        return {"type": "AppendToArrayVariable", "inputs": {"name": name, "value": value}, "runAfter": {after: ["Succeeded"]} if after else {}}

    def condition(expr, yes, no=None, after=None):
        return {"type": "If", "expression": expr, "actions": yes, "else": {"actions": no or {}},
                "runAfter": {after: ["Succeeded"]} if after else {}}

    def http(method, uri, after=None, body=None, secure=False):
        obj = {"type": "Http", "inputs": {"method": method, "uri": uri, "authentication": auth},
               "runAfter": {after: ["Succeeded"]} if after else {}}
        if body is not None:
            obj["inputs"]["body"] = body
            obj["inputs"]["headers"] = {"Content-Type": "application/json"}
        if secure:
            obj["runtimeConfiguration"] = secure_all
        return obj

    actions = {
        "IncidentArmId": compose("@string(triggerBody()?['object']?['id'])"),
        "IncidentLeaf": compose("@last(split(outputs('IncidentArmId'), '/'))", "IncidentArmId"),
        "TrustedIncidentPath": compose("@concat(parameters('workspaceResourceId'), '/providers/Microsoft.SecurityInsights/incidents/', encodeUriComponent(outputs('IncidentLeaf')))", "IncidentLeaf"),
        "InitLines": init_var("Lines", "Array", [], "TrustedIncidentPath"),
        "InitTags": init_var("Tags", "Array", ["MDCAI:V3:Propuesto"], "InitLines"),
        "InitUnknown": init_var("Unknown", "Boolean", False, "InitTags"),
        "WorkspaceBoundary": condition(
            {"and": [
                {"equals": ["@toLower(outputs('TrustedIncidentPath'))", "@toLower(outputs('IncidentArmId'))"]},
                {"equals": ["@length(outputs('IncidentLeaf'))", 36]},
            ]},
            {"ListIncidentAlerts": http("POST", f"@concat(parameters('armBase'), outputs('TrustedIncidentPath'), '/alerts?api-version={INSIGHTS_API}')", secure=True),
             "FilterCandidates": {
                 "type": "Query", "runAfter": {"ListIncidentAlerts": ["Succeeded"]}, "runtimeConfiguration": secure_all,
                 "inputs": {"from": "@body('ListIncidentAlerts')?['value']",
                            "where": "@and(equals(toLower(string(item()?['kind'])), 'securityalert'), contains(parameters('productNamesLower'), toLower(string(item()?['properties']?['productName']))), or(startsWith(string(item()?['properties']?['alertType']), 'AI.Azure_'), and(parameters('includeModelScan'), startsWith(string(item()?['properties']?['alertType']), 'AI.AIModelScan_'))))"},
             },
             "SelectTypes": {
                 "type": "Select", "runAfter": {"FilterCandidates": ["Succeeded"]},
                 "inputs": {"from": "@body('FilterCandidates')", "select": {"typeId": "@item()?['properties']?['alertType']"}},
             },
             "ForEachType": {
                 "type": "Foreach", "runAfter": {"SelectTypes": ["Succeeded"]}, "operationOptions": "Sequential",
                 "foreach": "@sort(union(body('SelectTypes'), body('SelectTypes')), 'typeId')",
                 "actions": {
                     "KnownProfile": condition({"equals": ["@contains(parameters('profiles'), items('ForEachType')?['typeId'])", True]},
                         {"Profile": compose("@parameters('profiles')[items('ForEachType')?['typeId']]"),
                          "AppendLine": append("Lines", "@outputs('Profile')?['line']", "Profile"),
                          "ForEachTag": {
                              "type": "Foreach", "runAfter": {"AppendLine": ["Succeeded"]}, "operationOptions": "Sequential",
                              "foreach": "@outputs('Profile')?['tags']",
                              "actions": {"AppendTag": append("Tags", "@items('ForEachTag')")},
                          }}, {"MarkUnknown": set_var("Unknown", True)}),
                 },
             },
             "IfUnknown": condition({"equals": ["@variables('Unknown')", True]},
                 {"AppendUnknownNote": append("Lines", "<div>Hay alertas IA candidatas sin clasificación en esta versión. Consultar QA y el incidente original.</div>"),
                  "AppendReviewTag": append("Tags", "MDCAI:V3:Revisar", "AppendUnknownNote")}, after="ForEachType"),
             "TagObjects": {
                 "type": "Select", "runAfter": {"IfUnknown": ["Succeeded"]},
                 "inputs": {"from": "@union(variables('Tags'), variables('Tags'))", "select": {"Tag": "@item()"}},
             },
             "Plan": compose(
                 {"version": release, "atlasVersion": atlas_version, "distinctTypes": "@length(union(body('SelectTypes'), body('SelectTypes')))",
                  "remarks": "@variables('Lines')", "tags": "@body('TagObjects')"}, "TagObjects"),
             "ApplyOnlyWhenEnabled": condition(
                 {"and": [{"equals": ["@parameters('writeToIncident')", True]}, {"greater": ["@length(variables('Lines'))", 0]}]},
                 {"GetExistingComment": http("GET",
                      f"@concat(parameters('armBase'), outputs('TrustedIncidentPath'), '/comments/{comment_guid}?api-version={INSIGHTS_API}')"),
                  "NewComment": compose(
                      f"@concat('<div><b>MDCAI V{release} · clasificación propuesta · ATLAS {atlas_version}</b><br/>No modifica la alerta ni prueba éxito o cobertura.</div>', join(variables('Lines'), ''))"),
                  "WriteIfChanged": {
                      "type": "If",
                      "expression": {"or": [
                          {"equals": ["@outputs('GetExistingComment')?['statusCode']", 404]},
                          {"and": [
                              {"equals": ["@outputs('GetExistingComment')?['statusCode']", 200]},
                              {"not": {"equals": ["@body('GetExistingComment')?['properties']?['message']", "@outputs('NewComment')"]}},
                          ]},
                      ]},
                      "actions": {"UpsertComment": http("PUT",
                          f"@concat(parameters('armBase'), outputs('TrustedIncidentPath'), '/comments/{comment_guid}?api-version={INSIGHTS_API}')",
                          body={"properties": {"message": "@outputs('NewComment')"}})},
                      "else": {"actions": {}},
                      "runAfter": {"GetExistingComment": ["Succeeded", "Failed"], "NewComment": ["Succeeded"]},
                  },
                  "CheckCommentReadStatus": condition({"or": [
                      {"equals": ["@outputs('GetExistingComment')?['statusCode']", 200]},
                      {"equals": ["@outputs('GetExistingComment')?['statusCode']", 404]},
                  ]}, {"AddTags": {
                          "type": "ApiConnection", "runAfter": {},
                          "inputs": {"host": host, "method": "put", "path": "/Incidents/Tags",
                                     "body": {"incidentArmId": "@outputs('TrustedIncidentPath')", "tagsToAdd": {"TagsToAdd": "@body('TagObjects')"}}},
                          }}, {"CommentReadFailed": {"type": "Terminate", "runAfter": {},
                                                   "inputs": {"runStatus": "Failed", "runError": {"code": "CommentRead", "message": "No se pudo leer el comentario. Revisar la respuesta y RBAC."}}}},
                      after="WriteIfChanged"),
                  },
                 after="Plan"),
             },
            {"RejectWorkspace": {"type": "Terminate", "runAfter": {},
                                 "inputs": {"runStatus": "Failed", "runError": {"code": "WrongWorkspace", "message": "El incidente no pertenece al workspace parametrizado."}}}},
            after="InitUnknown"),
    }
    return template(
        {"workspaceName": {"type": "string"}, "playbookName": {"type": "string", "defaultValue": "Enrich-MDCAI-ATLAS-v3"},
         "location": {"type": "string", "defaultValue": "[resourceGroup().location]"},
         "workflowState": {"type": "string", "defaultValue": "Disabled", "allowedValues": ["Disabled", "Enabled"]},
         "writeToIncident": {"type": "bool", "defaultValue": False}, "includeModelScan": {"type": "bool", "defaultValue": False}},
        [
            {"type": "Microsoft.Web/connections", "apiVersion": "2016-06-01", "name": "[variables('connectionName')]",
             "location": "[parameters('location')]",
             "properties": {"displayName": "[variables('connectionName')]", "parameterValueType": "Alternative",
                            "customParameterValues": {}, "api": {"id": "[variables('connectorId')]"}}},
            {"type": "Microsoft.Logic/workflows", "apiVersion": "2019-05-01", "name": "[parameters('playbookName')]",
             "location": "[parameters('location')]", "identity": {"type": "SystemAssigned"}, "dependsOn": [connection],
             "properties": {"state": "[parameters('workflowState')]",
                 "definition": {"$schema": WDL_SCHEMA, "contentVersion": "1.0.0.0",
                                "parameters": {"$connections": {"type": "Object"}, "profiles": {"type": "Object"},
                                               "workspaceResourceId": {"type": "String"}, "armBase": {"type": "String"},
                                               "armAudience": {"type": "String"}, "productNamesLower": {"type": "Array"},
                                               "writeToIncident": {"type": "Bool"}, "includeModelScan": {"type": "Bool"}},
                                "triggers": {"Microsoft_Sentinel_incident": {
                                    "type": "ApiConnectionWebhook",
                                    "inputs": {"host": host, "path": "/incident-creation", "body": {"callback_url": "@{listCallbackUrl()}"}},
                                    "runtimeConfiguration": {"concurrency": {"runs": 1}, "secureData": {"properties": ["inputs", "outputs"]}},
                                }},
                                "actions": actions, "outputs": {}},
                 "parameters": {"$connections": {"value": {"azuresentinel": {
                                      "id": "[variables('connectorId')]", "connectionId": connection, "connectionName": "[variables('connectionName')]",
                                      "connectionProperties": {"authentication": {"type": "ManagedServiceIdentity"}}}}},
                                "workspaceResourceId": {"value": workspace},
                                "armBase": {"value": "[if(endsWith(environment().resourceManager, '/'), substring(environment().resourceManager, 0, sub(length(environment().resourceManager), 1)), environment().resourceManager)]"},
                                "armAudience": {"value": "[environment().resourceManager]"},
                                "profiles": {"value": profile_lookup},
                                "productNamesLower": {"value": [n.lower() for n in policy["product_names"]]},
                                "writeToIncident": {"value": "[parameters('writeToIncident')]"},
                                "includeModelScan": {"value": "[parameters('includeModelScan')]"},
                                }}},
        ],
        variables={"connectionName": "[concat(parameters('playbookName'), '-sentinel-mi')]",
                   "connectorId": "[subscriptionResourceId('Microsoft.Web/locations/managedApis', parameters('location'), 'azuresentinel')]"},
        outputs={"logicAppResourceId": {"type": "string", "value": "[resourceId('Microsoft.Logic/workflows', parameters('playbookName'))]"},
                 "proposedMappingVersion": {"type": "string", "value": release}},
    )


def build_workbook(read_query, release):
    def query(title, text, span=43200, visualization="table"):
        return {"type": 3, "name": title, "content": {
            "version": "KqlItem/1.0", "query": text, "title": title, "size": 0, "timeContext": {"durationMs": span * 60000},
            "queryType": 0, "resourceType": "microsoft.operationalinsights/workspaces", "visualization": visualization,
        }}

    def markdown(text, name):
        return {"type": 1, "name": name, "content": {"json": text}}

    return {
        "version": "Notebook/1.0",
        "items": [
            markdown(f"# Defender for Cloud AI Services · Sentinel · V{release}\n"
                     "**Actividad observada y clasificación propuesta.** No es una medición de cobertura ni una atribución validada. "
                     "Los conteos por técnica, escenario o riesgo no se suman entre categorías.", "intro"),
            query("Alertas distintas por clase y ámbito · 30 días",
                  "MDCAI_V3_Enriched(30d)\n| summarize Alertas=count() by SignalScope, Disposition\n| order by Alertas desc"),
            query("14 escenarios CAAT · actividad y vínculo documentado", "MDCAI_V3_Escenarios(30d)"),
            query("ATLAS · técnicas vinculadas directamente", read_query("04_Actividad_ATLAS.kql")),
            query("OWASP · separar las dos ediciones", read_query("05_Actividad_OWASP.kql")),
            query("Triage · alertas originales, sin contenido de prompts", "MDCAI_V3_Enriched(7d)\n"
                  "| project TimeGenerated, AlertType, AlertSeverity, AlertStatus, Disposition, DirectCAAT, DirectATLAS, DirectOWASP2026, Triage, EvidenceBoundary, AlertLink\n"
                  "| top 100 by TimeGenerated desc", span=10080),
            query("QA · alertas observadas sin clasificar", read_query("06_QA_casos_sin_clasificar.kql")),
            query("QA · duplicados y consistencia de versiones", read_query("15_QA_watchlists.kql")),
        ],
        "fallbackResourceIds": ["__MDCAI_WORKSPACE_ID__"],
        "$schema": "https://github.com/Microsoft/Application-Insights-Workbooks/blob/master/schema/workbook.json",
    }


def build(root: Path, ref: dict, policy: dict, model: dict, watchlists: dict):
    def read_query(name):
        return (root / "kql" / name).read_text(encoding="utf-8-sig").strip()

    workspace_id = "resourceId('Microsoft.OperationalInsights/workspaces', parameters('workspaceName'))"
    workspace_param = {"workspaceName": {"type": "string"}}
    resources = []
    for alias, (key, raw) in watchlists.items():
        resources.append({
            "type": "Microsoft.OperationalInsights/workspaces/providers/watchlists",
            "apiVersion": INSIGHTS_API, "name": f"[concat(parameters('workspaceName'), '/Microsoft.SecurityInsights/{alias}')]",
            "properties": {"displayName": alias, "description": "MDCAI v3; managed by versioned package.",
                           "provider": "MDCAI-V3", "source": f"{alias}.csv", "sourceType": "Local",
                           "itemsSearchKey": key, "contentType": "text/csv", "rawContent": raw},
        })
    for query_file, alias, depends in [
        ("01_MDCAI_V3_Base.kql", "MDCAI_V3_Base", []),
        ("02_MDCAI_V3_Enriched.kql", "MDCAI_V3_Enriched", ["MDCAI_V3_Base"]),
        ("03_MDCAI_V3_Escenarios.kql", "MDCAI_V3_Escenarios", ["MDCAI_V3_Enriched"]),
    ]:
        resources.append({
            "type": "Microsoft.OperationalInsights/workspaces/savedSearches", "apiVersion": LOGS_API,
            "name": f"[concat(parameters('workspaceName'), '/{alias}')]",
            "dependsOn": [f"[resourceId('Microsoft.OperationalInsights/workspaces/savedSearches', parameters('workspaceName'), '{d}')]" for d in depends],
            "etag": "*", "properties": {"category": "MDCAI-V3", "displayName": alias, "functionAlias": alias,
                                        "functionParameters": "Lookback:timespan", "query": read_query(query_file), "version": 2},
        })
    workbook = build_workbook(read_query, policy["release"])
    standalone = {**workbook, "fallbackResourceIds": []}
    emit(root / "workbook" / "MDCAI_V3_Workbook.json", standalone)
    resources.append({
        "type": "Microsoft.Insights/workbooks", "apiVersion": "2022-04-01",
        "name": f"[guid({workspace_id}, 'mdcai-v3-workbook')]", "location": "[parameters('workbookLocation')]", "kind": "shared",
        "properties": {"displayName": "MDC-AI v3 · CAAT + ATLAS + OWASP", "category": "sentinel",
                       "sourceId": f"[{workspace_id}]",
                       "serializedData": f"[replace(string(variables('workbook')), '__MDCAI_WORKSPACE_ID__', {workspace_id})]"},
    })
    deploy = root / "deploy"
    emit(deploy / "01_Core.arm.json",
         template({**workspace_param, "workbookLocation": {"type": "string", "defaultValue": "[resourceGroup().location]"}},
                  resources, variables={"workbook": workbook}))
    emit(deploy / "02_Playbook.arm.json", build_playbook(policy, ref["atlas"]["version"], model["profiles"], model["candidates"]))
    emit(deploy / "03_Resumen_Diario.arm.json", template(
        {**workspace_param, "firstBinStartUtc": {"type": "string", "metadata": {"description": "Medianoche UTC vigente o siguiente, ISO 8601."}},
         "binDelayMinutes": {"type": "int", "defaultValue": 60, "minValue": 0, "maxValue": 1440}},
        [{"type": "Microsoft.OperationalInsights/workspaces/summaryLogs", "apiVersion": LOGS_API,
          "name": "[concat(parameters('workspaceName'), '/MDCAI-V3-Daily-Source')]",
          "properties": {"ruleType": "User", "description": "MDCAI V3 - volumen diario por AlertType; no cubre taxonomías.",
                         "ruleDefinition": {"query": read_query("10_Resumen_diario_origen.kql"), "binSize": 1440,
                                            "binStartTime": "[parameters('firstBinStartUtc')]", "binDelay": "[parameters('binDelayMinutes')]",
                                            "destinationTable": "MDCAI_V3_Daily_CL", "displayName": "MDCAI V3 diario por tipo de alerta"}}}],
    ))
    cols = [{"name": name, "type": typ} for name, typ in SNAPSHOT_COLUMNS]
    emit(deploy / "04_Historial_DCR.arm.json", template(
        {**workspace_param, "location": {"type": "string", "metadata": {"description": "Región del workspace (no del grupo de recursos)."}},
         "dcrName": {"type": "string", "defaultValue": "dcr-mdcai-v3-history"}},
        [{"type": "Microsoft.OperationalInsights/workspaces/tables", "apiVersion": LOGS_API,
          "name": "[concat(parameters('workspaceName'), '/MDCAI_EnrichmentV3_CL')]",
          "properties": {"plan": "Analytics", "retentionInDays": 90, "schema": {"name": "MDCAI_EnrichmentV3_CL", "columns": cols}}},
         {"type": "Microsoft.Insights/dataCollectionRules", "apiVersion": "2023-03-11", "kind": "Direct",
          "name": "[parameters('dcrName')]", "location": "[parameters('location')]",
          "dependsOn": ["[resourceId('Microsoft.OperationalInsights/workspaces/tables', parameters('workspaceName'), 'MDCAI_EnrichmentV3_CL')]"],
          "properties": {"streamDeclarations": {DATA_STREAM: {"columns": cols}},
                         "destinations": {"logAnalytics": [{"workspaceResourceId": f"[{workspace_id}]", "name": "mdcaiHistory"}]},
                         "dataFlows": [{"streams": [DATA_STREAM], "destinations": ["mdcaiHistory"], "transformKql": "source", "outputStream": DATA_STREAM}]}}],
        outputs={"dataCollectionRuleResourceId": {"type": "string", "value": "[resourceId('Microsoft.Insights/dataCollectionRules', parameters('dcrName'))]"}},
    ))

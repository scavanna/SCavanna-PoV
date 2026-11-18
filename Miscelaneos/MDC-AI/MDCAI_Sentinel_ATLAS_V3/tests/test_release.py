import csv
import io
import json
import sys
import unittest
import uuid
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import azure_artifacts as aa
import build_release as br
import export_navigator as nav


class ReleaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ref = br.load_json(ROOT / "data" / "reference.json")
        cls.policy = br.load_json(ROOT / "data" / "policy.json")
        cls.model = br.build_model(cls.ref, cls.policy)
        cls.profiles = br.unique_index(cls.model["profiles"], "AlertType")

    def arm(self, name):
        return br.load_json(ROOT / "deploy" / name)

    def test_exact_alert_inventory_and_status(self):
        r = self.profiles
        self.assertEqual(len([v for v in r.values() if v["SignalScope"] == "runtime"]), 16)
        self.assertEqual(len([v for v in r.values() if v["SignalScope"] == "model_scanning"]), 1)
        self.assertEqual("High", r["AI.Azure_ASCIISmuggling"]["DocumentedSeverity"])
        self.assertIn("Reconnaissance", r["AI.Azure_AccessAnomaly"]["DocumentedAttack"])
        self.assertEqual("preview", r["AI.Azure_LLMReconnaissance"]["ReleaseStatus"])
        self.assertEqual("preview", r["AI.AIModelScan_MalwareDetected"]["ReleaseStatus"])
        self.assertNotIn("AI.Azure_PhishingContentInModelResponse", r)
        self.assertNotIn("AI.Azure_DataLeakInModelResponse.Sensitive", r)
        self.assertNotIn("AI.Azure_Anomaly", r)
        for suffix in ["ModelResponse", "UnknownSource", "UserPrompt"]:
            self.assertIn("AI.Azure_MaliciousUrl." + suffix, r)

    def test_no_inheritance_and_no_retired_ids_in_operational_relations(self):
        r = self.profiles
        self.assertEqual("LLM01", r["AI.Azure_Jailbreak.ContentFiltering.BlockedAttempt"]["AutoOWASP2025"])
        self.assertEqual("CAAT-02", r["AI.Azure_Jailbreak.ContentFiltering.BlockedAttempt"]["AutoCAAT"])
        self.assertEqual("", r["AI.Azure_CredentialTheftAttempt"]["AutoATLAS"])
        self.assertEqual("", r["AI.Azure_DOWDuplicateRequests"]["AutoATLAS"])
        self.assertEqual("LLM06", r["AI.Azure_DOWVolumeAnomaly"]["AutoOWASP2026"])
        self.assertEqual("conditional", r["AI.Azure_AnomalousToolInvocation"]["Disposition"])
        for x in self.model["relations"]:
            self.assertNotIn(x["TargetId"], self.ref["atlas"]["migrations"])

    def test_caat_source_edition_and_canonical_resolution(self):
        c = br.unique_index(self.model["caat"], "CAAT_Id")
        self.assertEqual(len(c), 14)
        self.assertEqual(set(c["CAAT-02"]["Learn_OWASP"].split(";")), {"LLM01", "LLM02", "LLM03"})
        self.assertTrue(c["CAAT-05"]["LearnUrl"].endswith("/unbounded-ai-consumption-and-agentic-dos"))
        self.assertTrue(c["CAAT-12"]["LearnUrl"].endswith("/unmanaged-agent-sprawl"))
        self.assertIn("AML.T0057", c["CAAT-02"]["Learn_ATLAS"])
        self.assertIn(("AML.T0057", "AML.T0085.002"), [(x["SourceId"], x["CanonicalId"]) for x in self.model["caat_links"]])
        self.assertEqual(len(self.ref["atlas"]["tactics"]), 16)
        self.assertEqual(len(self.ref["atlas"]["techniques"]), 221)
        self.assertEqual(self.ref["owasp"]["2026"]["LLM03"]["name"], "Excessive Agency")

    def test_release_outputs_match_model_and_no_raw_prompt_scope(self):
        core = self.arm("01_Core.arm.json")
        payloads = {x["properties"]["displayName"]: x["properties"]["rawContent"] for x in core["resources"] if x["type"].endswith("/watchlists")}
        self.assertEqual(len(payloads), 4)
        for alias, name in [(br.PROFILE_ALIAS, "profiles"), (br.RELATION_ALIAS, "relations"),
                            (br.SCENARIO_ALIAS, "caat"), (br.ATLAS_ALIAS, "atlas")]:
            with (ROOT / "watchlists" / f"{alias}.csv").open(newline="", encoding="utf-8-sig") as f:
                rows = list(csv.DictReader(f, strict=True))
            self.assertEqual(rows, self.model[name])
            self.assertEqual(rows, list(csv.DictReader(io.StringIO(payloads[alias], newline=""), strict=True)))
        self.assertEqual(len([r for r in core["resources"] if r["type"].endswith("savedSearches")]), 3)
        baseline = (ROOT / "kql" / "01_MDCAI_V3_Base.kql").read_text(encoding="utf-8")
        self.assertNotIn("ExtendedProperties", baseline)
        self.assertIn("by AlertKey", baseline)
        for k in (ROOT / "kql").glob("*.kql"):
            self.assertNotRegex(k.read_text(encoding="utf-8"), r"__[A-Z_]+__", str(k))
        workbook = br.load_json(ROOT / "workbook" / "MDCAI_V3_Workbook.json")
        self.assertEqual(sum(row["type"] == 3 for row in workbook["items"]), 7)
        self.assertTrue(any("MDCAI_V3_Escenarios(30d)" in row["content"].get("query", "") for row in workbook["items"]))

    def test_workflow_safe_defaults_and_controlled_writes(self):
        a = self.arm("02_Playbook.arm.json")
        self.assertFalse(a["parameters"]["writeToIncident"]["defaultValue"])
        self.assertFalse(a["parameters"]["includeModelScan"]["defaultValue"])
        self.assertEqual("Disabled", a["parameters"]["workflowState"]["defaultValue"])
        workflow = next(x for x in a["resources"] if x["type"] == "Microsoft.Logic/workflows")
        self.assertEqual(workflow["identity"]["type"], "SystemAssigned")
        d = workflow["properties"]["definition"]
        initializers = [x for x in d["actions"].values() if x["type"] == "InitializeVariable"]
        self.assertEqual([[v["type"] for v in x["inputs"]["variables"]] for x in initializers], [["Array"], ["Array"], ["Boolean"]])
        allowed = d["actions"]["WorkspaceBoundary"]["actions"]["ApplyOnlyWhenEnabled"]
        self.assertEqual(allowed["expression"]["and"][0], {"equals": ["@parameters('writeToIncident')", True]})
        items = allowed["actions"]
        read_uri = items["GetExistingComment"]["inputs"]["uri"]
        write_uri = items["WriteIfChanged"]["actions"]["UpsertComment"]["inputs"]["uri"]
        filename_key = uuid.uuid5(uuid.NAMESPACE_URL, f"urn:mdcai:sentinel:enrichment:{self.policy['release']}")
        self.assertIn(str(filename_key), read_uri)
        self.assertEqual(read_uri, write_uri)
        self.assertEqual(items["CheckCommentReadStatus"]["actions"]["AddTags"]["inputs"]["path"], "/Incidents/Tags")
        p = workflow["properties"]["parameters"]["profiles"]["value"]
        self.assertEqual(len(p), len(self.profiles))
        self.assertIn("MDCAI:ATLAS:AML.T0054", p["AI.Azure_Jailbreak.ContentFiltering.BlockedAttempt"]["tags"])
        self.assertNotIn("MDCAI:ATLAS:AML.T0024", p["AI.Azure_CredentialTheftAttempt"]["tags"])
        self.assertFalse(p["AI.Azure_AnomalousToolInvocation"]["tags"])
        text = json.dumps(a)
        self.assertNotIn("ExtendedProperties", text)
        self.assertNotIn("teams.microsoft.com", text)

    def test_aggregate_and_historical_schema_are_independent(self):
        a = self.arm("03_Resumen_Diario.arm.json")["resources"][0]["properties"]["ruleDefinition"]
        self.assertEqual(a["binSize"], 1440)
        for bad in ["_GetWatchlist", "MDCAI_V3_Enriched", "mv-expand", "ago(", "now("]:
            self.assertNotIn(bad, "\n".join(line for line in a["query"].splitlines() if not line.startswith("//")))
        hist = self.arm("04_Historial_DCR.arm.json")["resources"]
        self.assertEqual(hist[0]["properties"]["schema"]["columns"], hist[1]["properties"]["streamDeclarations"][aa.DATA_STREAM]["columns"])
        projection = (ROOT / "kql" / "14_Capturar_clasificacion.kql").read_text(encoding="utf-8")
        for k, _ in aa.SNAPSHOT_COLUMNS[1:]:
            self.assertIn(k, projection)

    def test_navigator_layer_rejects_stale_or_repeated_ids(self):
        sample = {"TechniqueId": "AML.T0054", "Alerts": "2"}
        good = nav.build_layer([sample], self.ref, self.policy["release"])
        self.assertEqual(good["domain"], self.ref["navigator"]["domain"])
        self.assertEqual(good["techniques"][0]["score"], 2)
        for rows in [[sample, sample], [{"TechniqueId": "AML.T0057", "Alerts": "1"}], [{"TechniqueId": "AML.T0054", "Alerts": "-1"}]]:
            with self.assertRaises(ValueError):
                nav.build_layer(rows, self.ref, self.policy["release"])

    def test_excel_complete_static_and_editable_pilot(self):
        wb = load_workbook(ROOT / "MDC_AI_ATLAS_OWASP_Mapping_v3.xlsx", data_only=False)
        try:
            self.assertEqual(wb["Catálogo alertas"].max_row, len(self.profiles) + 1)
            self.assertEqual(wb["Alerta x marco"].max_row, len(self.model["relations"]) + 1)
            self.assertEqual(wb["Escenarios CAAT"].max_row, 15)
            self.assertTrue(wb["Piloto"].data_validations.dataValidation)
            self.assertFalse(any(c.data_type in {"f", "e"} for s in wb for row in s for c in row))
        finally:
            wb.close()


if __name__ == "__main__":
    unittest.main()

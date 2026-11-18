"""Rebuild data/reference.json from public sources; --check compares without writing."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import yaml


AS_OF = "2026-11-18"
LEARN = "https://learn.microsoft.com/en-us/"
ALERTS = LEARN + "azure/defender-for-cloud/alerts-ai-workloads"
CAAT_ROOT = LEARN + "security/zero-trust/catalog-ai-attack-techniques/"
CAAT_INDEX = CAAT_ROOT + "catalog-ai-attack-techniques"
CAAT_AUTHOR = "https://github.com/richarddiver-ms"
ATLAS_VERSION = "2026.10"
ATLAS_TAG = f"v{ATLAS_VERSION}"
ATLAS_RAW = "https://raw.githubusercontent.com/mitre-atlas/atlas-data/"
ATLAS_DATA = f"{ATLAS_RAW}{ATLAS_TAG}/dist/v6/ATLAS-{ATLAS_VERSION}.yaml"
ATLAS_RELEASES = "https://github.com/mitre-atlas/atlas-data/releases/"
ATLAS_2026_07 = f"{ATLAS_RAW}v2026.07/dist/v6/ATLAS-2026.07.yaml"
NAVIGATOR_MATRIX = f"{ATLAS_RELEASES}download/{ATLAS_TAG}/navigator-atlas_layer_matrix.json"
NAVIGATOR_EXAMPLE = (
    "https://raw.githubusercontent.com/mitre-atlas/atlas-navigator-data/main/"
    "dist/case-study-navigator-layers/AML.CS0000.json"
)
OWASP_2025 = "https://genai.owasp.org/llm-top-10/"
OWASP_REPO = "GenAI-Security-Project/GenAI-LLM-Top10"
OWASP_2026 = f"https://github.com/{OWASP_REPO}/tree/main/2026/final"
OWASP_2026_BLOB = f"https://github.com/{OWASP_REPO}/blob/main/2026/"
OWASP_2026_RAW = f"https://raw.githubusercontent.com/{OWASP_REPO}/main/2026/"
LLM_IDS = {f"LLM{number:02d}" for number in range(1, 11)}
MODEL_SCAN = "AI.AIModelScan_MalwareDetected"
INFRASTRUCTURE_HEADING = "exposed-kubernetes-service-detected-ai-applications-on-kubernetes"
MIGRATIONS = {
    "AML.T0024.000": "AML.T0137.000",
    "AML.T0024.001": "AML.T0137.002",
    "AML.T0056": "AML.T0085.003",
    "AML.T0057": "AML.T0085.002",
    # July's notes identify Models by name but repeat the Datasets URL;
    # both the July and October tagged YAML put Models at .001.
    "AML.T0058": "AML.T0115.001",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_url(url):
    request = Request(url, headers={"User-Agent": "AF-MDCAI-reference-refresh/3"})
    for attempt in range(2):
        try:
            with urlopen(request, timeout=20) as response:
                return response.read()
        except (URLError, TimeoutError) as error:
            if attempt or (
                isinstance(error, HTTPError) and error.code < 500 and error.code not in (408, 429)
            ):
                raise


def read_html(url):
    return BeautifulSoup(read_url(url), "html.parser")


def text(node):
    return node.get_text(" ", strip=True)


def section(heading):
    for node in heading.next_siblings:
        if node.name in ("h2", "h3"):
            break
        if node.name:
            yield node


def alerts():
    catalog, infrastructure = [], []
    for heading in read_html(ALERTS).find_all(["h2", "h3"], id=True):
        anchor = heading["id"]
        paragraphs = [text(node) for node in section(heading) if node.name == "p"]
        ids = [
            match[1] for paragraph in paragraphs
            if (match := re.fullmatch(r"\((AI\.(?:Azure_[\w.]+|AIModelScan_MalwareDetected))\)", paragraph))
        ]
        if not ids and anchor != INFRASTRUCTURE_HEADING:
            continue
        fields = {}
        for paragraph in paragraphs:
            name, separator, value = paragraph.partition(":")
            if separator and name.strip() in ("Severity", "MITRE tactics"):
                fields[name.strip()] = value.strip()
        severity = fields["Severity"]
        label = text(heading)
        link = f"{ALERTS}#{anchor}"
        if anchor == INFRASTRUCTURE_HEADING:
            require(not ids and severity == "Medium", "Exposed Kubernetes alert metadata changed")
            infrastructure.append(dict(label=label, anchor=link, scope="containers", severity=severity))
            continue
        require(len(ids) == 1, f"Multiple alert IDs for {anchor}")
        model_scanning = ids[0] == MODEL_SCAN
        catalog.append(dict(
            alert_type=ids[0],
            label=label,
            anchor=link,
            severity=severity,
            attack_tactics=[t.strip() for t in fields.get("MITRE tactics", "").split(",") if t.strip()],
            status="preview" if re.search(r"\bpreview\b", label, re.I) else "documented",
            scope="model_scanning" if model_scanning else "runtime",
        ))
    unique_ids = {row["alert_type"] for row in catalog}
    require(len(catalog) == len(unique_ids) == 17 and MODEL_SCAN in unique_ids, "Expected 17 unique alerts")
    require(len(infrastructure) == 1, "Expected one Kubernetes alert without an ID")
    require(all(row["attack_tactics"] for row in catalog if row["scope"] == "runtime"), "Missing runtime tactics")
    return catalog, infrastructure


def unique(values):
    return list(dict.fromkeys(values))


def caat_scenario(item):
    number, url = item
    page = read_html(url)
    title = re.fullmatch(r"(\d+)\.\s+(.+)", text(page.h1))
    require(title is not None and int(title[1]) == number, f"Scenario numbering changed: {url}")
    handle = page.find("meta", attrs={"name": "author"})["content"]
    require(handle == "richarddiver-ms", f"Scenario author changed: {url}")
    # ms.date is the article's source date, not the site's deployment timestamp.
    source_date = date.fromisoformat(page.find("meta", attrs={"name": "ms.date"})["content"][:10])
    require(source_date.isoformat() <= AS_OF, f"Scenario postdates the snapshot: {url}")
    owasp_mapping = " ".join(
        text(node) for node in section(page.find(["h2", "h3"], id="owasp-top-10-mapping"))
    )
    require("2025" in owasp_mapping, f"Scenario does not cite OWASP 2025: {url}")
    owasp_ids = unique(re.findall(r"\bLLM\d{2}\b", owasp_mapping))
    atlas_ids, mitigation_ids = [], []
    for node in section(page.find(["h2", "h3"], id="mitre-atlas-mapping")):
        for entry in node.find_all("li"):
            label = text(entry)
            base = None
            for match in re.finditer(r"\b(AML\.T\d{4})(\.\d{3})?\b|(?<![\w.])(\.\d{3})\b", label):
                if match[1]:
                    base = match[1]
                    atlas_ids.append(match[0])
                else:
                    require(base is not None, f"Orphaned subtechnique shorthand: {url}")
                    atlas_ids.append(base + match[3])
            mitigation_ids.extend(re.findall(r"\bAML\.M\d{4}\b", label))
    require(owasp_ids and set(owasp_ids) <= LLM_IDS and atlas_ids and mitigation_ids, f"Incomplete mapping: {url}")
    return dict(
        id=f"CAAT-{number:02d}", label=title[2], url=url, author="Richard Diver",
        source_date=source_date.isoformat(), owasp_edition="2025", owasp_ids=owasp_ids,
        atlas_ids=unique(atlas_ids), mitigation_ids=unique(mitigation_ids),
    )


def caat():
    index = read_html(CAAT_INDEX)
    heading = index.find(["h2", "h3"], id="attack-scenarios")
    listing = next(node for node in section(heading) if node.name in ("ul", "ol"))
    scenarios = []
    for anchor in listing.find_all("a", href=True):
        number = int(re.match(r"(\d+)\.\s", text(anchor))[1])
        url = urljoin(CAAT_INDEX, anchor["href"])
        require(re.fullmatch(re.escape(CAAT_ROOT) + r"[a-z0-9-]+", url), f"Unexpected scenario URL: {url}")
        scenarios.append((number, url))
    require([number for number, _ in scenarios] == list(range(1, 15)), "Expected 14 CAAT scenarios")
    with ThreadPoolExecutor(max_workers=8) as executor:
        return list(executor.map(caat_scenario, scenarios))


def atlas():
    data = yaml.safe_load(read_url(ATLAS_DATA))
    require(data["collection"]["version"] == ATLAS_VERSION, "Unexpected ATLAS content version")
    tactics = {key: record["name"] for key, record in sorted(data["tactics"].items())}
    techniques = {}
    for key, record in sorted(data["techniques"].items()):
        achieves = data["relationships"][key]["achieves"]
        targets = unique(rel["target"] for rel in achieves)
        require(
            targets and set(targets) <= tactics.keys()
            and all(rel["source"] == key and rel["relationship-type"] == "achieves" for rel in achieves),
            f"Invalid tactic relationships for {key}",
        )
        techniques[key] = dict(name=record["name"], tactics=targets, url=f"https://atlas.mitre.org/techniques/{key}")
    require(len(tactics) == 16 and len(techniques) == 221, "Unexpected ATLAS vocabulary size")
    require(not MIGRATIONS.keys() & techniques.keys() and set(MIGRATIONS.values()) <= techniques.keys(),
            "ATLAS redirects do not agree with the pinned vocabulary")
    return dict(version=ATLAS_VERSION, tag=ATLAS_TAG, source=ATLAS_DATA,
                tactics=tactics, techniques=techniques, migrations=MIGRATIONS)


def owasp():
    edition_2025 = {}
    for link in read_html(OWASP_2025).find_all("a", href=True):
        match = re.fullmatch(r"(LLM\d{2}):2025\s+(.+)", text(link))
        if match and "/llmrisk/" in link["href"]:
            url = urljoin(OWASP_2025, link["href"])
            require(url.startswith("https://genai.owasp.org/llmrisk/"), f"Unexpected OWASP category URL: {url}")
            edition_2025[match[1]] = dict(name=match[2], url=url)
    readme = read_url(OWASP_2026_RAW + "README.md").decode("utf-8-sig")
    edition_2026 = {
        key: dict(name=name, url=OWASP_2026_BLOB + path)
        for key, name, path in re.findall(
            r"(?m)^\|[ \t]*(LLM\d{2}):2026[ \t]+([^|\n]+?)[ \t]*\|[ \t]*"
            r"\[`[^`\n]+`\]\(\./(final/\1_\w+\.md)\)[ \t]*\|", readme,
        )
    }
    require(edition_2025.keys() == edition_2026.keys() == LLM_IDS, "Expected LLM01–LLM10 in both OWASP editions")
    return {"2025": dict(sorted(edition_2025.items())), "2026": dict(sorted(edition_2026.items()))}


def navigator(technique_ids):
    for source in (NAVIGATOR_MATRIX, NAVIGATOR_EXAMPLE):
        try:
            layer = json.loads(read_url(source))
            require(layer["domain"] == "atlas-atlas", "Unexpected Navigator domain")
            versions = layer["versions"]
            require({"layer", "navigator"} <= versions.keys()
                    and all(isinstance(value, str) and value for value in versions.values()),
                    "Invalid Navigator versions")
            if source == NAVIGATOR_MATRIX:
                require({row["techniqueID"] for row in layer["techniques"]} == technique_ids,
                        "Pinned Navigator matrix does not match the pinned vocabulary")
            return dict(domain=layer["domain"], versions=versions, source=source)
        except (OSError, ValueError, KeyError, TypeError):
            if source == NAVIGATOR_EXAMPLE:
                raise


def build_reference():
    catalog, infrastructure = alerts()
    scenarios = caat()
    vocabulary = atlas()
    editions = owasp()
    layer = navigator(vocabulary["techniques"].keys())
    return dict(
        as_of=AS_OF,
        sources={
            "microsoft_alerts": ALERTS, "microsoft_caat": CAAT_INDEX, "microsoft_caat_author": CAAT_AUTHOR,
            "atlas_data": ATLAS_DATA, "atlas_release": f"{ATLAS_RELEASES}tag/{ATLAS_TAG}",
            "atlas_2026_07_release": f"{ATLAS_RELEASES}tag/v2026.07", "atlas_2026_07_data": ATLAS_2026_07,
            "owasp_2025": OWASP_2025, "owasp_2026": OWASP_2026,
            "owasp_2026_index": OWASP_2026_BLOB + "README.md", "navigator": layer["source"],
        },
        catalog=catalog, infrastructure=infrastructure, caat=scenarios, atlas=vocabulary, owasp=editions,
        navigator=layer,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the current public inputs differ from the snapshot")
    args = parser.parse_args()
    snapshot = build_reference()
    payload = (json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    output = Path(os.path.relpath(Path(__file__).resolve().parents[1] / "data" / "reference.json"))
    if args.check:
        if not output.is_file() or output.read_bytes() != payload:
            parser.exit(1, "data/reference.json does not match the current public inputs\n")
    else:
        output.parent.mkdir(exist_ok=True)
        output.write_bytes(payload)
    print(f"{'Verified' if args.check else 'Wrote'} {output} (Navigator: {snapshot['navigator']['source']})")


if __name__ == "__main__":
    main()

import hashlib
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIRS = ("data", "deploy", "docs", "kql", "scripts", "src", "tests", "uso-interno", "watchlists", "workbook")
PACKAGE_FILES = ("README.md", "requirements.txt", "MDC_AI_ATLAS_OWASP_Mapping_v3.xlsx")
PACKAGE_SUFFIXES = {".csv", ".in", ".json", ".kql", ".md", ".ps1", ".py", ".txt"}


def files():
    selected = [ROOT / s for s in PACKAGE_FILES]
    for folder in PACKAGE_DIRS:
        selected.extend(
            p for p in (ROOT / folder).rglob("*")
            if p.is_file() and p.suffix in PACKAGE_SUFFIXES
            and all(not n.startswith(".") and n != "__pycache__" for n in p.relative_to(ROOT).parts)
        )
    if any(not p.is_file() or p.is_symlink() or not p.resolve().is_relative_to(ROOT.resolve()) for p in selected):
        raise ValueError("Hay un archivo faltante o no local dentro del paquete.")
    return sorted(selected, key=lambda p: p.relative_to(ROOT).as_posix())


def verify(archive, expected):
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise ValueError("Error CRC en el ZIP")
        base = f"{ROOT.name}/"
        found = z.read(base + "MANIFEST.sha256").decode("utf-8").splitlines()
        if len(found) != len(expected) or len(z.namelist()) != len(expected) + 1 or len(set(z.namelist())) != len(z.namelist()):
            raise ValueError("Inventario de ZIP incompleto o con duplicados.")
        for line in found:
            digest, name = line.split("  ", 1)
            if not re.fullmatch(r"[a-f0-9]{64}", digest) or expected.get(name) != digest:
                raise ValueError(f"No coincide el manifest: {name}")
            if hashlib.sha256(z.read(base + name)).hexdigest() != digest:
                raise ValueError(f"No coincide el SHA-256: {name}")
        if {line.split("  ", 1)[1] for line in found} != set(expected):
            raise ValueError("Faltan rutas en el manifest.")


def main():
    members = files()
    expected = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in members}
    manifest = ROOT / "MANIFEST.sha256"
    manifest.write_text("".join(f"{h}  {n}\n" for n, h in expected.items()), encoding="utf-8", newline="\n")
    target = ROOT.with_suffix(".zip")
    scratch = ROOT.with_suffix(".zip.tmp")
    try:
        with zipfile.ZipFile(scratch, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for f in [*members, manifest]:
                z.write(f, (Path(ROOT.name) / f.relative_to(ROOT)).as_posix())
        verify(scratch, expected)
        scratch.replace(target)
    finally:
        scratch.unlink(missing_ok=True)
    print(f"{target.name}: {len(members) + 1} archivos, {target.stat().st_size} bytes, CRC y SHA-256 conformes")


if __name__ == "__main__":
    main()

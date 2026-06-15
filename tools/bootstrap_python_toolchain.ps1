param(
    [switch]$CheckOnly
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$Requirements = Join-Path $PSScriptRoot "requirements.txt"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "Repo-local Python not found: $Python"
}

if (-not (Test-Path -LiteralPath $Requirements)) {
    throw "Requirements file not found: $Requirements"
}

if (-not $CheckOnly) {
    & $Python -m pip install -r $Requirements
    if ($LASTEXITCODE -ne 0) {
        throw "pip install failed with exit code $LASTEXITCODE"
    }
}

$CheckScript = @'
import importlib.util
import sys

CHECKS = [
    ("Pillow", "PIL", "paleography core"),
    ("numpy", "numpy", "paleography core"),
    ("opencv-python-headless", "cv2", "paleography core"),
    ("PyMuPDF", "fitz", "PDF rendering"),
    ("pypdf", "pypdf", "PDF extraction"),
    ("pdfplumber", "pdfplumber", "PDF extraction"),
    ("pypdfium2", "pypdfium2", "PDF rendering fallback"),
    ("cryptography", "cryptography", "encrypted PDF support"),
    ("requests", "requests", "web retrieval"),
    ("beautifulsoup4", "bs4", "HTML parsing"),
    ("lxml", "lxml", "XML/HTML parsing"),
    ("openpyxl", "openpyxl", "spreadsheet support"),
]

print(f"Python: {sys.executable}")
print(f"Version: {sys.version.split()[0]}")
print()
print(f"{'Package':28} {'Import':18} {'Status':8} Purpose")
print("-" * 80)
missing = []
for package, import_name, purpose in CHECKS:
    ok = importlib.util.find_spec(import_name) is not None
    status = "OK" if ok else "MISSING"
    if not ok:
        missing.append(package)
    print(f"{package:28} {import_name:18} {status:8} {purpose}")

if missing:
    print()
    print("Missing packages: " + ", ".join(missing))
    raise SystemExit(1)
'@

$TempScript = Join-Path ([System.IO.Path]::GetTempPath()) "gurney-toolchain-check.py"
Set-Content -LiteralPath $TempScript -Value $CheckScript -Encoding UTF8
try {
    & $Python $TempScript
    if ($LASTEXITCODE -ne 0) {
        throw "toolchain check failed with exit code $LASTEXITCODE"
    }
}
finally {
    Remove-Item -LiteralPath $TempScript -ErrorAction SilentlyContinue
}

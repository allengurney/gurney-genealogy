const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const projectRoot = path.resolve(__dirname, "..");
const siteDir = path.join(projectRoot, "_site");
const distDir = path.join(projectRoot, "dist");
const stamp = new Date().toISOString().slice(0, 10);
const zipPath = path.join(distDir, `gurney-genealogy-site-${stamp}.zip`);
const requiredEntries = [
  "index.html",
  "assets/site.css",
  "assets/explorer.css",
  "assets/refactor.css",
  "assets/phase2.css",
  "assets/pedigree-explorer.js",
  "maps-and-lists/ancestor-table.html",
  "maps-and-lists/ancestor-map.html",
  "maps-and-lists/places.html",
];

function psQuote(value) {
  return `'${value.replace(/'/g, "''")}'`;
}

function runPowerShell(command) {
  execFileSync("powershell.exe", ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command], {
    stdio: "inherit",
  });
}

if (!fs.existsSync(siteDir)) {
  console.error("Cannot package site: _site/ does not exist. Run npm run build first.");
  process.exit(1);
}

fs.mkdirSync(distDir, { recursive: true });
if (fs.existsSync(zipPath)) fs.rmSync(zipPath, { force: true });

if (process.platform === "win32") {
  const command = `
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$source = ${psQuote(siteDir)}
$destination = ${psQuote(zipPath)}
if (Test-Path -LiteralPath $destination) {
  Remove-Item -LiteralPath $destination -Force
}
$archive = [System.IO.Compression.ZipFile]::Open($destination, [System.IO.Compression.ZipArchiveMode]::Create)
try {
  Get-ChildItem -LiteralPath $source -Recurse -File | ForEach-Object {
    $entryName = $_.FullName.Substring($source.Length).TrimStart([char[]]@('\\', '/')) -replace '\\\\', '/'
    $entry = $archive.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
    $entry.LastWriteTime = $_.LastWriteTime
    $inputStream = [System.IO.File]::OpenRead($_.FullName)
    try {
      $entryStream = $entry.Open()
      try {
        $inputStream.CopyTo($entryStream)
      } finally {
        $entryStream.Dispose()
      }
    } finally {
      $inputStream.Dispose()
    }
  }
} finally {
  $archive.Dispose()
}
`;
  runPowerShell(command);
} else {
  execFileSync("zip", ["-qr", zipPath, "."], { cwd: siteDir, stdio: "inherit" });
}

if (process.platform === "win32") {
  const required = requiredEntries.map(psQuote).join(", ");
  const command = `
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead(${psQuote(zipPath)})
try {
  $names = @($zip.Entries | ForEach-Object { $_.FullName })
  $required = @(${required})
  foreach ($entry in $required) {
    if ($names -notcontains $entry) {
      throw "Package missing required entry: $entry"
    }
  }
  foreach ($name in $names) {
    if ($name.Contains('\\')) {
      throw "Package contains Windows-style path separator: $name"
    }
  }
} finally {
  $zip.Dispose()
}
`;
  runPowerShell(command);
} else {
  const names = execFileSync("unzip", ["-Z1", zipPath], { encoding: "utf8" })
    .split(/\r?\n/)
    .filter(Boolean);
  for (const entry of requiredEntries) {
    if (!names.includes(entry)) {
      throw new Error(`Package missing required entry: ${entry}`);
    }
  }
}

console.log(`Packaged manual Cloudflare upload zip: ${path.relative(projectRoot, zipPath).replace(/\\/g, "/")}`);


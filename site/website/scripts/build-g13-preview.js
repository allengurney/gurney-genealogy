/*
 * G13 preview build (Plan 03 §4, revised 2026-07-06).
 *
 * Produces the cutover-shaped full-site zip for the Cloudflare preview host
 * (preview.genealogy-1l3.pages.dev):
 *   1. ordinary pipeline with G13_PACKAGE=staging (annex at canonical routes,
 *      flat legacy G13 companion suppressed),
 *   2. site validation,
 *   3. noindex hardening baked into the built output (robots.txt disallow-all
 *      + noindex meta on every page) so the preview host cannot be indexed,
 *   4. zip to dist/.
 *
 * The ordinary `npm run build` and `npm run package` paths are untouched.
 */
const fs = require("fs");
const path = require("path");
const { execSync, execFileSync } = require("child_process");

const projectRoot = path.resolve(__dirname, "..");
const siteDir = path.join(projectRoot, "_site");
const distDir = path.join(projectRoot, "dist");
const stamp = new Date().toISOString().slice(0, 10);
const zipPath = path.join(distDir, `gurney-genealogy-preview-g13-${stamp}.zip`);

const requiredEntries = [
  "index.html",
  "robots.txt",
  "research/notes/g13-john-gurney.html",
  "research/notes/g13-john-gurney/colonial/braintree-community.html",
  "research/evidence/g13-pm-000001/index.html",
  "research/findings/g13-ri-000001/index.html",
  "assets/g13-graph/markers.json",
  "assets/g13-graph/site-map.json",
  "assets/evidence-drawer.js",
  "assets/g13-graph-render.js",
  "assets/g13-annex.css",
];

function run(command) {
  execSync(command, {
    cwd: projectRoot,
    stdio: "inherit",
    env: { ...process.env, G13_PACKAGE: "staging" },
  });
}

function walkFiles(dir, predicate, results = []) {
  fs.readdirSync(dir, { withFileTypes: true }).forEach(entry => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walkFiles(full, predicate, results);
    else if (!predicate || predicate(full)) results.push(full);
  });
  return results;
}

function hardenForPreview() {
  fs.writeFileSync(
    path.join(siteDir, "robots.txt"),
    "# Preview deployment — not for indexing.\nUser-agent: *\nDisallow: /\n"
  );
  let injected = 0;
  walkFiles(siteDir, file => file.endsWith(".html")).forEach(file => {
    let html = fs.readFileSync(file, "utf8");
    if (/<meta\b[^>]*name=["']robots["']/i.test(html)) {
      html = html.replace(
        /<meta\b[^>]*name=["']robots["'][^>]*>/gi,
        '<meta name="robots" content="noindex,nofollow">'
      );
    } else {
      html = html.replace(/<\/head>/i, '  <meta name="robots" content="noindex,nofollow">\n</head>');
    }
    fs.writeFileSync(file, html);
    injected += 1;
  });
  console.log(`Preview hardening: robots.txt disallow-all + noindex meta on ${injected} pages.`);
}

function psQuote(value) {
  return `'${value.replace(/'/g, "''")}'`;
}

function zipSite() {
  fs.mkdirSync(distDir, { recursive: true });
  if (fs.existsSync(zipPath)) fs.rmSync(zipPath, { force: true });

  if (process.platform === "win32") {
    const command = `
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$source = ${psQuote(siteDir)}
$destination = ${psQuote(zipPath)}
$archive = [System.IO.Compression.ZipFile]::Open($destination, [System.IO.Compression.ZipArchiveMode]::Create)
try {
  Get-ChildItem -LiteralPath $source -Recurse -File | ForEach-Object {
    $entryName = $_.FullName.Substring($source.Length).TrimStart([char[]]@('\\', '/')) -replace '\\\\', '/'
    $entry = $archive.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
    $entry.LastWriteTime = $_.LastWriteTime
    $inputStream = [System.IO.File]::OpenRead($_.FullName)
    try {
      $entryStream = $entry.Open()
      try { $inputStream.CopyTo($entryStream) } finally { $entryStream.Dispose() }
    } finally { $inputStream.Dispose() }
  }
} finally { $archive.Dispose() }
$zip = [System.IO.Compression.ZipFile]::OpenRead($destination)
try {
  $names = @($zip.Entries | ForEach-Object { $_.FullName })
  $required = @(${requiredEntries.map(psQuote).join(", ")})
  foreach ($entry in $required) {
    if ($names -notcontains $entry) { throw "Preview package missing required entry: $entry" }
  }
  foreach ($name in $names) {
    if ($name.Contains('\\')) { throw "Preview package contains Windows-style path separator: $name" }
  }
} finally { $zip.Dispose() }
`;
    execFileSync("powershell.exe", ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command], {
      stdio: "inherit",
    });
  } else {
    execFileSync("zip", ["-qr", zipPath, "."], { cwd: siteDir, stdio: "inherit" });
    const names = execFileSync("unzip", ["-Z1", zipPath], { encoding: "utf8" }).split(/\r?\n/).filter(Boolean);
    requiredEntries.forEach(entry => {
      if (!names.includes(entry)) throw new Error(`Preview package missing required entry: ${entry}`);
    });
  }
}

run("npm run build");
run("npm run validate:site");
hardenForPreview();
zipSite();
console.log(`Packaged G13 preview zip: ${path.relative(projectRoot, zipPath).replace(/\\/g, "/")}`);

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const projectRoot = path.resolve(__dirname, "..");
const siteDir = path.join(projectRoot, "_site");
const distDir = path.join(projectRoot, "dist");
const stamp = new Date().toISOString().slice(0, 10);
const zipPath = path.join(distDir, `gurney-genealogy-site-${stamp}.zip`);

function psQuote(value) {
  return `'${value.replace(/'/g, "''")}'`;
}

if (!fs.existsSync(siteDir)) {
  console.error("Cannot package site: _site/ does not exist. Run npm run build first.");
  process.exit(1);
}

fs.mkdirSync(distDir, { recursive: true });
if (fs.existsSync(zipPath)) fs.rmSync(zipPath, { force: true });

if (process.platform === "win32") {
  const command = `Compress-Archive -Path ${psQuote(path.join(siteDir, "*"))} -DestinationPath ${psQuote(zipPath)} -Force`;
  execFileSync("powershell.exe", ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command], { stdio: "inherit" });
} else {
  execFileSync("zip", ["-qr", zipPath, "."], { cwd: siteDir, stdio: "inherit" });
}

console.log(`Packaged manual Cloudflare upload zip: ${path.relative(projectRoot, zipPath).replace(/\\/g, "/")}`);

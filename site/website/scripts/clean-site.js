const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const outputDir = path.join(projectRoot, "_site");

if (!outputDir.startsWith(projectRoot + path.sep)) {
  throw new Error(`Refusing to clean output outside project: ${outputDir}`);
}

// OneDrive's sync engine briefly holds directories it is syncing, which
// surfaces as EPERM/EBUSY on Windows. Retry with backoff instead of failing
// the whole build on a transient lock.
fs.rmSync(outputDir, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
console.log("Cleaned _site output directory.");

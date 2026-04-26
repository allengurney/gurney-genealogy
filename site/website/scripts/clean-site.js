const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const outputDir = path.join(projectRoot, "_site");

if (!outputDir.startsWith(projectRoot + path.sep)) {
  throw new Error(`Refusing to clean output outside project: ${outputDir}`);
}

fs.rmSync(outputDir, { recursive: true, force: true });
console.log("Cleaned _site output directory.");

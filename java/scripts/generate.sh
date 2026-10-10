#!/usr/bin/env bash
# Regenerates the Java client from ../openapi/pleaxy.json. Needs Java 11+ and Node.
# OPENAPI_GENERATOR_JAR: path to openapi-generator-cli-7.10.0.jar (downloaded when unset).
set -euo pipefail
cd "$(dirname "$0")/.."
jar="${OPENAPI_GENERATOR_JAR:-}"
if [ -z "$jar" ]; then
  jar="$(mktemp -d)/openapi-generator-cli.jar"
  curl -sSfLo "$jar" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.10.0/openapi-generator-cli-7.10.0.jar
fi
rm -rf src/main/java/ai/pleaxy/api src/main/java/ai/pleaxy/model src/main/java/ai/pleaxy/client
java -jar "$jar" generate -c openapi-generator.yaml >/dev/null
node scripts/fix-generated.mjs

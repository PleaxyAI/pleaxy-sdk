#!/usr/bin/env bash
# Regenerates the Rust client from ../openapi/pleaxy.json. Needs Java 11+, Node and cargo.
# OPENAPI_GENERATOR_JAR: path to openapi-generator-cli-7.10.0.jar (downloaded when unset).
set -euo pipefail
cd "$(dirname "$0")/.."
jar="${OPENAPI_GENERATOR_JAR:-}"
if [ -z "$jar" ]; then
  jar="$(mktemp -d)/openapi-generator-cli.jar"
  curl -sSfLo "$jar" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.10.0/openapi-generator-cli-7.10.0.jar
fi
rm -rf src/apis src/models
java -jar "$jar" generate -c openapi-generator.yaml >/dev/null
rm -rf .openapi-generator
node scripts/generate-resources.mjs
cargo fmt

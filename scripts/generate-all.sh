#!/usr/bin/env bash
# Regenerates every SDK from openapi/openapi.sdk.json (the backend's export).
# Needs Node 18+, Python 3.9+, Go 1.21+, Java 11+, Rust (cargo). Run from anywhere.
set -euo pipefail
cd "$(dirname "$0")/.."
node scripts/prepare-spec.mjs

echo "== typescript"
(cd typescript && npm ci --silent && npm run -s generate)

echo "== python"
# The generator runs ruff on its output, so it gets the pinned ruff in its own venv (python/.venv, gitignored):
# a newer ruff first on PATH rewrites or rejects the generated code.
(cd python && { [ -x .venv/bin/python ] || python3 -m venv .venv; } && .venv/bin/pip install -q -r requirements-generate.txt && PATH="$PWD/.venv/bin:$PATH" ./scripts/generate.sh)

echo "== go"
(cd go && go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@v2.4.1 -config oapi-codegen.yaml ../openapi/pleaxy.json && node scripts/generate-operations.mjs && gofmt -w .)

jar="${OPENAPI_GENERATOR_JAR:-$(mktemp -d)/openapi-generator-cli.jar}"
[ -f "$jar" ] || curl -sSfLo "$jar" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.10.0/openapi-generator-cli-7.10.0.jar
export OPENAPI_GENERATOR_JAR="$jar"

echo "== java"
(cd java && ./scripts/generate.sh)

echo "== ruby"
(cd ruby && ./scripts/generate.sh)

echo "== rust"
(cd rust && ./scripts/generate.sh)

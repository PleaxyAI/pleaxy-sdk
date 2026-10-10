#!/usr/bin/env bash
# Regenerates the Ruby client from ../openapi/pleaxy.json. Needs Java 11+.
# OPENAPI_GENERATOR_JAR: path to openapi-generator-cli-7.10.0.jar (downloaded when unset).
set -euo pipefail
cd "$(dirname "$0")/.."
jar="${OPENAPI_GENERATOR_JAR:-}"
if [ -z "$jar" ]; then
  jar="$(mktemp -d)/openapi-generator-cli.jar"
  curl -sSfLo "$jar" https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.10.0/openapi-generator-cli-7.10.0.jar
fi
rm -rf lib/pleaxy/api lib/pleaxy/models
java -jar "$jar" generate -c openapi-generator.yaml >/dev/null
# openapi-generator 7.10's ApiClient builds a oneOf union with .build but an anyOf
# one with .build_from_hash, which anyOf modules don't have: every operation
# returning a union (GetPurchaseOrder, GetInvoice, ...) would raise NoMethodError.
sed -i.bak 's/klass.respond_to?(:openapi_one_of) ? klass.build(data)/(klass.respond_to?(:openapi_one_of) || klass.respond_to?(:openapi_any_of)) ? klass.build(data)/' lib/pleaxy/api_client.rb
rm lib/pleaxy/api_client.rb.bak
grep -q 'openapi_any_of)) ? klass.build' lib/pleaxy/api_client.rb || { echo "generate.sh: the anyOf fix no longer applies" >&2; exit 1; }
# lib/pleaxy.rb is generated; load the hand-written client from it.
echo "require 'pleaxy/client'" >> lib/pleaxy.rb

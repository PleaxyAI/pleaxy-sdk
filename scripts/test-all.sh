#!/usr/bin/env bash
# Builds and tests every SDK, including its quickstart example.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== typescript"
(cd typescript && npm ci --silent && npx tsc --noEmit && npm test && npm run -s build)

echo "== python"
(cd python && pip install -q -e . pytest==8.3.4 mypy==1.13.0 && pytest -q && mypy)

echo "== go"
(cd go && test -z "$(gofmt -l .)" && go vet ./... && go test ./...)

echo "== java"
(cd java && mvn -q -B verify)

echo "== ruby"
(cd ruby && bundle install --quiet && bundle exec rake)

echo "== rust"
(cd rust && cargo fmt --check && cargo test && cargo build --examples)

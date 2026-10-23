#!/usr/bin/env bash
# Builds and tests every SDK, including its quickstart example.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== typescript"
(cd typescript && npm ci --silent && npx tsc --noEmit && npm test && npm run -s build)

echo "== python"
# The same venv as generation (python/.venv), so pip, pytest and mypy are one interpreter whatever is on PATH.
(cd python && { [ -x .venv/bin/python ] || python3 -m venv .venv; } && .venv/bin/pip install -q -e . pytest==8.3.4 mypy==1.13.0 && .venv/bin/pytest -q && .venv/bin/mypy)

echo "== go"
(cd go && test -z "$(gofmt -l .)" && go vet ./... && go test ./...)

echo "== java"
(cd java && mvn -q -B verify)

echo "== ruby"
# Gem.bin_path finds rake whether or not the Ruby install's bin directory is on PATH.
(cd ruby && bundle install --quiet && bundle exec ruby -e 'load Gem.bin_path("rake", "rake")')

echo "== rust"
(cd rust && cargo fmt --check && cargo test && cargo build --examples)

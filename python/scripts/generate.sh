#!/usr/bin/env bash
# Regenerates src/pleaxy/_generated and src/pleaxy/_resources.py from ../openapi/pleaxy.json.
# Needs: pip install -r requirements-generate.txt
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf src/pleaxy/_generated
openapi-python-client generate --path ../openapi/pleaxy.json --config generator.yaml --meta none --output-path src/pleaxy/_generated
python scripts/generate_resources.py
ruff format --quiet src/pleaxy/_resources.py

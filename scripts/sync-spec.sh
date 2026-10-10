#!/usr/bin/env bash
# Copies the backend's SDK document into openapi/: scripts/sync-spec.sh ../pleaxy-backend
# The backend writes it with `npm run openapi:export` (openapi/openapi.sdk.json there).
set -euo pipefail
cd "$(dirname "$0")/.."
backend="${1:?usage: scripts/sync-spec.sh <path to a pleaxy-backend checkout>}"
cp "$backend/openapi/openapi.sdk.json" openapi/openapi.sdk.json
node scripts/prepare-spec.mjs

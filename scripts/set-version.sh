#!/usr/bin/env bash
# Sets the version of every SDK: scripts/set-version.sh 0.2.0
# Then run scripts/generate-all.sh (the Ruby gem's version.rb is generated) and commit.
# Go has no version file: its release is the go/vX.Y.Z tag that release.yml pushes.
set -euo pipefail
cd "$(dirname "$0")/.."
version="${1:?usage: scripts/set-version.sh X.Y.Z}"
[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.]+)?$ ]] || { echo "not a semantic version: $version" >&2; exit 1; }

echo "$version" > VERSION
(cd typescript && npm pkg set version="$version")
sed -i.bak -E "s/^version = \".*\"/version = \"$version\"/" python/pyproject.toml
sed -i.bak -E "s/^__version__ = \".*\"/__version__ = \"$version\"/" python/src/pleaxy/__init__.py
sed -i.bak -E "s/^artifactVersion: .*/artifactVersion: $version/" java/openapi-generator.yaml
# The pom's first <version> is the project's own (it has no parent).
sed -i.bak -E "0,/<version>[^<]*<\/version>/s||<version>$version</version>|" java/pom.xml
sed -i.bak -E "s/^  gemVersion: .*/  gemVersion: $version/" ruby/openapi-generator.yaml
find . -name '*.bak' -not -path '*/node_modules/*' -delete
echo "version $version - now run scripts/generate-all.sh"

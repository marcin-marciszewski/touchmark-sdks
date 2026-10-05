#!/usr/bin/env bash
# Regenerate the clients from openapi/openapi.json.
set -euo pipefail
cd "$(dirname "$0")/.."
(cd typescript && npm run generate)

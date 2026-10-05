#!/usr/bin/env bash
# Pack the package, install the tarball in a clean project, and check that it
# imports at runtime and type-checks under Node's module resolution.
set -euo pipefail
cd "$(dirname "$0")/.."
package_dir=$PWD
tarball=$(npm pack --silent | tail -1)
work=$(mktemp -d)
# By its full path: the script works in "$work" when the trap runs.
trap 'rm -rf "$work"; rm -f "$package_dir/$tarball"' EXIT
cp "$tarball" "$work/"
cd "$work"
npm init -y >/dev/null
npm install --silent "./$tarball" typescript@5.9.2
node --input-type=module -e '
import { Touchmark, TouchmarkError } from "touchmark"
const tm = new Touchmark({ apiKey: "vld_live_check" })
if (typeof tm.email.validate !== "function" || typeof TouchmarkError !== "function") process.exit(1)
console.log("runtime import ok")
'
cat > check.mts <<'TS'
import { Touchmark, type ValidateResponse } from "touchmark"
const tm = new Touchmark({ apiKey: "vld_live_check" })
export const answer: Promise<ValidateResponse> = tm.email.validate({ email: "a@b.co" })
TS
npx tsc --noEmit --strict --module nodenext --moduleResolution nodenext --target es2022 check.mts
echo "types ok"

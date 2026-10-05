import { defineConfig } from "@hey-api/openapi-ts"

// Types only: the hand-written client in src/index.ts makes the requests, so
// the package ships no generated runtime code.
export default defineConfig({
  input: "../openapi/openapi.json",
  output: { path: "./src/gen", importFileExtension: ".js" },
  plugins: [{ name: "@hey-api/typescript" }],
})

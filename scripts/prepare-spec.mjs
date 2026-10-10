#!/usr/bin/env node
// Turns the backend's openapi.sdk.json (copied into openapi/ by scripts/sync-spec.sh)
// into openapi/pleaxy.json, the document every generator reads:
//
// - Every SDK operation lives under /v1/workspaces/{regionId}. The workspace
//   moves into the base URL instead, so each client is configured once with a
//   workspace ID and no call takes one: /purchase-orders, not
//   /v1/workspaces/{regionId}/purchase-orders.
// - Request models drop the backend's "Dto" suffix for "Input":
//   CreatePurchaseOrderDto -> CreatePurchaseOrderInput.
// - Response models require nothing but `id`. The API's types say which
//   fields it sends, but a record stored before a field existed can lack it,
//   and a strict SDK (Python, Java) would then fail to read the whole
//   response. An object's id is its key and always there. Request models
//   keep their required fields.
// - An inline response body (a union like buyer-or-supplier view, or an
//   object literal) becomes a named model, <OperationId>Result (or
//   <OperationId>Item for a list's entries), so every language can name it.
// - Numbers are doubles: without a format, Go would read amounts as float32.
// - A `/` in a pattern is escaped (`\/`, the same regex in every language):
//   the Ruby generator writes patterns as /.../ literals.
// - The SDK version and license are stamped in.
//
// Usage: node scripts/prepare-spec.mjs [version]
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const PREFIX = "/v1/workspaces/{regionId}";
const version = process.argv[2] ?? readFileSync(resolve(root, "VERSION"), "utf8").trim();
const source = JSON.parse(readFileSync(resolve(root, "openapi/openapi.sdk.json"), "utf8"));

const paths = {};
for (const [path, item] of Object.entries(source.paths)) {
  if (!path.startsWith(PREFIX)) throw new Error(`${path} is not under ${PREFIX}`);
  const rest = path.slice(PREFIX.length) || "/";
  const out = {};
  for (const [key, value] of Object.entries(item)) {
    if (key === "parameters") continue;
    out[key] = { ...value, parameters: (value.parameters ?? []).filter((p) => !(p.in === "path" && p.name === "regionId")) };
    if (!out[key].parameters.length) delete out[key].parameters;
  }
  paths[rest] = out;
}

const renames = {};
for (const name of Object.keys(source.components.schemas)) {
  if (!name.endsWith("Dto")) continue;
  const renamed = name.slice(0, -"Dto".length) + "Input";
  if (source.components.schemas[renamed]) throw new Error(`Renaming ${name} would collide with ${renamed}`);
  renames[name] = renamed;
}
const renameRefs = (node) => {
  if (Array.isArray(node)) return node.map(renameRefs);
  if (!node || typeof node !== "object") return node;
  return Object.fromEntries(
    Object.entries(node).map(([key, value]) => {
      if (key === "$ref" && typeof value === "string") {
        const name = value.replace("#/components/schemas/", "");
        return [key, renames[name] ? `#/components/schemas/${renames[name]}` : value];
      }
      return [key, renameRefs(value)];
    })
  );
};
const schemas = Object.fromEntries(Object.entries(source.components.schemas).map(([name, schema]) => [renames[name] ?? name, renameRefs(schema)]));

const spec = {
  ...source,
  info: {
    ...source.info,
    version,
    license: { name: "MIT", url: "https://opensource.org/licenses/MIT" },
  },
  servers: [
    {
      url: "https://api.pleaxy.ai/v1/workspaces/{workspaceId}",
      description: "One workspace's API. The SDK clients build this from baseUrl and workspaceId.",
      variables: { workspaceId: { default: "WORKSPACE_ID", description: "Company profile → Workspace ID in the Pleaxy console." } },
    },
  ],
  paths: renameRefs(paths),
  components: { ...source.components, schemas },
};

for (const item of Object.values(spec.paths)) {
  for (const op of Object.values(item)) {
    for (const [code, response] of Object.entries(op.responses)) {
      const media = code.startsWith("2") && response.content?.["application/json"];
      if (!media?.schema || media.schema.$ref) continue;
      const hoist = (schema, name) => {
        if (spec.components.schemas[name]) throw new Error(`${name} already exists`);
        spec.components.schemas[name] = schema;
        return { $ref: `#/components/schemas/${name}` };
      };
      const schema = media.schema;
      if (schema.type === "array") {
        if (schema.items && !schema.items.$ref && (schema.items.anyOf || schema.items.type === "object")) schema.items = hoist(schema.items, `${op.operationId}Item`);
      } else if (schema.anyOf || schema.type === "object" || schema.allOf) {
        media.schema = hoist(schema, `${op.operationId}Result`);
      }
    }
  }
}
const doubles = (node) => {
  if (Array.isArray(node)) return node.forEach(doubles);
  if (!node || typeof node !== "object") return;
  if (node.type === "number" && !node.format) node.format = "double";
  if (typeof node.pattern === "string") node.pattern = node.pattern.replace(/(?<!\\)\//g, "\\/");
  Object.values(node).forEach(doubles);
};
doubles(spec);

// Schemas a request body reaches keep `required`; everything else is response-only.
const requestSchemas = new Set();
const collect = (node) => {
  if (Array.isArray(node)) return node.forEach(collect);
  if (!node || typeof node !== "object") return;
  for (const [key, value] of Object.entries(node)) {
    if (key === "$ref" && typeof value === "string") {
      const name = value.replace("#/components/schemas/", "");
      if (!requestSchemas.has(name)) {
        requestSchemas.add(name);
        collect(spec.components.schemas[name]);
      }
    } else collect(value);
  }
};
for (const item of Object.values(spec.paths)) for (const op of Object.values(item)) collect([op.requestBody, op.parameters]);
const lenient = (node) => {
  if (Array.isArray(node)) return node.forEach(lenient);
  if (!node || typeof node !== "object") return;
  if (node.type === "object" && Array.isArray(node.required)) {
    if (node.required.includes("id")) node.required = ["id"];
    else delete node.required;
  }
  Object.values(node).forEach(lenient);
};
for (const [name, schema] of Object.entries(spec.components.schemas)) if (!requestSchemas.has(name) && name !== "ApiError") lenient(schema);
for (const item of Object.values(spec.paths)) for (const op of Object.values(item)) lenient(Object.entries(op.responses).filter(([code]) => code !== "default").map(([, r]) => r));

writeFileSync(resolve(root, "openapi/pleaxy.json"), JSON.stringify(spec, null, 2) + "\n");
console.log(`openapi/pleaxy.json: ${Object.keys(paths).length} paths, version ${version}`);

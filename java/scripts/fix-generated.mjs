#!/usr/bin/env node
// openapi-generator 7.10's Java templates write invalid code for a union with a
// list member (ApiError.message is a string or a list of strings): `List<X>.class`
// and a getter named `getList<X>()`. This rewrites those three forms. It also
// saves a file download (CSV, PDF) with ai.pleaxy.Downloads instead of parsing it
// as JSON, which the native library's template does.
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "../src/main/java/ai/pleaxy");
let fixed = 0;
const files = ["model", "api"].flatMap((sub) => readdirSync(resolve(root, sub)).map((file) => resolve(root, sub, file)));
for (const path of files) {
  const before = readFileSync(path, "utf8");
  const after = before
    .replace(/readValueAs\(List<(\w+)>\.class\)/g, "readValueAs(new com.fasterxml.jackson.core.type.TypeReference<List<$1>>() {})")
    .replace(/List<\w+>\.class/g, "List.class")
    .replace(/\bgetList<(\w+)>\(\)/g, "get$1List()")
    .replace(/memberVarObjectMapper\.readValue\(localVarResponse\.body\(\), new TypeReference<File>\(\) \{\}\)/g, "ai.pleaxy.Downloads.toTempFile(localVarResponse.body())");
  if (after !== before) {
    writeFileSync(path, after);
    fixed++;
  }
}
console.log(`fix-generated: ${fixed} files rewritten`);

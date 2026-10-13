# Pleaxy SDKs

Official clients for the [Pleaxy API](https://pleaxy.ai/api-reference) - purchase orders, invoices and settlement for cloud spend - generated from the same OpenAPI document as the API Reference.

| Language | Package | Install | |
|---|---|---|---|
| TypeScript / JavaScript | [`@pleaxy/sdk`](https://www.npmjs.com/package/@pleaxy/sdk) | `npm install @pleaxy/sdk` | [typescript/](typescript) |
| Python | [`pleaxy`](https://pypi.org/project/pleaxy/) | `pip install pleaxy` | [python/](python) |
| Go | `github.com/pleaxyai/pleaxy-sdk/go` | `go get github.com/pleaxyai/pleaxy-sdk/go` | [go/](go) |
| Java | [`ai.pleaxy:pleaxy-java`](https://central.sonatype.com/artifact/ai.pleaxy/pleaxy-java) | Maven / Gradle | [java/](java) |
| Ruby | [`pleaxy`](https://rubygems.org/gems/pleaxy) | `gem install pleaxy` | [ruby/](ruby) |
| Rust | [`pleaxy`](https://crates.io/crates/pleaxy) | `cargo add pleaxy` | [rust/](rust) |

Every SDK works the same way: create a client with an API key and your **Workspace ID** (Company profile → Workspace ID in the Pleaxy console), then call the operations from the API Reference by name - `CreatePurchaseOrder` is `createPurchaseOrder`, `create_purchase_order` or `CreatePurchaseOrder` depending on the language. A failed call raises the language's error type with the HTTP status and the API's machine-readable `code`.

Need another language? [`openapi/pleaxy.json`](openapi/pleaxy.json) works with any OpenAPI 3.0 code generator.

## How this repository works

```
openapi/openapi.sdk.json   the API's public operations, exported by pleaxy-backend (npm run openapi:export)
openapi/pleaxy.json        what the generators read (scripts/prepare-spec.mjs)
typescript/ python/ go/ java/ ruby/ rust/
                           generated code plus a small hand-written client per language
```

`scripts/prepare-spec.mjs` turns the backend's document into the generators' input: the workspace moves from every path into the client's base URL, request models are named `...Input`, inline responses get names (`GetPurchaseOrderResult`), and response fields are all optional, so an SDK never fails to read a response that lacks a field.

The generators, all free and pinned: [openapi-typescript](https://openapi-ts.dev) + [openapi-fetch](https://openapi-ts.dev/openapi-fetch/), [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen), and [OpenAPI Generator](https://openapi-generator.tech) for Java, Ruby and Rust.

### Updating the SDKs after an API change

```bash
scripts/sync-spec.sh ../pleaxy-backend   # copy the backend's openapi/openapi.sdk.json
scripts/generate-all.sh                  # regenerate all six (Node, Python, Go, Java, Rust)
scripts/test-all.sh                      # build and test them, quickstarts included
```

CI fails a pull request whose generated code doesn't match `openapi/`.

### Releasing

```bash
scripts/set-version.sh 0.2.0 && scripts/generate-all.sh
git commit -am "Release 0.2.0" && git tag v0.2.0 && git push origin master v0.2.0
```

The tag runs [`.github/workflows/release.yml`](.github/workflows/release.yml), which publishes to npm, PyPI, RubyGems, Maven Central and crates.io and tags the Go module (`go/v0.2.0`). The secrets it needs are listed at the top of that file.

Versions follow semver and are shared across languages. Before 1.0, a minor version may change method or model names when the API does.

## License

MIT

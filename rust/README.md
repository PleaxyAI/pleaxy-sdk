# Pleaxy Rust SDK

The official Rust client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```bash
cargo add pleaxy
```

Async, on `reqwest` with rustls. Rust 1.88+.

## Quickstart

```rust
use pleaxy::models::{create_purchase_order_input, line_item_input, CreatePurchaseOrderInput, LineItemInput};

let client = pleaxy::Client::builder()
    .api_key(std::env::var("PLEAXY_API_KEY")?)            // <keyId>.<secret>, minted by a workspace administrator
    .workspace_id(std::env::var("PLEAXY_WORKSPACE_ID")?)  // Company profile → Workspace ID in the Pleaxy console
    .build()?;

let mut line = LineItemInput::new(
    line_item_input::ScopeType::Sku,
    "EC2 m5.large".into(),
    line_item_input::RuleType::Quantity,
    "hr".into(),
    0.096,     // unit price
    5000.0,    // quantity
    0.0,       // not-to-exceed amount
    "Net 30".into(),
    "2026-01-01".into(),
    "2026-12-31".into(),
);
line.scope_id = Some(Some("AWS-EC2-M5LG".into()));

let mut input = CreatePurchaseOrderInput::new("Amazon Web Services".into(), vec![line]);
input.provider = Some(create_purchase_order_input::Provider::Aws);

let po = client.purchase_orders().create_purchase_order(input).await?;
println!("{}", po.id);
```

Operations are grouped by API area (`client.purchase_orders()`, `client.invoices()`, ...) and named after the operations in the [API Reference](https://pleaxy.ai/api-reference): `CreatePurchaseOrder` is `create_purchase_order`. Arguments are the path parameters, then the JSON body, then the query parameters as `Option`s. Models are in `pleaxy::models`; `new` takes the required fields and the rest are public `Option` fields. File downloads (a payment export's CSV, a remittance advice PDF) return `Vec<u8>`.

## Errors

A failed call returns `pleaxy::apis::Error<E>`. For a non-2xx response, `pleaxy::api_error(&err)` gives the HTTP `status`, the API's machine-readable `code` when it names one (e.g. `PO_ID_AMBIGUOUS`) and the `message`:

```rust
if let Err(err) = client.invoices().approve_invoice("INV-1").await {
    if let Some(api) = pleaxy::api_error(&err) {
        if api.code.as_deref() == Some("HUMAN_APPROVAL_REQUIRED") {
            // ...
        }
    }
}
```

## Configuration

| Builder method | Default | |
|---|---|---|
| `workspace_id` | required | Every call is scoped to this workspace. |
| `api_key` / `access_token` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `base_url` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<workspace_id>`. |
| `timeout` | 30 seconds | How long to wait for a response. |
| `http_client` | | The `reqwest::Client` requests are sent with, e.g. for a proxy. |

`client.configuration()` is the generated `Configuration`, to call a function in `pleaxy::apis` directly.

## Development

`src/apis`, `src/models` and `src/resources.rs` are generated from `../openapi/pleaxy.json` (`./scripts/generate.sh`); don't edit them by hand. `src/client.rs` and `src/lib.rs` are maintained here.

```bash
cargo test && cargo build --examples
```

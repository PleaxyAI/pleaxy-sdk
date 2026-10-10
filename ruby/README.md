# Pleaxy Ruby SDK

The official Ruby client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```bash
gem install pleaxy
```

Ruby 3.0+.

## Quickstart

```ruby
require 'pleaxy'

client = Pleaxy::Client.new(
  api_key: ENV.fetch('PLEAXY_API_KEY'),           # <keyId>.<secret>, minted by a workspace administrator
  workspace_id: ENV.fetch('PLEAXY_WORKSPACE_ID')  # Company profile → Workspace ID in the Pleaxy console
)

po = client.purchase_orders.create_purchase_order(
  Pleaxy::CreatePurchaseOrderInput.new(
    supplier: 'Amazon Web Services',
    provider: 'aws',
    line_items: [
      Pleaxy::LineItemInput.new(
        scope_type: 'sku',
        scope_id: 'AWS-EC2-M5LG',
        name: 'EC2 m5.large',
        rule_type: 'quantity',
        unit: 'hr',
        unit_price: 0.096,
        qty: 5000,
        nte_amount: 0,
        payment_terms: 'Net 30',
        valid_from: '2026-01-01',
        valid_until: '2026-12-31'
      )
    ]
  )
)
puts po.id
```

Operations are grouped by API area (`client.purchase_orders`, `client.invoices`, ...) and named after the operations in the [API Reference](https://pleaxy.ai/api-reference): `CreatePurchaseOrder` is `create_purchase_order`. Query parameters go in a trailing hash: `client.purchase_orders.get_purchase_order('PO-8842', buyer: 'reg_...buyer')`. File downloads return a `Tempfile`.

## Errors

A non-2xx response raises `Pleaxy::ApiError` with `code` (the HTTP status) and `response_body`. `Pleaxy::Client.error(e)` parses the body, including the API's machine-readable `:code` when it names one (e.g. `PO_ID_AMBIGUOUS`):

```ruby
begin
  client.invoices.approve_invoice('INV-1')
rescue Pleaxy::ApiError => e
  Pleaxy::Client.error(e)&.dig(:code) # => "HUMAN_APPROVAL_REQUIRED"
end
```

## Configuration

| Argument | Default | |
|---|---|---|
| `workspace_id` | required | Every call is scoped to this workspace. |
| `api_key` / `access_token` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `base_url` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<workspace_id>`. |
| `timeout` | `30` | Seconds to wait for a response. |
| `logger` | silent | Where the underlying client logs. |

Pass a block to configure the Faraday connection (a proxy, an adapter): `Pleaxy::Client.new(...) { |conn| conn.proxy = '...' }`.

## Development

`lib/pleaxy.rb`, `lib/pleaxy/{api,models}` and the rest of `lib/pleaxy` except `client.rb` are generated from `../openapi/pleaxy.json` (`./scripts/generate.sh`); don't edit them by hand.

```bash
bundle install && bundle exec rake
```

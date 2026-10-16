# Pleaxy Go SDK

The official Go client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```bash
go get github.com/pleaxyai/pleaxy-sdk/go
```

Go 1.21+.

## Quickstart

```go
import "github.com/pleaxyai/pleaxy-sdk/go" // package pleaxy

client, err := pleaxy.NewClient(pleaxy.Config{
	APIKey:      os.Getenv("PLEAXY_API_KEY"),      // <keyId>.<secret>, minted by a workspace administrator
	WorkspaceID: os.Getenv("PLEAXY_WORKSPACE_ID"), // Company profile → Workspace ID in the Pleaxy console
})
if err != nil {
	log.Fatal(err)
}

po, err := client.CreatePurchaseOrder(ctx, pleaxy.CreatePurchaseOrderInput{
	Supplier: "Amazon Web Services",
	Provider: pleaxy.Ptr(pleaxy.CreatePurchaseOrderInputProviderAws),
	LineItems: []pleaxy.LineItemInput{
		{
			ScopeType:    pleaxy.LineItemInputScopeTypeSku,
			ScopeId:      pleaxy.Ptr("AWS-EC2-M5LG"),
			Name:         "EC2 m5.large",
			RuleType:     pleaxy.LineItemInputRuleTypeQuantity,
			Unit:         "hr",
			UnitPrice:    0.096,
			Qty:          5000,
			NteAmount:    0,
			PaymentTerms: pleaxy.Ptr("Net 30"),
			ValidFrom:    "2026-01-01",
			ValidUntil:   "2026-12-31",
		},
	},
})
```

Methods are named after the operations in the [API Reference](https://pleaxy.ai/api-reference) (`CreatePurchaseOrder`) and take the path parameters, then the query parameters (`*<Operation>Params`, nil for none), then the JSON body. Optional fields are pointers: `pleaxy.Ptr(v)` makes one. File downloads return `[]byte`.

A response that is one of several shapes - a buyer's or a supplier's view of an order - is a union type with `As...` methods:

```go
result, err := client.GetPurchaseOrder(ctx, "PO-8842", nil)
po, err := result.AsPurchaseOrder()
```

## Errors

A non-2xx response is returned as a `*pleaxy.Error` with `StatusCode`, the API's machine-readable `Code` when it names one (e.g. `PO_ID_AMBIGUOUS`), `Message` and the raw `Body`.

```go
var apiErr *pleaxy.Error
if errors.As(err, &apiErr) && apiErr.Code == "HUMAN_APPROVAL_REQUIRED" {
	// ...
}
```

## Configuration

| Field | Default | |
|---|---|---|
| `WorkspaceID` | required | Every call is scoped to this workspace. |
| `APIKey` / `AccessToken` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `BaseURL` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<WorkspaceID>`. |
| `HTTPClient` | 30-second timeout | The `*http.Client` requests are sent with. |

`client.Raw()` is the underlying [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen) client, for anything the methods don't expose (response headers, for one).

## Development

`pleaxy.gen.go` and `operations.gen.go` are generated from `../openapi/pleaxy.json` (`go generate ./...`); don't edit them by hand.

```bash
go vet ./... && go test ./...
```

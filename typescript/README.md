# Pleaxy TypeScript SDK

The official TypeScript/JavaScript client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```bash
npm install @pleaxy/sdk
```

Node 18+, Deno, Bun, or any runtime with `fetch`. ESM and CommonJS, fully typed.

## Quickstart

```ts
import { Pleaxy } from "@pleaxy/sdk";

const pleaxy = new Pleaxy({
  apiKey: process.env.PLEAXY_API_KEY,               // <keyId>.<secret>, minted by a workspace administrator
  workspaceId: process.env.PLEAXY_WORKSPACE_ID!,    // Company profile → Workspace ID in the Pleaxy console
});

const po = await pleaxy.purchaseOrders.createPurchaseOrder({
  supplier: "Amazon Web Services",
  provider: "aws",
  lineItems: [
    {
      scopeType: "sku",
      scopeId: "AWS-EC2-M5LG",
      name: "EC2 m5.large",
      ruleType: "quantity",
      unit: "hr",
      unitPrice: 0.096,
      qty: 5_000,
      nteAmount: 0,
      paymentTerms: "Net 30",
      validFrom: "2026-01-01",
      validUntil: "2026-12-31",
    },
  ],
});
```

Methods are grouped by API area (`pleaxy.purchaseOrders`, `pleaxy.invoices`, ...) and named after the operations in the [API Reference](https://pleaxy.ai/api-reference): `CreatePurchaseOrder` is `createPurchaseOrder`. Arguments are the path parameters, then the JSON body, then the query parameters:

```ts
const po = await pleaxy.purchaseOrders.getPurchaseOrder("PO-8842", { buyer: "reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer" });
const csv = await pleaxy.invoices.exportInvoicesForPayment(); // file downloads are ArrayBuffers
```

Every request and response type is exported: `PurchaseOrder`, `InvoiceBuyerView`, `CreatePurchaseOrderInput`, or any schema as `components["schemas"]["..."]`.

## Errors

A non-2xx response throws `PleaxyError` with `status`, the API's machine-readable `code` when it names one (e.g. `PO_ID_AMBIGUOUS`), the parsed `body` and the `response`.

```ts
import { PleaxyError } from "@pleaxy/sdk";

try {
  await pleaxy.invoices.approveInvoice("INV-1");
} catch (err) {
  if (err instanceof PleaxyError && err.code === "HUMAN_APPROVAL_REQUIRED") {
    // ...
  }
}
```

## Configuration

| Option | Default | |
|---|---|---|
| `workspaceId` | required | Every call is scoped to this workspace. |
| `apiKey` / `accessToken` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `baseUrl` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<workspaceId>`. |
| `headers` | | Sent with every call. |
| `fetch` | `globalThis.fetch` | A custom fetch, e.g. for a proxy or tests. |

Every method also takes a last `options` argument with per-call `headers` and an abort `signal`. `pleaxy.raw` is the underlying [openapi-fetch](https://openapi-ts.dev/openapi-fetch/) client, typed against the whole API, for anything the methods don't expose (response headers, for one).

## Development

`src/schema.ts` and `src/operations.ts` are generated from `../openapi/pleaxy.json` (`npm run generate`); don't edit them by hand.

```bash
npm ci && npm run typecheck && npm test && npm run build
```

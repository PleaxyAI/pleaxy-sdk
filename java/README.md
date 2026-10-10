# Pleaxy Java SDK

The official Java client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```xml
<dependency>
  <groupId>ai.pleaxy</groupId>
  <artifactId>pleaxy-java</artifactId>
  <version>0.1.0</version>
</dependency>
```

Gradle: `implementation("ai.pleaxy:pleaxy-java:0.1.0")`. Java 11+; uses `java.net.http` and Jackson.

## Quickstart

```java
import ai.pleaxy.PleaxyClient;
import ai.pleaxy.model.CreatePurchaseOrderInput;
import ai.pleaxy.model.LineItemInput;
import ai.pleaxy.model.PurchaseOrder;

PleaxyClient client = PleaxyClient.builder()
    .apiKey(System.getenv("PLEAXY_API_KEY"))            // <keyId>.<secret>, minted by a workspace administrator
    .workspaceId(System.getenv("PLEAXY_WORKSPACE_ID"))  // Company profile → Workspace ID in the Pleaxy console
    .build();

PurchaseOrder po = client.purchaseOrders().createPurchaseOrder(new CreatePurchaseOrderInput()
    .supplier("Amazon Web Services")
    .provider(CreatePurchaseOrderInput.ProviderEnum.AWS)
    .lineItems(List.of(new LineItemInput()
        .scopeType(LineItemInput.ScopeTypeEnum.SKU)
        .scopeId("AWS-EC2-M5LG")
        .name("EC2 m5.large")
        .ruleType(LineItemInput.RuleTypeEnum.QUANTITY)
        .unit("hr")
        .unitPrice(0.096)
        .qty(5000.0)
        .nteAmount(0.0)
        .paymentTerms("Net 30")
        .validFrom("2026-01-01")
        .validUntil("2026-12-31"))));
```

Operations are grouped by API area (`client.purchaseOrders()`, `client.invoices()`, ...) and named after the operations in the [API Reference](https://pleaxy.ai/api-reference): `CreatePurchaseOrder` is `createPurchaseOrder`. Models are in `ai.pleaxy.model`. A response that is one of several shapes - a buyer's or a supplier's view of an order - is a union class; `getActualInstance()` returns the parsed model. File downloads return a temporary `java.io.File`.

## Errors

A non-2xx response throws `ai.pleaxy.client.ApiException` with `getCode()` (the HTTP status) and `getResponseBody()`. `client.error(e)` parses the body into an `ApiError` with the API's machine-readable `code` when it names one (e.g. `PO_ID_AMBIGUOUS`):

```java
try {
  client.invoices().approveInvoice("INV-1");
} catch (ApiException e) {
  String code = client.error(e).map(ApiError::getCode).orElse(null);
}
```

## Configuration

| Builder method | Default | |
|---|---|---|
| `workspaceId` | required | Every call is scoped to this workspace. |
| `apiKey` / `accessToken` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `baseUrl` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<workspaceId>`. |
| `timeout` | 30 seconds | How long to wait for a response. |
| `httpClientBuilder` | | The `HttpClient.Builder` requests are sent with, e.g. for a proxy. |

## Development

`src/main/java/ai/pleaxy/{api,model,client}` are generated from `../openapi/pleaxy.json` (`./scripts/generate.sh`); don't edit them by hand. `PleaxyClient`, `Downloads` and `pom.xml` are maintained here.

```bash
mvn verify
```

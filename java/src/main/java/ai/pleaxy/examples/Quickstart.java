package ai.pleaxy.examples;

import ai.pleaxy.PleaxyClient;
import ai.pleaxy.client.ApiException;
import ai.pleaxy.model.CreatePurchaseOrderInput;
import ai.pleaxy.model.LineItemInput;
import ai.pleaxy.model.PurchaseOrder;
import java.util.List;

/** The quickstart on pleaxy.ai/sdks. Compiled with the SDK, so it can't drift from it. */
public final class Quickstart {
  private Quickstart() {}

  public static void main(String[] args) {
    PleaxyClient client = PleaxyClient.builder()
        .apiKey(System.getenv("PLEAXY_API_KEY"))
        .workspaceId(System.getenv("PLEAXY_WORKSPACE_ID"))
        .build();

    try {
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
      System.out.println(po.getId() + " " + po.getStatus());
    } catch (ApiException e) {
      System.err.println(e.getCode() + " " + client.error(e).map(err -> err.getCode() + ": " + err.getMessage()).orElse(e.getMessage()));
    }
  }
}

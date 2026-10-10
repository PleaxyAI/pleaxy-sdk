// The quickstart on pleaxy.ai/sdks. Type-checked in CI (npm run typecheck), so it can't drift from the SDK.
import { Pleaxy, PleaxyError } from "../src/index.ts";

const pleaxy = new Pleaxy({
  apiKey: process.env.PLEAXY_API_KEY,
  workspaceId: process.env.PLEAXY_WORKSPACE_ID!,
});

try {
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
  console.log(po.id, po.status);
} catch (err) {
  if (err instanceof PleaxyError) console.error(err.status, err.code, err.message);
  else throw err;
}

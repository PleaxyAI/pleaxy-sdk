// The TypeScript snippets on pleaxy.ai (home page examples, docs, hero panel), as one
// type-checked file, so the site can't show a call the SDK doesn't have.
import { Pleaxy } from "../src/index.ts";

const pleaxy = new Pleaxy({
  apiKey: process.env.PLEAXY_API_KEY,
  workspaceId: process.env.PLEAXY_WORKSPACE_ID!,
});
declare const invoiceId: string;

// Create a purchase order
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
po.status satisfies string | undefined;

// Match an invoice
const result = await pleaxy.invoices.runInvoiceMatch(invoiceId);
if (result.matchStatus === "discrepancy") {
  await pleaxy.invoices.resolveInvoiceDiscrepancy(invoiceId);
}

// Chase a pending approval (supplier)
const invoices = await pleaxy.invoices.listInvoices();
const pending = invoices.filter((inv) => inv.approval?.status === "pending");
for (const inv of pending) {
  await pleaxy.invoices.remindInvoice(inv.id);
}

// Connect a cloud account
const setup = await pleaxy.cloudConnections.initAwsCloudConnection();
const connection = await pleaxy.cloudConnections.createCloudConnection({
  provider: "aws",
  accountLabel: "Production payer",
  awsConnectionId: setup.connectionId,
  roleArn: "arn:aws:iam::912345678901:role/PleaxyBillingRead",
});
connection.status satisfies string | undefined;

// Hero panel
const pos = await pleaxy.purchaseOrders.listPurchaseOrders();
pos.length satisfies number;
const payment = await pleaxy.invoices.getStripePayment(invoiceId);
payment satisfies object;

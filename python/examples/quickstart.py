"""The quickstart on pleaxy.ai/sdks. Type-checked in CI (mypy), so it can't drift from the SDK."""

import os

import pleaxy
from pleaxy.models import CreatePurchaseOrderInput, LineItemInput

client = pleaxy.Client(
    api_key=os.environ["PLEAXY_API_KEY"],
    workspace_id=os.environ["PLEAXY_WORKSPACE_ID"],
)

try:
    po = client.purchase_orders.create_purchase_order(
        body=CreatePurchaseOrderInput(
            supplier="Amazon Web Services",
            provider="aws",
            line_items=[
                LineItemInput(
                    scope_type="sku",
                    scope_id="AWS-EC2-M5LG",
                    name="EC2 m5.large",
                    rule_type="quantity",
                    unit="hr",
                    unit_price=0.096,
                    qty=5000,
                    nte_amount=0,
                    payment_terms="Net 30",
                    valid_from="2026-01-01",
                    valid_until="2026-12-31",
                )
            ],
        )
    )
    print(po.id, po.status)
except pleaxy.PleaxyError as err:
    print(err.status, err.code, err)

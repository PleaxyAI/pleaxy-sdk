# Pleaxy Python SDK

The official Python client for the [Pleaxy API](https://pleaxy.ai/api-reference): purchase orders, invoices and settlement for cloud spend.

```bash
pip install pleaxy
```

Python 3.9+.

## Quickstart

```python
import os

import pleaxy
from pleaxy.models import CreatePurchaseOrderInput, LineItemInput

client = pleaxy.Client(
    api_key=os.environ["PLEAXY_API_KEY"],          # <keyId>.<secret>, minted by a workspace administrator
    workspace_id=os.environ["PLEAXY_WORKSPACE_ID"],  # Company profile → Workspace ID in the Pleaxy console
)

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
```

Methods are grouped by API area (`client.purchase_orders`, `client.invoices`, ...) and named after the operations in the [API Reference](https://pleaxy.ai/api-reference): `CreatePurchaseOrder` is `create_purchase_order`. Request and response models are in `pleaxy.models`; a model's `to_dict()` gives the JSON the API sent, including fields this version of the SDK doesn't know yet (`additional_properties`).

## Errors

Every non-2xx response raises `pleaxy.PleaxyError` with `status`, the API's machine-readable `code` when it names one (e.g. `PO_ID_AMBIGUOUS`), and the parsed `body`.

```python
try:
    client.invoices.approve_invoice("INV-1")
except pleaxy.PleaxyError as err:
    if err.code == "HUMAN_APPROVAL_REQUIRED":
        ...
```

## Configuration

| Argument | Default | |
|---|---|---|
| `workspace_id` | required | Every call is scoped to this workspace. |
| `api_key` / `access_token` | one required | An API key is sent as `X-Api-Key`; a signed-in session's token as `Authorization: Bearer`. |
| `base_url` | `https://api.pleaxy.ai` | The API's origin; the client adds `/v1/workspaces/<workspace_id>`. |
| `timeout` | `30.0` | Seconds, or an `httpx.Timeout`. |
| `httpx_args` | | Passed to `httpx.Client`, e.g. a proxy or a custom transport. |

## Development

The code in `src/pleaxy/_generated` and `src/pleaxy/_resources.py` is generated from `../openapi/pleaxy.json`; don't edit it by hand.

```bash
pip install -r requirements-generate.txt && ./scripts/generate.sh
pip install -e . pytest mypy && pytest && mypy
```

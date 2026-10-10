import json

import httpx
import pytest

import pleaxy
from pleaxy.models import CancelPurchaseOrderInput, PurchaseOrder


def client_with(handler, **kwargs):
    options = {"api_key": "key.secret", "workspace_id": "reg_123.buyer", "base_url": "https://api.example.test/", **kwargs}
    return pleaxy.Client(httpx_args={"transport": httpx.MockTransport(handler)}, **options)


PO = {"id": "PO-1", "supplier": "AWS", "amount": 480, "currency": "USD", "status": "draft", "lineItems": [], "createdAt": "2026-01-01T00:00:00Z"}


def test_sends_the_api_key_to_the_workspace_url():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=PO)

    po = client_with(handler).purchase_orders.get_purchase_order("PO-1", buyer="reg_9.buyer")
    assert str(seen[0].url) == "https://api.example.test/v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer"
    assert seen[0].headers["x-api-key"] == "key.secret"
    assert po.id == "PO-1"


def test_sends_a_json_body_with_a_session_token():
    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(201, json=PO)

    client = client_with(handler, api_key=None, access_token="tok")
    po = client.purchase_orders.cancel_purchase_order("PO-1", body=CancelPurchaseOrderInput(reason="duplicate"))
    assert seen[0].method == "POST"
    assert str(seen[0].url).endswith("/v1/workspaces/reg_123.buyer/purchase-orders/PO-1/cancel")
    assert seen[0].headers["authorization"] == "Bearer tok"
    assert json.loads(seen[0].content) == {"reason": "duplicate"}
    assert isinstance(po, PurchaseOrder)


def test_raises_pleaxy_error_with_the_api_code():
    def handler(request):
        return httpx.Response(409, json={"statusCode": 409, "code": "PO_ID_AMBIGUOUS", "message": "Two buyers issued PO-1"})

    with pytest.raises(pleaxy.PleaxyError) as raised:
        client_with(handler).purchase_orders.get_purchase_order("PO-1")
    assert raised.value.status == 409
    assert raised.value.code == "PO_ID_AMBIGUOUS"
    assert str(raised.value) == "409 PO_ID_AMBIGUOUS: Two buyers issued PO-1"


def test_joins_validation_messages():
    def handler(request):
        return httpx.Response(400, json={"statusCode": 400, "message": ["a is wrong", "b is wrong"], "error": "Bad Request"})

    with pytest.raises(pleaxy.PleaxyError, match="400 a is wrong; b is wrong"):
        client_with(handler).purchase_orders.list_purchase_orders()


def test_returns_a_file_download_as_bytes():
    def handler(request):
        return httpx.Response(200, content=b"invoice,amount\nINV-1,10\n", headers={"Content-Type": "text/csv"})

    assert client_with(handler).invoices.get_payment_export("EXP-1") == b"invoice,amount\nINV-1,10\n"


def test_keeps_fields_the_sdk_does_not_know():
    def handler(request):
        return httpx.Response(200, json={**PO, "someNewField": 1})

    po = client_with(handler).purchase_orders.get_purchase_order("PO-1")
    assert po.to_dict()["someNewField"] == 1


def test_requires_a_workspace_and_a_credential():
    with pytest.raises(ValueError, match="workspace_id is required"):
        pleaxy.Client(api_key="k", workspace_id="")
    with pytest.raises(ValueError, match="api_key or an access_token"):
        pleaxy.Client(workspace_id="w")

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_order_fulfillment import PurchaseOrderFulfillment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/purchase-orders/{po_id}/fulfillment".format(
            po_id=po_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseOrderFulfillment]:
    if response.status_code == 200:
        response_200 = PurchaseOrderFulfillment.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseOrderFulfillment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderFulfillment]:
    """[Both] What the supplier said about an order: { confirmation?, confirmations, shipNotices,
    shippedByLine, expectedDeliveryDate? }. confirmation is the latest (outcome
    accepted|backordered|changed|partial|rejected, lines with status accept|backordered|change|reject,
    qty, unitPrice, dates and reason, and the buyer's decision on a changed one: applied or declined);
    shipNotices are the shipments (status planned|shipped|canceled, carrier, trackingNumber,
    trackingUrl, lines); shippedByLine adds up what shipped, canceled and planned shipments left out. A
    ship notice is never a receipt: what arrives is confirmed with a goods receipt. Takes the same
    ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderFulfillment]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderFulfillment]:
    """[Both] What the supplier said about an order: { confirmation?, confirmations, shipNotices,
    shippedByLine, expectedDeliveryDate? }. confirmation is the latest (outcome
    accepted|backordered|changed|partial|rejected, lines with status accept|backordered|change|reject,
    qty, unitPrice, dates and reason, and the buyer's decision on a changed one: applied or declined);
    shipNotices are the shipments (status planned|shipped|canceled, carrier, trackingNumber,
    trackingUrl, lines); shippedByLine adds up what shipped, canceled and planned shipments left out. A
    ship notice is never a receipt: what arrives is confirmed with a goods receipt. Takes the same
    ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderFulfillment
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderFulfillment]:
    """[Both] What the supplier said about an order: { confirmation?, confirmations, shipNotices,
    shippedByLine, expectedDeliveryDate? }. confirmation is the latest (outcome
    accepted|backordered|changed|partial|rejected, lines with status accept|backordered|change|reject,
    qty, unitPrice, dates and reason, and the buyer's decision on a changed one: applied or declined);
    shipNotices are the shipments (status planned|shipped|canceled, carrier, trackingNumber,
    trackingUrl, lines); shippedByLine adds up what shipped, canceled and planned shipments left out. A
    ship notice is never a receipt: what arrives is confirmed with a goods receipt. Takes the same
    ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderFulfillment]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderFulfillment]:
    """[Both] What the supplier said about an order: { confirmation?, confirmations, shipNotices,
    shippedByLine, expectedDeliveryDate? }. confirmation is the latest (outcome
    accepted|backordered|changed|partial|rejected, lines with status accept|backordered|change|reject,
    qty, unitPrice, dates and reason, and the buyer's decision on a changed one: applied or declined);
    shipNotices are the shipments (status planned|shipped|canceled, carrier, trackingNumber,
    trackingUrl, lines); shippedByLine adds up what shipped, canceled and planned shipments left out. A
    ship notice is never a receipt: what arrives is confirmed with a goods receipt. Takes the same
    ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderFulfillment
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            buyer=buyer,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_order_confirmation_input import CreateOrderConfirmationInput
from ...models.order_confirmation import OrderConfirmation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    body: CreateOrderConfirmationInput,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/confirmations".format(
            po_id=po_id,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OrderConfirmation]:
    if response.status_code == 201:
        response_201 = OrderConfirmation.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrderConfirmation]:
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
    body: CreateOrderConfirmationInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[OrderConfirmation]:
    """[Supplier] Confirm an order, as a cXML ConfirmationRequest would: { type:
    accept|backordered|detail|reject, confirmId?, deliveryDate?, note?, lines?: [{ lineNo, status:
    accept|backordered|change|reject, qty?, unitPrice?, substitute?: { supplierPartId, name },
    shipmentDate?, deliveryDate?, reason? }] }. accept, backordered and reject speak for the whole
    order; detail names its lines, and a line it leaves out is accepted as ordered. A change offers
    another quantity (qty, the new total for the line), unit price (in the order's currency) or item
    (substitute: a part number in your published catalog makes it that catalog item) on a line ordered
    by quantity; one that matches the order is an acceptance. Answers the stored confirmation with its
    outcome: accepted, backordered, changed (for the buyer to apply with ApplyConfirmationChanges or
    decline), partial (some lines refused) or rejected. The buyer's requester and receiver are told when
    the outcome changes, and the buyer's sync feed gets purchase_order.confirmed. The order itself
    doesn't change: a refused order is the buyer's to cancel. Only an open order (awaiting_fulfillment
    or invoiced); 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as GetPurchaseOrder. An API key
    needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateOrderConfirmationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderConfirmation]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
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
    body: CreateOrderConfirmationInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[OrderConfirmation]:
    """[Supplier] Confirm an order, as a cXML ConfirmationRequest would: { type:
    accept|backordered|detail|reject, confirmId?, deliveryDate?, note?, lines?: [{ lineNo, status:
    accept|backordered|change|reject, qty?, unitPrice?, substitute?: { supplierPartId, name },
    shipmentDate?, deliveryDate?, reason? }] }. accept, backordered and reject speak for the whole
    order; detail names its lines, and a line it leaves out is accepted as ordered. A change offers
    another quantity (qty, the new total for the line), unit price (in the order's currency) or item
    (substitute: a part number in your published catalog makes it that catalog item) on a line ordered
    by quantity; one that matches the order is an acceptance. Answers the stored confirmation with its
    outcome: accepted, backordered, changed (for the buyer to apply with ApplyConfirmationChanges or
    decline), partial (some lines refused) or rejected. The buyer's requester and receiver are told when
    the outcome changes, and the buyer's sync feed gets purchase_order.confirmed. The order itself
    doesn't change: a refused order is the buyer's to cancel. Only an open order (awaiting_fulfillment
    or invoiced); 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as GetPurchaseOrder. An API key
    needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateOrderConfirmationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderConfirmation
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        body=body,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOrderConfirmationInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[OrderConfirmation]:
    """[Supplier] Confirm an order, as a cXML ConfirmationRequest would: { type:
    accept|backordered|detail|reject, confirmId?, deliveryDate?, note?, lines?: [{ lineNo, status:
    accept|backordered|change|reject, qty?, unitPrice?, substitute?: { supplierPartId, name },
    shipmentDate?, deliveryDate?, reason? }] }. accept, backordered and reject speak for the whole
    order; detail names its lines, and a line it leaves out is accepted as ordered. A change offers
    another quantity (qty, the new total for the line), unit price (in the order's currency) or item
    (substitute: a part number in your published catalog makes it that catalog item) on a line ordered
    by quantity; one that matches the order is an acceptance. Answers the stored confirmation with its
    outcome: accepted, backordered, changed (for the buyer to apply with ApplyConfirmationChanges or
    decline), partial (some lines refused) or rejected. The buyer's requester and receiver are told when
    the outcome changes, and the buyer's sync feed gets purchase_order.confirmed. The order itself
    doesn't change: a refused order is the buyer's to cancel. Only an open order (awaiting_fulfillment
    or invoiced); 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as GetPurchaseOrder. An API key
    needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateOrderConfirmationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderConfirmation]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateOrderConfirmationInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[OrderConfirmation]:
    """[Supplier] Confirm an order, as a cXML ConfirmationRequest would: { type:
    accept|backordered|detail|reject, confirmId?, deliveryDate?, note?, lines?: [{ lineNo, status:
    accept|backordered|change|reject, qty?, unitPrice?, substitute?: { supplierPartId, name },
    shipmentDate?, deliveryDate?, reason? }] }. accept, backordered and reject speak for the whole
    order; detail names its lines, and a line it leaves out is accepted as ordered. A change offers
    another quantity (qty, the new total for the line), unit price (in the order's currency) or item
    (substitute: a part number in your published catalog makes it that catalog item) on a line ordered
    by quantity; one that matches the order is an acceptance. Answers the stored confirmation with its
    outcome: accepted, backordered, changed (for the buyer to apply with ApplyConfirmationChanges or
    decline), partial (some lines refused) or rejected. The buyer's requester and receiver are told when
    the outcome changes, and the buyer's sync feed gets purchase_order.confirmed. The order itself
    doesn't change: a refused order is the buyer's to cancel. Only an open order (awaiting_fulfillment
    or invoiced); 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as GetPurchaseOrder. An API key
    needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateOrderConfirmationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderConfirmation
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            body=body,
            buyer=buyer,
        )
    ).parsed
